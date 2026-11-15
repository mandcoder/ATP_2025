import streamlit as st

from utils.constants import STYLING_PATH
from utils.match_summary_card import build_match_summary_html
from utils.snowflake_connection import load_matches


# Sidans egen stil: bakgrund och kortet. Laddas först så att allt nedan får den.
st.html(STYLING_PATH / "match_stats.css")

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

# Matchkortet: huvud och statistik, allt från matchraden
st.html(build_match_summary_html(selected_match))
