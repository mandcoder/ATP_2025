import streamlit as st

from utils.snowflake_connection import load_matches
from utils.snowflake_connection import load_yearly_player_stat
from utils.constants import STYLING_PATH
from utils.leader_board_aces import build_leaderboard_html

st.set_page_config(layout="wide")  # denna måste ligga först


# Sidans egen stil: bakgrund och kortet. Laddas först så att allt nedan får den.
st.html(STYLING_PATH / "home_page.css")

st.markdown(
    """
    <style>
    
       [data-testid="stMetricLabel"]{
            
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        [data-testid="stMetricValue"]{
        
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

left, middle, right = st.columns([1, 6, 1])
df = load_matches()
yearly_player_stat = load_yearly_player_stat()

top_10_player_aces = yearly_player_stat

total_players = len(yearly_player_stat)
total_matches = len(df)

total_cities = df["city"].nunique()
total_countries = df["tournament_country"].nunique()
total_tournaments = df["tournament_name"].nunique()


with middle:

    with st.container(border=True):

        # st.image(PICT_PATH / "ATP_main_page.png", width="stretch")

        kpi1, kpi2, kpi3, kpi4, kpi5 = st.columns(5)

        with kpi1:
            st.metric(label="Players", value=total_players)

        with kpi2:
            st.metric(label="Matches", value=total_matches)

        with kpi3:
            st.metric(label="Tournaments", value=total_tournaments)

        with kpi4:
            st.metric(label="Cities", value=total_cities)

        with kpi5:
            st.metric(label="Countries", value=total_countries)

    _, table_column = st.columns([2, 1])

    with table_column:

        top_aces = yearly_player_stat.sort_values("total_aces", ascending=False).head(5)
        st.html(build_leaderboard_html(top_aces, "Most aces", "total_aces"))
