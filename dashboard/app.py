import streamlit as st

from utils.snowflake_connection import load_match_and_stats, load_player_stats
from utils.path_helpers import PICT_PATH
from utils.filters import side_bar_filters

st.set_page_config(layout="wide")  # denna måste ligga först

side_bar_filters()


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
df = load_match_and_stats()

total_matches = len(df)

total_cities = df["city"].nunique()
total_countries = df["tournament_country"].nunique()
total_tournaments = df["tournament_name"].nunique()

with middle:

    st.image(PICT_PATH / "ATP_main_page.png", width="stretch")

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        st.metric(label="Matches", value=total_matches)

    with kpi2:
        st.metric(label="Tournaments", value=total_tournaments)

    with kpi3:
        st.metric(label="Cities", value=total_cities)

    with kpi4:
        st.metric(label="Countries", value=total_countries)
