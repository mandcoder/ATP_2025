USE ROLE SYSADMIN;

SELECT count (*) as rader
FROM sportsapi365.matches;

SELECT *
FROM sportsapi365.matches;

SELECT COUNT(DISTINCT MATCH_ID) as ids
FROM sportsapi365.matches;

SELECT round_id
FROM sportsapi365.matches;

SELECT count (*) as nr_round
FROM sportsapi365.matches
WHERE round_id = 4;  -- resultatet blir 64 -> korrekt

SELECT count (*) as nr_round
FROM sportsapi365.matches
WHERE round_id = 5; -- resultatet blir 31

SELECT count (*) as nr_round
FROM sportsapi365.matches
WHERE round_id = 6; -- resultatet blir 15

SELECT count(*) as nr_round
FROM sportsapi365.matches
WHERE round_id = 7; -- resultatet blir 8

SELECT count(*) as nr_round
FROM sportsapi365.matches
WHERE round_id = 9; -- resultatet blir 4

SELECT count(*) as nr_round
FROM sportsapi365.matches
WHERE round_id = 10; -- resultatet blir 2 

SELECT count(*) as nr_round
FROM sportsapi365.matches
WHERE round_id = 12; -- resultatet blir 1

SELECT * 
FROM sportsapi365.matches
WHERE round_id = 4;

SELECT count(*) as stat_rader
FROM sportsapi365.statistic; -- detta ger 125

SELECT COUNT(DISTINCT match_id)
FROM sportsapi365.statistic;

SELECT COUNT(*) AS stat_utan_match
FROM sportsapi365.statistic s
LEFT JOIN sportsapi365.matches m
    ON s.match_id = m.id
WHERE m.id IS NULL;

SELECT
    id,
    player1__name,
    player2__name,
    result,
    result_type
FROM atp_2025.sportsapi365.matches
WHERE match_winner = player2__id
    AND result_type = 'completed'
LIMIT 5;

SELECT count(*) as player1_vann
FROM atp_2025.sportsapi365.matches
WHERE match_winner = player1__id;

SELECT tournament_id, COUNT(*) AS matcher
FROM atp_2025.sportsapi365.matches
GROUP BY tournament_id
ORDER BY tournament_id;

SELECT column_name
FROM atp_2025.information_schema.columns
WHERE table_schema = 'SPORTSAPI365'
    AND table_name = 'MATCHES'
    AND column_name LIKE 'TOURNAMENT%'
ORDER BY ordinal_position;

SELECT tournament__name, COUNT(*) AS matcher
FROM atp_2025.sportsapi365.matches
GROUP BY tournament__name
ORDER BY matcher DESC;

SHOW GRANTS TO USER mander;