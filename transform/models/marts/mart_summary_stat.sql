-- mart_summary_stat.sql
-- Grain: en rad per spelare, över alla matcher i datan.

-- 1. Import
with stats as (
    select * from {{ ref('fct_stats') }}
),

players as (
    select * from {{ ref('dim_players') }}
),

country_codes as (
    select * from {{ ref('country_iso_codes') }}
),

-- 2. Summerar varje spelares matcher
final as (
    select
        stats.player_id,
        players.player_name,
        players.player_country,
        country_codes.iso_code,

        count_if(stats.is_winner)                       as matches_won,
        count(*)                                        as matches_played,
        sum(stats.aces)                                 as total_aces,
        sum(stats.double_faults)                        as total_double_faults,
        sum(stats.winners)                              as total_winners,
        round(total_aces / matches_played, 0)           as average_aces_per_match,
        round(matches_won / matches_played * 100, 0)    as percent_of_match_won

    from stats
    left join players on players.player_id = stats.player_id
    left join country_codes on country_codes.country_code = players.player_country
    group by
        stats.player_id,
        players.player_name,
        players.player_country,
        country_codes.iso_code
)

-- 3. Det dbt bygger tabellen från
select * from final