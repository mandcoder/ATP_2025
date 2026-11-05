with winner as (

    select * from {{ ref('stg_sportsapi365__matches')}}
)

    select 
        match_id,
        player1_id,
        winner_id
    
    from winner
    where winner_id != player1_id
    


