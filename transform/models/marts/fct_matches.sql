with matches as (

    select * from {{ref('stg_sportsapi365__matches')}}
)

select
    match_id                                            as match_id,
    winner_id                                           as winner_id,
    result                                              as result,
    result_type                                         as result_type,
    round_id                                            as round_id,
    tournament_id                                       as tournament_id,
    to_char(match_date_utc, 'YYYYMMDD')::integer        as date_id,
    case
        when player1_id = winner_id then player2_id
        else player1_id
    end                                                 as loser_id

from matches
