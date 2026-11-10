import pandas as pd
import streamlit as st


def match_filters(df: pd.DataFrame) -> pd.Series:
    """Visar tunerigs och matchfilter och returnerar raden för vald match.

    df skall redan vara avgränsad till en tunneringstyp, tex. bara Grandslam.
    Funktionen anropas inuti kolumnen på sidan, så filtren hamndar där.
    """

    # Fyra kolumner: två för filtren, tvp tomma som trycker ihop filtren
    # så att de inte fyller hela bredden under bilden

    tournament_col, match_col, _, _ = st.columns([1, 2, 1, 1])

    with tournament_col:
        # Alternativen är tuneringarna som finns i datan.
        selected_tournament = st.selectbox(
            label="Tournament",
            options=df["tournament_name"].unique(),
        )

    with match_col:
        # Bara matcherna från vald tunering, sorterade efter datum
        # så att listan följer turneringens gång

        tour_selected = df[df["tournament_name"] == selected_tournament].sort_values(
            "date_id"
        )

        # Användaren väljer bland ettiketterna, tex "Sinner vs Alexi"

        selected_label = st.selectbox(
            label="Matches",
            options=tour_selected["match_label"],
        )

    # Slå upp raden som hör till vald etikett. Filtreringen ger en DataFram
    # med en rad, iloc[0] plockar ut den raden som en Series

    selected_match = tour_selected[tour_selected["match_label"] == selected_label].iloc[
        0
    ]

    return selected_match
