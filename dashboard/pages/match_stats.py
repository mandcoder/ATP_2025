import streamlit as st

from utils.snowflake_connection import load_matches, load_stat_comparisons
from utils.match_stats_chart_butterfly import match_stats_chart

if st.button("Back"):
    st.switch_page("pages/tournaments.py")

# ingen match vald: visa felmeddelande och stoppa här

match_id_text = st.query_params.get("match_id") or st.session_state.get("match_id")

if match_id_text is None:
    st.info("No match selected. Go back and choose a match.")
    st.stop()

# Lägg tillbaka id:t i adressen, så att en omladdning också fungerar

st.query_params["match_id"] = match_id_text

# Gör om från text till tal så det matchar tabellen
match_id = int(match_id_text)

# Alla matcher, en rad per match
matches = load_matches()

# Raden för matchen i adressen. Finns inget sådant id, stoppa med meddelande
is_selected_match = matches["match_id"] == match_id
if not is_selected_match.any():
    st.info("Match not found. Go back and choose a match.")
    st.stop()
selected_match = matches[is_selected_match].iloc[0]

# Alla jämförelser, en rad per statistik per match
stat_comparisons = load_stat_comparisons()

# True på raderna som hör till vald match
is_selected = stat_comparisons["match_id"] == match_id

# Jämförelserna är vald match, i den ordning som diagrammet ska visa dem
selected_comparision = stat_comparisons[is_selected].sort_values("sort_order")


# Resultatet och vinnaren, centrerade

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

# match_stats_chart(selected_comparision, is_selected)
st.dataframe(selected_comparision)
