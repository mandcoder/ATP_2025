-- grain: en rad per spelare per match.

with stats as (
    select * from {{ref('int_stats_per_player') }}
),

matches as (
    select * from {{ ref('fct_matches') }}
)

select
    s.match_id                      as match_id,
    s.player_id                     as player_id,
    m.tournament_id                 as tournament_id,
    m.date_id                       as date_id,
    m.round_id                      as round_id,
    s.aces                          as aces,
    s.average_first_serve_speed     as average_first_serve_speed,
    s.average_second_serve_speed    as average_second_serve_speed,
    s.break_points_chance           as break_points_chance,
    s.break_points_saved            as break_points_saved,
    s.break_points_faced            as break_points_faced,
    s.double_faults                 as double_faults,
    s.fastest_serve                 as fastest_serve,
    s.first_serves_in               as first_serves_in,
    s.first_serves_total            as first_serves_total,
    s.net_approaches_won            as net_approaches_won,
    s.net_approaches_total          as net_approaches_total,
    s.total_points_won              as total_points_won,
    s.unforced_errors               as unforced_errors,
    s.winners                       as winners,
    s.first_serves_won              as first_serves_won,
    s.second_serves_won             as second_serves_won,
    s.second_serves_in              as second_serves_in,
    
    s.player_id = m.winner_id       as is_winner,
from stats s
inner join matches m
    on s.match_id = m.match_id
