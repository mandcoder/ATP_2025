-- int_stats_per_player.sql
-- Grain: en rad per spelare per match.
-- Unpivot: varje match blir två rader, en för player1 och för player2.

with stats as (
    select * from {{ ref('stg_sportsapi365__match_statistics')}}
)

-- player1:s rad
select
    match_id,
    player1_id                      as player_id,
    player1_aces                    as aces,
    player1_winners                 as winners,
from stats

union all

-- player2:s rad i samma ordning
select
    match_id,
    player2_id                      as player_id,
    player2_aces                    as aces,
    player2_winners                 as winners
from stats
                  