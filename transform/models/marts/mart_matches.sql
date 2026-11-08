
--1 Import: en CTE per modell som läses
with matches as (

    select * from {{ref('fct_matches')}}
),

stats as (
    select * from {{ref('fct_stats')}}
),

tournaments as (
    select * from {{ref('dim_tournament')}}
),

rounds as (
    select * from {{ref('dim_round')}}
),

dates as (
    select * from {{ref('dim_date')}}
),

players as (
    select * from {{ref('dim_players')}}
),

final as (

    select

        -- match    
        matches.match_id,
        matches.tournament_id,
        matches.date_id,
        matches.winner_id,
        matches.loser_id,
        matches.round_id,
        matches.result,
        matches.result_type,

        -- tournament
        tournaments.tournament_name,
        tournaments.country,
        tournaments.surface,
        tournaments.tournament_type,
        tournaments.city,

        -- dates
         dates.full_date,

        -- players
        match_winner.player_name as match_winner_name,
        match_winner.player_country as match_winner_country,
        match_loser.player_name as match_loser_name,
        match_loser.player_country as match_loser_country,

        -- winner statistics
        winner_stats.aces                                   as winner_aces,
        winner_stats.average_first_serve_speed              as winner_average_first_serve_speed,         
        winner_stats.average_second_serve_speed             as winner_average_second_serve_speed,
        winner_stats.break_points_chance                    as winner_break_points_chance,
        winner_stats.break_points_saved                     as winner_break_points_saved,
        winner_stats.break_points_faced                     as winner_break_points_faced,
        winner_stats.break_points_won                       as winner_break_points_won,
        winner_stats.double_faults                          as winner_double_faults,
        winner_stats.fastest_serve                          as winner_fastest_serve,
        winner_stats.first_serves_in                        as winner_first_serves_in,
        winner_stats.first_serves_total                     as winner_first_serves_total, 
        winner_stats.first_serves_won                       as winner_first_serves_won,    
        winner_stats.net_approaches_won                     as winner_net_approaches_won,
        winner_stats.net_approaches_total                   as winner_net_approaches_total,
        winner_stats.total_points_won                       as winner_total_points_won, 
        winner_stats.unforced_errors                        as winner_unforced_errors, 
        winner_stats.winners                                as winner_winners, 
        winner_stats.second_serves_won                      as winner_second_serves_won,
        winner_stats.second_serves_in                       as winner_second_serves_in,

        -- losers statistics

        loser_stats.aces                                  as loser_aces,
        loser_stats.average_first_serve_speed             as loser_average_first_serve_speed,         
        loser_stats.average_second_serve_speed            as loser_average_second_serve_speed,
        loser_stats.break_points_chance                   as loser_break_points_chance,
        loser_stats.break_points_saved                    as loser_break_points_saved,
        loser_stats.break_points_faced                    as loser_break_points_faced,
        loser_stats.break_points_won                      as loser_break_points_won,
        loser_stats.double_faults                         as loser_double_faults,
        loser_stats.fastest_serve                         as loser_fastest_serve,
        loser_stats.first_serves_in                       as loser_first_serves_in,
        loser_stats.first_serves_total                    as loser_first_serves_total, 
        loser_stats.first_serves_won                      as loser_first_serves_won,    
        loser_stats.net_approaches_won                    as loser_net_approaches_won,
        loser_stats.net_approaches_total                  as loser_net_approaches_total,
        loser_stats.total_points_won                      as loser_total_points_won, 
        loser_stats.unforced_errors                       as loser_unforced_errors, 
        loser_stats.winners                               as loser_winners, 
        loser_stats.second_serves_won                     as loser_second_serves_won,
        loser_stats.second_serves_in                      as loser_second_serves_in

from matches

left join tournaments                       on tournaments.tournament_id        = matches.tournament_id
left join rounds                            on rounds.round_id                  = matches.round_id
left join dates                             on dates.date_id                    = matches.date_id
left join players       as match_winner     on match_winner.player_id           = matches.winner_id          
left join players       as match_loser      on match_loser.player_id            = matches.loser_id


-- statistiken två gånge: en rad för vinnaren, en för förloraren.
-- match_id + player_id är unikt i fct_stats, så ingen dubblering.

left join stats as winner_stats             on matches.match_id     = winner_stats.match_id
                                            and matches.winner_id   = winner_stats.player_id
left join stats as loser_stats              on matches.match_id     = loser_stats.match_id
                                            and matches.loser_id    = loser_stats.player_id
)
-- 3 final select that dbt builds the table from

select * from final
