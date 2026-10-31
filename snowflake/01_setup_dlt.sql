USE ROLE USERADMIN;


-- skapar användare --
CREATE USER IF NOT EXISTS api_extractor
    PASSWORD = "tennis_Tour_2025"
    DEFAULT_WAREHOUSE = dev_wh;


-- Skapar roller --
CREATE ROLE IF NOT EXISTS api_dlt_role;


-- tilldelar roller till användare --
GRANT ROLE api_dlt_role TO USER api_extractor;

GRANT ROLE api_dlt_role TO USER mander;

-- tilldelar rättigheter till roller --
GRANT USAGE ON WAREHOUSE dev_wh TO ROLE api_dlt_role;

GRANT USAGE ON DATABASE atp_2025 TO ROLE api_dlt_role;

GRANT USAGE ON SCHEMA atp_2025.staging TO ROLE api_dlt_role;

GRANT USAGE ON SCHEMA atp_2025.sportsapi365 TO ROLE api_dlt_role;

GRANT USAGE ON SCHEMA sportsapi365_staging TO ROLE api_dlt_role;

GRANT CREATE TABLE ON SCHEMA sportsapi365_staging TO ROLE api_dlt_role;

GRANT CREATE TABLE ON SCHEMA atp_2025.sportsapi365 TO api_dlt_role;

GRANT CREATE TABLE ON SCHEMA atp_2025.staging TO api_dlt_role;

GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA atp_2025.staging TO ROLE api_dlt_role;

GRANT SELECT, INSERT, UPDATE, DELETE ON FUTURE TABLES IN SCHEMA atp_2025.staging TO ROLE api_dlt_role;