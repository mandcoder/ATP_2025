import html

import pandas as pd


def _format_value(
    value: float | int | None,
    total: float | int | None = None,
) -> str:
    """Funktionen tar in value, och gör om till text utan decimaler"""
    if pd.isna(value):
        return ""

    if total is None or pd.isna(total):
        return f"{int(value)}"

    return f"{int(value)} / {int(total)}"


def _build_leaderboard_row_html(
    rank: int,
    player_name: str,
    value: float | int | None,
    total: float | int | None = None,
) -> str:
    """HTML för en rad: placering | namn | värde ."""
    # Namnet kommer från datan och escapas så att < och & visas som text
    name = html.escape(str(player_name))

    return f"""
<div class="lb-row">
    <div class="lb-rank">{rank}</div>
    <div class="lb-name">{name}</div>
    <div class="lb-value">{_format_value(value, total)}</div>
</div>
"""


def build_leaderboard_html(
    top_rows: pd.DataFrame,
    title: str,
    value_column: str,
    total_column: str | None = None,
    rank_column: str | None = None,
) -> str:
    """Topplista: rubrik och en rad per spelare, i den ordning raderna kommer."""
    # Gör om tabellen till en lista med en ordbok per spelare
    players = top_rows.to_dict("records")

    # Bygger HTML för en spelare i taget
    rows = []
    for position, player in enumerate(players, start=1):
        # Placering från datan om rank_column anges, annars löpnummer
        rank = int(player[rank_column]) if rank_column else position
        value = player[value_column]
        total = player[total_column] if total_column else None
        rows.append(
            _build_leaderboard_row_html(rank, player["player_name"], value, total)
        )

    # Slår ihop raderna till en sträng
    rows_html = "".join(rows)

    return (
        f'<div class="lb-card">'
        f'<div class="lb-title">{html.escape(title)}</div>'
        f"{rows_html}"
        f"</div>"
    )
