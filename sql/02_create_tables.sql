/*
 * File Name : 02_create_tables.sql
 * Project   : DW Data Validator
 * Author    : 김예지
 * Created   : 2026-07-08
 * Description
 *   - Create sample tables for validation.
 */

-- ods_sales
CREATE TABLE valid.ods_sales (
    sale_id      INTEGER PRIMARY KEY,
    sale_dt      DATE,
    store_cd     VARCHAR(10),
    product_cd   VARCHAR(20),
    qty          INTEGER,
    sale_amt     NUMERIC(15,2)
);

-- fact_sales
CREATE TABLE valid.fact_sales (
    sale_id      INTEGER PRIMARY KEY,
    sale_dt      DATE,
    store_cd     VARCHAR(10),
    product_cd   VARCHAR(20),
    qty          INTEGER,
    sale_amt     NUMERIC(15,2)
);

-- validation_history
CREATE TABLE valid.validation_history (
    history_id SERIAL PRIMARY KEY,
    validation_time TIMESTAMP,
    source_table VARCHAR(100),
    target_table VARCHAR(100),
    validation_type VARCHAR(50),
    result VARCHAR(20),
    message TEXT
);