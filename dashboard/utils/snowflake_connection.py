"""Create a connection to Snowflake and load data for the dashboard"""

from pathlib import Path

import pandas as pd
import streamlit as st

# SQL files lives in dashboard/query one file per mart

QUERIES_DIR = Path(__file__).resolve().parents[1] / "queries"

# Cache results for 10 minutes so every filter click does not hit Snowflake
CACHE_SECONDS = 600


def load_match_and_stats() -> pd.DataFrame:
    """
    Return one row per match_id, from mart_matches.
    Will be used to visualize match_card summary
    """

    sql = (QUERIES_DIR / "match_and_stats.sql").read_text(encoding="utf-8")

    # st.connection reads [connections.snowflake] from .streamlit/secrets.toml

    conn = st.connection("snowflake")
    df = conn.query(sql, ttl=CACHE_SECONDS)

    # Snowflake returns uppercase columna name, therefore they will be convert to lowercase
    df.columns = df.columns.str.lower()
    return df


def load_player_stats() -> pd.DataFrame:
    """
    Return tow rows per match_id, one for each player from mart_stats.
    Will be used for example yearly summary of aces.
    """

    sql = (QUERIES_DIR / "player_stats.sql").read_text(encoding="utf-8")

    # st.connection reads [connection.snowflake] from .streamlit/secrets.toml

    conn = st.connection("snowflake")
    df = conn.query(sql, ttl=CACHE_SECONDS)

    # Snowflake returns uppercase column-name, they will be converted to lowercase
    df.columns = df.columns.str.lower()
    return df


def load_long_table_match_stats() -> pd.DataFrame:
    "return a long table match-stat"

    sql = (QUERIES_DIR / "long_match_and_stats.sql").read_text(encoding="utf-8")

    conn = st.connection("snowflake")
    df = conn.query(sql, ttl=CACHE_SECONDS)

    df.columns = df.columns.str.lower()

    return df
