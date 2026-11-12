"""Ligande stapeldiagram för spelare"""

import pandas as pd
import plotly.graph_objects as go

COLORS = {"winner": "#2f6fd1", "loser": "#e0b52b"}

AXIS_MAX = 130


def player_bar_chart(stat_rows: pd.DataFrame, match: pd.Series, side: str) -> go.Figure:
    """Liggande stapeldiagram för en spelare.

    Funktionen tar 3 inparametrar:
    - stat_rows:    är raderna för vald match ur "long_format_match_stat"
    - match:        är raden från match_filters, den ger spelarens namn och land.
    - Side:         är "winner" eller "loser" och avgör vilka kolumner som läses.
    """

    # Kontrollerar stavfel för att undvika KeyError
    if side not in COLORS:
        raise ValueError(f"side must be 'winner' eller 'loser', got: {side}")

    if side == "winner":
        mirrored = True
    else:
        mirrored = False

    # f"match_{side}_name"] -> kolumn namnet
    name = match[
        f"match_{side}_name"
    ]  #  if side= winner -> match_winner_name -> players name
    country = match[f"match_{side}_country"]

    fig = go.Figure(
        go.Bar(
            y=stat_rows["stat_lagel"],  # en rad per statistik
            x=stat_rows[f"{side}_share"],  # andel av radens summa
            orientation="h",
            text=stat_rows[f"{side}_value"],  # Det riktiga värdet av vid stapeln
            textposition="outside",  # texten utanför stapelns ände
            hoverinfo="skip",
            marker_color=COLORS["side"],
            width=0.5,
        )
    )

    fig.update_layout(
        go.Layout(
            # Players name and country centered
            title=go.layout.Title(text=f"{name} ({country})", x=0.5, xanchor="center"),
            xaxis=go.layout.YAxis(
                # Reversed, bar goes from left to right
                range=[AXIS_MAX, 0] if mirrored else [0, AXIS_MAX],
                showticklabels=False,
                showgrid=False,
                zeroline=False,
            ),
            yaxis=go.layout.YAxis(
                autorange="reversed",  # sätter första raden överst
                side="right" if mirrored else "left",
            ),
            showlegend=False,
            height=140 + 40 * len(stat_rows),
            font=go.layout.Font(size=16),
            margin=go.layout.Margin(l=10, r=10, t=60, b=10),
            barcornerradius=8,
        )
    )

    return fig
