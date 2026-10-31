import dlt
from dlt.sources.helpers.rest_client import RESTClient
from dlt.sources.helpers.rest_client.auth import APIKeyAuth

@dlt.source
def sportsapi365(
    base_url:str = dlt.config.value,
    api_key: str = dlt.secrets.value,
    season_ids: list = dlt.config.value,
):
    # The client is created once: the base URL and the API key header are included in every request
    client = RESTClient(
        base_url=base_url, auth=APIKeyAuth(name="X-Gravitee-Api-Key", 
                                           api_key=api_key, location="header"),
    )
    
    @dlt.resource(write_disposition="merge", primary_key="id")
    def matches():
        for season_id in season_ids:
            # Only the path is needed, the client takes care of the rest
            response = client.get(f"/tournament/results/{season_id}")
            response.raise_for_status()
            match_payload = response.json()
            yield match_payload["data"]["singles"]
            
            
    @dlt.resource(write_disposition="replace")
    def player_ranking():
        # Only path is needed, client is take care of the rest
        response = client.get("ranking/singles")
        response.raise_for_status()
        ranking_payload = response.json()
        yield ranking_payload["data"]
            
    @dlt.resource(write_disposition="merge", primary_key="id")
    def tournament_info():
        ## fortsätt här enligt ovan
        

    
    