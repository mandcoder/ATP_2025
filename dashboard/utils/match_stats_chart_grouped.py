"""Grupperat stapeldiagram för statistiken i en vald match."""

import pandas as pd
import plotly.graph_objects as go


# Samma färger som de andra diagrammen
WINNER_COLOR = "#2f6fd1"
LOSER_COLOR = "#e0b52b"


def match_stats_chart(stat_rows: pd.DataFrame, match: pd.Series) -> go.Figure:
    """Två staplar per statistik, båda från vänster: vinnaren och förloraren.

    inparametrar:
     - stat_rows är för vald match ur long_format_match_stat, sorterade på sort_order
     - match är raden från match_filters, den ger spelarnas namn.
    """

    fig = go.Figure()

    # Vinnarens staplar. Längden är andelen, texten det riktiga värdet
    fig.add_trace(
        go.Bar(
            y=stat_rows["stat_label"],
            x=stat_rows["winner_share"],
            orientation="h",
            name=match["match_winner_name"],  # namnet i legenden
            text=stat_rows["winner_value"],
            textposition="outside",  # värdet efter stapelns ände
            textfont=go.bar.Textfont(color=WINNER_COLOR),  # samma färg som stapeln
            hoverinfo="skip",
            marker_color=WINNER_COLOR,
        )
    )

    # Förlorarens staplar, läggs bredvid vinnarens i samma rad
    fig.add_trace(
        go.Bar(
            y=stat_rows["stat_label"],
            x=stat_rows["loser_share"],
            orientation="h",
            name=match["match_loser_name"],
            text=stat_rows["loser_value"],
            textposition="outside",
            textfont=go.bar.Textfont(color=LOSER_COLOR),
            hoverinfo="skip",
            marker_color=LOSER_COLOR,
        )
    )

    fig.update_layout(
        go.Layout(
            barmode="group",  # staplarna bredvid varandra inom varje rad
            bargap=0.25,  # luft mellan raderna
            bargroupgap=0.2,  # liten luft mellan de två staplarna i en rad
            xaxis=go.layout.XAxis(
                range=[0, 110],  # 100 är maxandel, resten är plats för texten
                showticklabels=False,  # andelarna betyder inget för läsaren
                showgrid=False,
                zeroline=False,
            ),
            yaxis=go.layout.YAxis(
                autorange="reversed",  # första raden överst
                ticksuffix="  ",  # luft mellan etikett och stapel
                tickfont=go.layout.yaxis.Tickfont(size=15),
            ),
            legend=go.layout.Legend(
                orientation="h",
                x=1,
                xanchor="right",  # uppe till höger, som i exemplet
                y=1.08,
                font=go.layout.legend.Font(size=16),
            ),
            height=140 + 60 * len(stat_rows),  # två staplar per rad kräver mer höjd
            font=go.layout.Font(size=16, color="#b5b0a8"),
            margin=go.layout.Margin(l=10, r=10, t=60, b=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            barcornerradius=8,
        )
    )

    return fig
