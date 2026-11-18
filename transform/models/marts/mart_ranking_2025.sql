-- mart_ranking_2025.sql
-- Grain: en rad per spelare i årsslutsrankingen 2025.

-- 1. Import
with ranking as (
    select * from {{ ref('atp_ranking_2025') }}
),

country_codes as (
    select * from {{ ref('country_iso_codes') }}
),

-- 2. Väljer kolumnerna och lägger till ISO-koden för flaggan
final as (
    select
        ranking.ranking_position,
        ranking.player_name,
        ranking.player_country,
        country_codes.iso_code,
        ranking.ranking_points
    from ranking
    left join country_codes on country_codes.country_code = ranking.player_country
)

-- 3. Det dbt bygger tabellen från
select * from final