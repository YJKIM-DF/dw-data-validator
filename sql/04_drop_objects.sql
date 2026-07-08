/*
 * File Name : 04_drop_objects.sql
 * Project   : DW Data Validator
 * Author    : 김예지
 * Created   : 2026-07-08
 * Description
 *   - Drop validation objects.
 */

DROP TABLE IF EXISTS valid.validation_history;

DROP TABLE IF EXISTS valid.fact_sales;

DROP TABLE IF EXISTS valid.ods_sales;

DROP SCHEMA IF EXISTS valid;