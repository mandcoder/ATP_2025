with match_statistics as (
    
    select * from {{source('sportsapi365', 'match_statistics')}}
)

    select

        try_cast(MATCH_ID as integer)                   as match_id,
        --player1 statistic
        PLAYER1_STATS__ACES                             as player1_aces,
        PLAYER1_STATS__AVERAGE_FIRST_SERVE_SPEED        as player1_average_first_serve_speed,
        PLAYER1_STATS__AVERAGE_SECOND_SERVE_SPEED       as player1_average_second_serve_speed,
        PLAYER1_STATS__BREAK_POINT_CHANCE_GM            as player1_break_point_chance,
        PLAYER1_STATS__BREAK_POINT_FACED_GM             as player1_break_point_faced,
        PLAYER1_STATS__BREAK_POINT_SAVED_GM             as player1_break_point_saved,
        PLAYER1_STATS__BREAK_POINT_WON_GM               as player1_break_points_won,
        PLAYER1_STATS__DOUBLE_FAULTS                    as player1_double_faults,
        PLAYER1_STATS__FASTEST_SERVE                    as player1_fastest_serve,
        PLAYER1_STATS__FIRST_SERVE                      as player1_first_serve_in,
        PLAYER1_STATS__FIRST_SERVE_OF                   as player1_first_serve_total,
        PLAYER1_STATS__NET_APPROACHES                   as player1_net_approaches_won,
        PLAYER1_STATS__NET_APPROACHES_OF                as player1_net_approaches_total,
        PLAYER1_STATS__PLAYER1_ID                       as player1_id,
        PLAYER1_STATS__TOTAL_POINTS_WON                 as player1_total_points_won,
        PLAYER1_STATS__UNFORCED_ERRORS                  as player1_unforced_errors,
        PLAYER1_STATS__WINNERS                          as player1_winners,
        PLAYER1_STATS__WINNING_ON_FIRST_SERVE           as player1_winning_on_first_serve,
        PLAYER1_STATS__WINNING_ON_SECOND_SERVE          as player1_winning_on_second_serve,
        PLAYER1_STATS__WINNING_ON_SECOND_SERVE_OF       as player1_second_serves_in,

        --player2 statistic

        PLAYER2_STATS__ACES                             as player2_aces,
        PLAYER2_STATS__AVERAGE_FIRST_SERVE_SPEED        as player2_average_first_serve_speed,
        PLAYER2_STATS__AVERAGE_SECOND_SERVE_SPEED       as player2_average_second_serve_speed,
        PLAYER2_STATS__BREAK_POINT_CHANCE_GM            as player2_break_point_chance,
        PLAYER2_STATS__BREAK_POINT_FACED_GM             as player2_break_point_faced,
        PLAYER2_STATS__BREAK_POINT_SAVED_GM             as player2_break_point_saved,
        PLAYER2_STATS__BREAK_POINT_WON_GM               as player2_break_points_won,
        PLAYER2_STATS__DOUBLE_FAULTS                    as player2_double_faults,
        PLAYER2_STATS__FASTEST_SERVE                    as player2_fastest_serve,
        PLAYER2_STATS__FIRST_SERVE                      as player2_first_serve_in,
        PLAYER2_STATS__FIRST_SERVE_OF                   as player2_first_serve_total,
        PLAYER2_STATS__NET_APPROACHES                   as player2_net_approaches_won,
        PLAYER2_STATS__NET_APPROACHES_OF                as player2_net_approaches_total,
        PLAYER2_STATS__PLAYER2_ID                       as player2_id,
        PLAYER2_STATS__TOTAL_POINTS_WON                 as player2_total_points_won,
        PLAYER2_STATS__UNFORCED_ERRORS                  as player2_unforced_errors,
        PLAYER2_STATS__WINNERS                          as player2_winners,
        PLAYER2_STATS__WINNING_ON_FIRST_SERVE           as player2_winning_on_first_serve,
        PLAYER2_STATS__WINNING_ON_SECOND_SERVE          as player2_winning_on_second_serve,
        PLAYER2_STATS__WINNING_ON_SECOND_SERVE_OF       as player2_second_serv_in,

    from match_statistics





