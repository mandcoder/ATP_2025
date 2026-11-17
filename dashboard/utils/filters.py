import pandas as pd
import streamlit as st


def match_filters(matches: pd.DataFrame) -> pd.Series:
    """
    Visar tunering och matchfilter och returnerar raden för vald match.
    """

    # Walkovers har ingen statistik och skall inte gå att välja
    played_df = matches[matches["result_type"] != "walkover"]

    level_col, tournament_col, match_col, _, _ = st.columns([1, 1, 2, 1, 1])

    ## step 1: select tournament level
    with level_col:

        selected_level = st.selectbox(
            label="Tournament Level",
            options=played_df["tournament_type"].unique(),
        )

    # bara tuneringarna efter vald nivå
    is_selected_level: pd.Series = played_df["tournament_type"] == selected_level
    level_df: pd.DataFrame = played_df[is_selected_level]

    # Step 2: select tournament
    with tournament_col:
        # Alternativen är tuneringarna som finns i datan.
        selected_tournament = st.selectbox(
            label="Tournament",
            options=level_df["tournament_name"].unique(),
        )

    # bara matcherna i vald turnering, i turneringens ordning
    is_selected_tournament: pd.Series = (
        level_df["tournament_name"] == selected_tournament
    )
    tournament_df: pd.DataFrame = level_df[is_selected_tournament].sort_values(
        "date_id"
    )

    # Step 3: select match from selected tournament
    with match_col:
        selected_match_label = st.selectbox(
            label="Matches",
            options=tournament_df["match_label"],
        )

    # hela raden för vald match, iloc[0] plockar ut den som en Series
    is_selected_match: pd.Series = tournament_df["match_label"] == selected_match_label
    selected_match: pd.Series = tournament_df[is_selected_match].iloc[0]

    return selected_match
