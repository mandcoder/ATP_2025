import streamlit as st

from utils.filters import match_filters
from utils.path_helpers import PICT_PATH
from utils.snowflake_connection import load_match_and_stats, load_long_table_match_stats
from utils.match_stats_chart_2 import match_stats_chart


st.set_page_config(layout="wide")

# data, hämtar allt och avgränsar till den här sidanstuneringstyp
long_match_stat_df = load_long_table_match_stats()
df = load_match_and_stats()
df_grandslam = df[df["tournament_type"] == "Grand Slam"]

# picture
left, middle, right = st.columns([1, 6, 1])

with middle:
    # det som är unikt för denna sidan, dvs bilden i detta fallet
    st.image(PICT_PATH / "grand_slam.png", width="stretch")

    # filter
    selected_match = match_filters(df_grandslam)

    long_m_stat_df = long_match_stat_df[
        long_match_stat_df["match_id"] == selected_match["match_id"]
    ].sort_values("sort_order")

    fig = match_stats_chart(long_m_stat_df, selected_match)
    st.plotly_chart(fig, width="stretch")
