import streamlit as st

from utils.filters import match_filters
from utils.snowflake_connection import load_match_and_stats, load_long_table_match_stats
from utils.match_stats_chart_grouped import match_stats_chart


st.set_page_config(layout="wide")


st.html(
    """
<style>
.st-key-match_stats_chart {
    background-color: #191612;  /* ytans färg */
    border-radius: 16px;        /* rundade hörn */
    padding: 1.25rem 1.5rem;    /* luft runt diagrammet */
}
</style>
"""
)

# data, hämtar allt och avgränsar till den här sidanstuneringstyp
long_match_stat_df = load_long_table_match_stats()
df = load_match_and_stats()
df_grandslam = df[df["tournament_type"] == "Grand Slam"]


left, middle, right = st.columns([1, 3, 1])


with middle:

    st.title("Grand Slam tournaments")
    st.markdown("Select tournament and match, to view player statisics")

    # filter
    selected_match = match_filters(df_grandslam)

    long_m_stat_df = long_match_stat_df[
        long_match_stat_df["match_id"] == selected_match["match_id"]
    ].sort_values("sort_order")

    fig = match_stats_chart(long_m_stat_df, selected_match)
    with st.container(key="match_stats_chart"):
        # Resultatet och vinnaren centrerade över diagrammet.
        # st.html tolkar strängen som HTML direkt, indragningen spelar ingen roll
        st.html(
            f"""
            <p style='text-align:center; font-size:1.7rem; margin:0;'>
                {selected_match['result']}
            </p>
            <p style='text-align:center; font-size:1.4rem; color:#2f6fd1; margin:0;'>
                {selected_match['match_winner_name']}
            </p>
            """
        )
        st.plotly_chart(fig, width="stretch")
