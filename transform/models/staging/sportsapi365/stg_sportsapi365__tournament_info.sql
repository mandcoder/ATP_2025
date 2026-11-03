with tournament_info as (

    select * from {{ source('sportsapi365', 'tournament_info')}}
)

    select
        ID                          as tournament_id,
        COUNTRY__NAME               as country_name,
        COURT__NAME                 as court_surface,
        TIER                        as tournament_type, -- ex ATP Masters 1000, Grand Slam
        trim(split_part(NAME, '-', 1)) as tournament_name,
        trim(split_part(NAME, '-', 2)) as city,

    from tournament_info
    