import dlt
from dlt.sources.helpers.rest_client import RESTClient
from dlt.sources.helpers.rest_client.auth import APIKeyAuth
from typing import Any
import logging

logger = logging.getLogger(__name__)


@dlt.source
def sportsapi365(
    base_url: str = dlt.config.value,
    api_key: str = dlt.secrets.value,
    season_ids: list = dlt.config.value,
):
    # The client is created once: the base URL and the API key header are included in every request
    client = RESTClient(
        base_url=base_url,
        auth=APIKeyAuth(name="X-Gravitee-Api-Key", api_key=api_key, location="header"),
    )

    @dlt.resource(write_disposition="merge", primary_key="id")
    def matches():
        for season_id in season_ids:
            # Only the path is needed, the client takes care of the rest
            response = client.get(f"/tournament/results/{season_id}")
            response.raise_for_status()
            match_payload: dict[str, Any] = response.json()
            yield match_payload["data"]["singles"]

    @dlt.resource(write_disposition="replace")
    def player_ranking():
        # Only path is needed, client is take care of the rest
        response = client.get("ranking/singles")
        response.raise_for_status()
        ranking_payload: dict[str, Any] = response.json()
        yield ranking_payload["data"]

    @dlt.resource(write_disposition="merge", primary_key="id")
    def tournament_info():
        for season_id in season_ids:
            response = client.get(f"/tournament/info/{season_id}")
            response.raise_for_status()
            tournament_info_payload: dict[str, Any] = response.json()
            yield tournament_info_payload["data"]

    @dlt.transformer(
        write_disposition="merge", primary_key="match_id", data_from=matches
    )
    def match_statistics(match_payload: list[dict[str, Any]]):
        for match in match_payload:
            response = client.get(
                f"/h2h/match-stats/{match['tournamentId']}/{match['player1Id']}/{match['player2Id']}"
            )
            if response.status_code == 401:
                logger.warning(
                    "No statistics (401) for match %s in tournament %s",
                    match["id"],
                    match["tournamentId"],
                )
                continue
            response.raise_for_status()
            match_statistics_payload: dict[str, Any] = response.json()

            if "data" not in match_statistics_payload:
                logger.warning("No statistics for match %s", match["id"])
                continue

            yield {
                "match_id": match["id"],
                "player1_stats": match_statistics_payload["data"]["player1Stats"],
                "player2_stats": match_statistics_payload["data"]["player2Stats"],
            }

    return matches, player_ranking, tournament_info, match_statistics
