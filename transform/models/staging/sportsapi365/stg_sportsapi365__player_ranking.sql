with player_ranking as (

    select * from {{ source('sportsapi365', 'player_ranking')}}
)

    select

        convert_timezone('UTC',"DATE")::date        as ranking_date,
        PLAYER__ID                                  as player__id,
        PLAYER__NAME                                as player_name,
        PLAYER__COUNTRY__NAME                       as player_country_name,
        PLAYER__COUNTRY__ACRONYM                    as player_country_acronym,
        "POSITION"                                  as ranking_position,
        RANKING_POINTS                              as ranking_points,

    from player_ranking
    



        


