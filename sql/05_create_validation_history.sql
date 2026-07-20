/*
 * File Name : 05_create_validation_history.sql
 * Project   : DW Data Validator
 * Author    : 김예지
 * Created   : 2026-07-17
 * Description
 *   - Create validation history table.
 */

DROP TABLE IF EXISTS valid.validation_history;

CREATE TABLE valid.validation_history
(
    history_id       SERIAL PRIMARY KEY,
    validation_name  VARCHAR(100) NOT NULL,
    count_result     VARCHAR(10) NOT NULL,
    sum_result       VARCHAR(10) NOT NULL,
    groupby_result   VARCHAR(10) NOT NULL,
    rowcompare_result VARCHAR(10) NOT NULL,
    run_dt           TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);