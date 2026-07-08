/*
 * File Name : 03_insert_sample_data.sql
 * Project   : DW Data Validator
 * Author    : 김예지
 * Created   : 2026-07-08
 * Description
 *   - Insert sample data into validation tables.
 */

INSERT INTO valid.ods_sales
(sale_id, sale_dt, store_cd, product_cd, qty, sale_amt)
VALUES
(1, '2026-07-01', 'S001', 'P001', 2, 1000),
(2, '2026-07-01', 'S001', 'P002', 1, 2000),
(3, '2026-07-01', 'S002', 'P001', 3, 3000),
(4, '2026-07-02', 'S001', 'P003', 2, 4000),
(5, '2026-07-02', 'S002', 'P002', 5, 5000);

INSERT INTO valid.fact_sales
(sale_id, sale_dt, store_cd, product_cd, qty, sale_amt)
VALUES
(1, '2026-07-01', 'S001', 'P001', 2, 1000),
(2, '2026-07-01', 'S001', 'P002', 1, 2000),
(3, '2026-07-01', 'S002', 'P001', 3, 3500),   -- 금액 변경
(5, '2026-07-02', 'S002', 'P002', 5, 5000),   -- sale_id=4 누락
(6, '2026-07-02', 'S003', 'P004', 1, 6000);   -- 추가 데이터