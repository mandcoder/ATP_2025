from typing import NamedTuple

import pandas as pd
import html


class CardRow(NamedTuple):
    """En rad i matchkortet: vad som visas och var värdena finns i mart_matches."""

    label: str  # texten i mitten av raden
    value_column: str  # grundnamn, blir winner_<namn> och loser_<namn>
    total_column: str | None  # grundnamn för totalen, None för antal
    display_type: str  # "count", "percent" eller "fraction"


# Kortets rader, i den ordning de visas uppifrån och ner.
# Ändra ordning, etikett eller visningstyp här.
CARD_ROWS = [
    CardRow("Aces", "aces", None, "count"),
    CardRow("Double Faults", "double_faults", None, "count"),
    CardRow("1st Serves In", "first_serves_in", "first_serves_total", "percent"),
    CardRow("1st Serve Points Won", "first_serves_won", "first_serves_in", "percent"),
    CardRow("2nd Serve Points Won", "second_serves_won", "second_serves_in", "percent"),
    CardRow("Break Points Won", "break_points_won", "break_points_chance", "percent"),
    CardRow("Net Points Won", "net_approaches_won", "net_approaches_total", "percent"),
    CardRow("Total Unforced Errors", "unforced_errors", None, "count"),
    CardRow("Total Winners", "winners", None, "count"),
    CardRow("Total Points Won", "total_points_won", None, "count"),
]


def _format_stat(
    value: float | int | None,
    total: float | int | None,
    display_type: str,
) -> str:
    """Värde och total som text i kortet: 7, 58% eller 7/14."""
    # Saknat värde: tom cell hellre än en påhittad nolla
    if pd.isna(value):
        return ""
    value_int = int(value)

    # Antal visas som det är
    if display_type == "count":
        return f"{value_int}"

    # Procent och kvot behöver en total
    if pd.isna(total):
        return ""
    total_int = int(total)

    if display_type == "fraction":
        return f"{value_int}/{total_int}"

    if display_type == "percent":
        # Ingen chans alls (total 0) visas som 0%, som ATP gör
        if total_int == 0:
            return "0%"
        return f"{value_int / total_int * 100:.0f}%"

    # Okänd visningstyp betyder fel i CARD_ROWS
    raise ValueError(f"Okänd display_type: {display_type}")


def _has_data(card_row: CardRow, match: pd.Series) -> bool:
    """Filterar bort stat-raden om det inte finns något värde"""
    winner_value = match[f"winner_{card_row.value_column}"]
    loser_value = match[f"loser_{card_row.value_column}"]

    return not (pd.isna(winner_value) and pd.isna(loser_value))


def _build_card_row_html(card_row: CardRow, match: pd.Series) -> str:
    """HTML för en rad i kortet: vinnarens värde | etikett | förlorarens värde."""
    # Värdena: grundnamnet blir winner_<namn> och loser_<namn> i mart_matches
    winner_value = match[f"winner_{card_row.value_column}"]
    loser_value = match[f"loser_{card_row.value_column}"]

    # Totalen finns bara för procent och kvot
    if card_row.total_column is None:
        winner_total = None
        loser_total = None
    else:
        winner_total = match[f"winner_{card_row.total_column}"]
        loser_total = match[f"loser_{card_row.total_column}"]

    # Text i cellerna, formaterad efter radens visningstyp
    winner_text = _format_stat(winner_value, winner_total, card_row.display_type)
    loser_text = _format_stat(loser_value, loser_total, card_row.display_type)

    # Etiketten escapas så att tecken som < och & visas som text
    label = html.escape(card_row.label)

    return f"""
<div class="ms-row">
    <div class="ms-value ms-value-winner">{winner_text}</div>
    <div class="ms-label">{label}</div>
    <div class="ms-value">{loser_text}</div>
</div>
"""


def _format_year(full_date: object) -> str:
    """Året ur matchens datum, tom sträng om datumet saknas."""
    if pd.isna(full_date):
        return ""
    return str(pd.to_datetime(full_date).year)


def _build_card_header_html(match: pd.Series) -> str:
    """HTML ovanför kortet: rubrik, turnering, stad och år, resultat, namnrad."""

    # Text från datan escapas så att tecken som < och & visas som text
    tournament_name = html.escape(str(match["tournament_name"]))
    city = html.escape(str(match["city"]))
    year = _format_year(match["full_date"])
    result = html.escape(str(match["result"]))
    winner_name = html.escape(str(match["match_winner_name"]))
    loser_name = html.escape(str(match["match_loser_name"]))

    return f"""
<div class="ms-heading">
    <div class="ms-title">Results</div>
    <div class="ms-tournament">{tournament_name}</div>
    <div class="ms-place">{city} {year}</div>
    <div class="ms-result">{result}</div>
</div>
<div class="ms-names">
    <div class="ms-name-winner">{winner_name}</div>
    <div></div>
    <div>{loser_name}</div>
</div>
"""


def build_match_summary_html(match: pd.Series) -> str:
    """Hela matchkortet: huvud och statistikrader. Stilen finns i sidans CSS-fil."""
    header_html = _build_card_header_html(match)

    # En rad per post i CARD_ROWS, i listans ordning.
    # Rader där ingen spelare har data hoppas över, till exempel
    # statistik som saknas för ATP 1000-turneringar.

    rows_html = "".join(
        _build_card_row_html(card_row, match)
        for card_row in CARD_ROWS
        if _has_data(card_row, match)
    )
    # Huvud och kort i en gemensam behållare, så att de får samma bredd
    return (
        f'<div class="ms-summary">{header_html}'
        f'<div class="ms-card">{rows_html}</div></div>'
    )
