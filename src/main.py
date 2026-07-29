from db.connection import get_connection
from db.query_executor import QueryExecutor

from utils.config_reader import ConfigReader

from validator.validator import Validator

from report.excel_report_writer import ExcelReportWriter
from history.history_writer import HistoryWriter


def main():

    # Database 연결
    conn = get_connection()

    print("PostgreSQL 연결 성공!")

    # Validation Config 로드
    reader = ConfigReader("config/validation_config.xlsx")
    config_df = reader.load()

    # 객체 생성
    executor = QueryExecutor(conn)

    validator = Validator()

    report_writer = ExcelReportWriter()
    history_writer = HistoryWriter(conn)

    # Validation 시작
    for _, row in config_df.iterrows():

        print("=" * 60)
        print(f"Validation Name : {row['VALIDATION_NAME']}")

        # Source / Target 데이터 조회
        source_df = executor.get_table_data(
            row["SOURCE_TABLE"]
        )

        target_df = executor.get_table_data(
            row["TARGET_TABLE"]
        )

        # Validation 수행
        count_result = validator.validate_count(
            source_df,
            target_df
        )

        sum_results = validator.validate_sum(
            source_df,
            target_df,
            row["COMPARE_COLUMNS"]
        )

        groupby_result = validator.validate_groupby(
            source_df,
            target_df,
            row["GROUP_BY_COLUMNS"],
            row["COMPARE_COLUMNS"]
        )

        rowcompare_result = validator.validate_rowcompare(
            source_df,
            target_df,
            row["PK_COLUMNS"]
        )

        # ==========================================================
        # Count Validation
        # ==========================================================

        print(
            f"[COUNT] {'PASS' if count_result['result'] else 'FAIL'} "
            f"(Source: {count_result['source_count']}, "
            f"Target: {count_result['target_count']})"
        )

        # ==========================================================
        # Sum Validation
        # ==========================================================

        sum_pass = all(
            result["result"]
            for result in sum_results
        )

        print(
            f"[SUM] {'PASS' if sum_pass else 'FAIL'}"
        )

        # ==========================================================
        # Group By Validation
        # ==========================================================

        print(
            f"[GROUP BY] "
            f"{'PASS' if groupby_result['result'] else 'FAIL'}"
        )

        # ==========================================================
        # Row Compare Validation
        # ==========================================================

        print(
            f"[ROW COMPARE] "
            f"{'PASS' if rowcompare_result['result'] else 'FAIL'}"
        )

        # Excel Report 생성
        report_path = report_writer.write(
            count_result,
            sum_results,
            groupby_result,
            rowcompare_result
        )

        # Validation History 저장
        history_writer.save(
            row["VALIDATION_NAME"],
            count_result["result"],
            sum_results,
            groupby_result,
            rowcompare_result
        )

        print("=" * 60)

        print("Excel Report 생성 완료")

        print(f"저장 위치 : {report_path}")

        print("=" * 60)

    conn.close()


if __name__ == "__main__":
    main()