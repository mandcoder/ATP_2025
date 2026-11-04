with matches as (

    select * from {{ref('stg_sportsapi365__matches')}}
)

select
    player1_id          as player_id,
    player1_name        as player_name,
    player1_country     as player_country,

from matches

union

select
    player2_id          as player_id,
    player2_name        as player_name,
    player2_country     as player_country,

from matches
