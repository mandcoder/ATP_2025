import pandas as pd
import streamlit as st

from utils.filters import match_filters
from utils.snowflake_connection import load_matches


st.set_page_config(layout="wide")

matches: pd.DataFrame = load_matches()

_, middle, _ = st.columns([1, 3, 1])

with middle:

    st.title("Tournaments")
    st.markdown("Select tournament and match, to view player statistics")

    # Filtren visas här och returnerar raden för vald match
    selected_match = match_filters(matches)

    if st.button("View match stats"):
        match_id = str(selected_match["match_id"])
        st.session_state["match_id"] = match_id
        st.switch_page(
            "pages/match_stats.py",
            query_params={"match_id": match_id},
        )
