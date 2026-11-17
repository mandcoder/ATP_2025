-- mart_ranking_2025.sql
-- Grain: en rad per spelare i årslutsrankingen 2025

-- 1. Import
with ranking as (
    select * from {{ref('atp_ranking_2025') }}
),

-- 2 Väljer kolumnerna för dashboarden
final as (
    select
        ranking_position,
        player_name,
        player_country,
        ranking_points
    from ranking
)

--3. Det dbt bygger tabellen från
select * from final
