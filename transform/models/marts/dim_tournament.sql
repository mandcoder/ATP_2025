with tournament as (
    select * from {{ref('stg_sportsapi365__tournament_info')}}
)

select
    tournament_id       as tournament_id,
    tournament_name     as tournament_name,
    country_name        as country,
    court_surface       as surface,
    tournament_type     as tournament_type,
    city                as city,
from tournament
