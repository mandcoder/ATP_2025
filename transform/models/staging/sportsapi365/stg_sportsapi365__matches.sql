-- stg_sportsapi365__matches.sql
-- Grain: en rad per match
-- Städad version av sportsapi365.matches

with matches as (

    select * from {{ source('sportsapi365', 'matches')}}
)
    
    select
        -- Konverterar källans tidpunkt till UTC och byter typ till tidsstämpel utan tidszon, t.ex. 2025-05-25 14:30:00
        convert_timezone('UTC', "DATE")::timestamp_ntz      as match_started_at_utc,
       -- Konverterar källans tidpunkt till UTC och behåller bara datumdelen, t.ex. 2025-05-25
        convert_timezone('UTC', "DATE")::date               as match_date_utc,
        try_cast(ID as integer)                             as match_id,
        MATCH_WINNER                                        as winner_id,
        PLAYER1__COUNTRY_ACR                                as player1_country,
        PLAYER1__ID                                         as player1_id,
        PLAYER1__NAME                                       as player1_name,
        PLAYER2__COUNTRY_ACR                                as player2_country,
        PLAYER2__ID                                         as player2_id,
        PLAYER2__NAME                                       as player2_name,
        RESULT                                              as result,
        RESULT_TYPE                                         as result_type,
        ROUND_ID                                            as round_id,
        TOURNAMENT__ID                                      as tournament_id,
    from matches
    

