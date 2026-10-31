
-- ================================================================
-- 02_setup_dbt.sql
-- Roll, användare och rättigheter för dbt
-- ================================================================



--  ---------------------------------------------------------------
-- DEL 1: Roll och användare
-- Kör som USERADMIN, som ansvarar för roller och användare
-- ----------------------------------------------------------------

USE ROLE USERADMIN;

-- rollen som alla dbt-rättigheter samlas på
CREATE ROLE IF NOT EXISTS dbt_role;

-- Användaren som dbt loggar in som
CREATE USER IF NOT EXISTS dbt_transformer
    PASSWORD = 'transform_2025'
    DEFAULT_WAREHOUSE = dev_wh
    LOGIN_NAME = 'dbt_transformer'
    DEFAULT_NAMESPACE= atp_2025.sportsapi365 -- här hamnar användaren vid inloggning
    COMMENT = 'dbt user for transforming data'
    DEFAULT_ROLE = dbt_role;

-- ge rollen till användaren
GRANT ROLE dbt_role TO USER dbt_transformer;

-- Ge rollen till SYSADMIN, så att admin ser objekten dbt skapar
GRANT ROLE dbt_role TO ROLE SYSADMIN;

-- ----------------------------------------------------
-- DEL 2: Rättigheter på warehouse, databas och rådata
-- Kör som SYSADMIN, som äger objekten
-- Mottagare på alla rader: dbt_role
-- ----------------------------------------------------

USE ROLE SYSADMIN;

-- Får köra frågor på warehouse
GRANT USAGE ON WAREHOUSE dev_wh TO ROLE dbt_role;

-- Får se databasen
GRANT USAGE ON DATABASE atp_2025 TO ROLE dbt_role;

-- Får skapa egna scheman (staging, intermediate, marts)
GRANT CREATE SCHEMA ON DATABASE atp_2025 TO ROLE dbt_role;

-- Får se rådatachemat
GRANT USAGE ON SCHEMA atp_2025.sportsapi365 TO ROLE dbt_role;

-- Får läsa alla tabeller som finns i rådataschemat nu
GRANT SELECT ON ALL TABLES IN SCHEMA atp_2025.sportsapi365 TO ROLE dbt_role;


-- ----------------------------------------------------------
-- DEL 3: Future grants
-- Kör som SECURITYADMIN, som har behörigheter MANAGE GRANTS
-- ----------------------------------------------------------

USE ROLE SECURITYADMIN;

-- Får läsa alla tabeller som dlt skapar i rådataschemat i framtiden
GRANT SELECT ON FUTURE TABLES IN SCHEMA atp_2025.sportsapi365 TO ROLE dbt_role;

-- Verifiering -- 
SHOW GRANTS TO ROLE dbt_role;

SHOW FUTURE GRANTS IN SCHEMA atp_2025.sportsapi365;
