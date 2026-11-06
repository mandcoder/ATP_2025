with matches as (

    select * from {{ref('fct_matches')}}
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
)

select
    matches.match_id,
    matches.tournament_id,
    matches.date_id,
    matches.winner_id,
    matches.loser_id,
    matches.round_id,
    matches.result,
    matches.result_type,

    tournaments.tournament_name,
    tournaments.country,
    tournaments.surface,
    tournaments.tournament_type,
    tournaments.city,

    dates.full_date,

    match_winner.player_name as match_winner_name,
    match_winner.player_country as match_winner_country,
    match_loser.player_name as match_loser_name,
    match_loser.player_country as match_loser_country

from matches

left join tournaments                       on tournaments.tournament_id        = matches.tournament_id
left join rounds                            on rounds.round_id                  = matches.round_id
left join dates                             on dates.date_id                    = matches.date_id
left join players       as match_winner     on match_winner.player_id           = matches.winner_id          
left join players       as match_loser      on match_loser.player_id            = matches.loser_id
