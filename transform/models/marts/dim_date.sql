with dates as (

    select * from {{ref('stg_sportsapi365__matches')}}
)

select distinct
    to_char(match_date_utc, 'YYYYMMDD')::integer        as date_id,
    match_date_utc                                      as full_date,
    year(match_date_utc)                                as year,
    month(match_date_utc)                               as month,
    monthname(match_date_utc)                           as month_name,
    weekiso(match_date_utc)                             as week_number,
    dayofweekiso(match_date_utc)                        as day_number,
    dayname(match_date_utc)                             as day_name,

from dates
