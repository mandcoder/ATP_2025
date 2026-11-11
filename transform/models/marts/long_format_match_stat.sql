-- grain: en rad per match och statistik
-- långt format för statistiken i matchdiagrammet: vinnarens och förlorarens värde i var sin kolumn.

-- 1. hämtar datan
with stats as (
    select * from {{ref('fct_stats')}}
),

-- vänder statistik kolumner till rader: en rad per spelare, match och statistik.
-- Listan i UNPIOVOT är urvalet, kolumner som inte står här följer inte med.


-- 2. Vänder kolumner till rader
unpivoted as (
    select
        match_id,
        is_winner,
        lower(stat_name) as stat_name, -- UNPIVOT ger kolumnnamnen med versaler
        stat_value
    from stats
        unpivot (
            stat_value for stat_name in (

                first_serves_in,
                aces, 
                second_serves_in,
                double_faults,
                break_points_won,
                break_points_saved,
                total_points_won
               
            )

    )
),

-- 3. Lägg vinnare och förlorare i var sin kolumn.
paired as (
    select
        match_id,
        stat_name,
        max(case when is_winner then stat_value end)        as winner_value,
        max(case when not is_winner then stat_value end)    as loser_value 
    from unpivoted
    group by match_id, stat_name

),

final as (
    select
        match_id,
        stat_name,

        -- Etikett från kolumnnamnet: initcap --> unforced_errors -> Unforced Errors
        initcap(replace(stat_name, '_', ' ')) as stat_label,

        -- Ordningen i matchstat-diagrammet
        case stat_name
            when 'first_serves_in'      then 1
            when 'aces'                 then 2
            when 'second_serves_in'     then 3
            when 'double_faults'        then 4
            when 'break_points_won'     then 5
            when 'break_points_saved'   then 6
            when 'total_points_won'     then 7
        end                                     as sort_order,
        winner_value,
        loser_value
    from paired
                                            
)
select * from final
