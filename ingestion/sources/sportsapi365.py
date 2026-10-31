import dlt
from dlt.sources.helpers import requests
from dlt.sources.helpers.requests import Response


@dlt.resource(write_disposition="merge", primary_key="id")
def matches(
    season_ids: list = dlt.config.value,
    base_url: str = dlt.config.value,
    api_key: str = dlt.secrets.value,
):

    headers = {"X-Gravitee-Api-Key": api_key}

    for season_id in season_ids:
        url = f"{base_url}/tournament/results/{season_id}"
        response: Response = requests.get(url, headers=headers)

        response.raise_for_status()

        match_payload = response.json()

        yield match_payload["data"]["singles"]
