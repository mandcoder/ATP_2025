import logging
import dlt

from sources.sportsapi365 import sportsapi365


def run_pipeline():

    pipeline = dlt.pipeline(
        "Atp_2025", destination="snowflake", dataset_name="sportsapi365", progress="log"
    )

    load_info = pipeline.run(sportsapi365())
    print(load_info)


if __name__ == "__main__":

    logging.basicConfig(level=logging.INFO)
    run_pipeline()
