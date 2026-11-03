-- int_stats_per_player.sql
-- Grain: en rad per spelare per match.
-- Unpivot: varje match blir två rader, en för player1 och för player2.

with stats as (
    select * from {{ ref('stg_sportsapi365__match_statistics')}}
)

-- player1:s rad
select
    match_id,
    player1_id                          as player_id,
    player1_aces                        as aces,
    player1_average_first_serve_speed   as average_first_serve_speed,  
    player1_average_second_serve_speed  as average_second_serve_speed,
    player1_break_point_chance          as break_points_chance,
    player1_break_points_saved          as break_points_saved,
    player1_break_points_faced          as break_points_faced,
    player1_break_points_won            as break_points_won,
    player1_double_faults               as double_faults,
    player1_fastest_serve               as fastest_serve,
    player1_first_serve_in              as first_serves_in,
    player1_first_serve_total           as first_serves_total,
    player1_net_approaches_won          as net_approaches_won,
    player1_net_approaches_total        as net_approaches_total,
    player1_total_points_won            as total_points_won,
    player1_unforced_errors             as unforced_errors,
    player1_winners                     as winners,
    player1_winning_on_first_serve      as first_serves_won,
    player1_winning_on_second_serve     as second_serves_won,
    player1_second_serves_in            as second_serves_in,












from stats

union all

-- player2:s rad i samma ordning
select
    match_id,
    player2_id                      as player_id,
    player2_aces                    as aces,
    player2_winners                 as winners
from stats
    