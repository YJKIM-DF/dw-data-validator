from db.connection import get_connection
from db.query_executor import QueryExecutor
from utils.config_reader import ConfigReader

from validator.count_validator import CountValidator
from validator.sum_validator import SumValidator
from validator.groupby_validator import GroupByValidator
from validator.rowcompare_validator import RowCompareValidator

from report.excel_report_writer import ExcelReportWriter

def main():

    conn = get_connection()

    print("PostgreSQL 연결 성공!")

    reader = ConfigReader("config/validation_config.xlsx")

    config_df = reader.load()

    executor = QueryExecutor(conn)

    count_validator = CountValidator()
    sum_validator = SumValidator()
    groupby_validator = GroupByValidator()
    rowcompare_validator = RowCompareValidator()
    
    report_writer = ExcelReportWriter()

    for _, row in config_df.iterrows():

        print("\n" + "=" * 60)

        print(f"Validation Name : {row['VALIDATION_NAME']}")

        source_df = executor.get_table_data(row["SOURCE_TABLE"])
        target_df = executor.get_table_data(row["TARGET_TABLE"])

        count_result = count_validator.validate(
            source_df,
            target_df
        )

        sum_results = sum_validator.validate(
            source_df,
            target_df,
            row["COMPARE_COLUMNS"]
        )

        groupby_result = groupby_validator.validate(
            source_df,
            target_df,
            row["GROUP_BY_COLUMNS"],
            row["COMPARE_COLUMNS"]
        )

        rowcompare_result = rowcompare_validator.validate(
            source_df,
            target_df,
            row["PK_COLUMNS"]
        )

        print("\n[COUNT VALIDATION]")
        print(f"Source Count : {count_result['source_count']}")
        print(f"Target Count : {count_result['target_count']}")
        print(f"Result       : {'PASS' if count_result['result'] else 'FAIL'}")

        print("\n[SUM VALIDATION]")

        for result in sum_results:

            print(f"Column      : {result['column']}")
            print(f"Source Sum  : {result['source_sum']}")
            print(f"Target Sum  : {result['target_sum']}")
            print(f"Result      : {'PASS' if result['result'] else 'FAIL'}")
            print()

        print("\n[GROUP BY VALIDATION]")

        print(
            "Group By Columns : "
            + ", ".join(groupby_result["group_by_columns"])
        )

        print(
            f"Result : {'PASS' if groupby_result['result'] else 'FAIL'}"
        )

        if not groupby_result["result"]:

            print()

            for _, diff in groupby_result["difference_df"].iterrows():

                print("=" * 50)

                print("[Group]")

                for column in groupby_result["group_by_columns"]:
                    print(f"{column} : {diff[column]}")

                print()

                print("[Compare]")

                for column in groupby_result["compare_columns"]:

                    print(column)

                    print(
                        f"  Source : {diff[column + '_source']}"
                    )

                    print(
                        f"  Target : {diff[column + '_target']}"
                    )

                    print(
                        "  Result : "
                        + (
                            "PASS"
                            if diff[column + "_result"]
                            else "FAIL"
                        )
                    )

                    print()

        print("\n[ROW COMPARE VALIDATION]")

        print(
            "PK Columns : "
            + ", ".join(rowcompare_result["pk_columns"])
        )

        print(
            f"Result : {'PASS' if rowcompare_result['result'] else 'FAIL'}"
        )

        if rowcompare_result["update_rows"]:

            print("\n" + "=" * 50)
            print("[UPDATE]")

            for update in rowcompare_result["update_rows"]:

                print()

                print(f"sale_id : {update['pk']}")

                print()

                for change in update["changes"]:

                    print(change["column"])

                    print(
                        f"  Source : {change['source']}"
                    )

                    print(
                        f"  Target : {change['target']}"
                    )

                    print()

        if not rowcompare_result["delete_rows"].empty:

            print("=" * 50)
            print("[DELETE]")

            print()

            for _, delete in rowcompare_result["delete_rows"].iterrows():

                print(
                    f"sale_id : {delete['sale_id']}"
                )

            print()

        if not rowcompare_result["insert_rows"].empty:

            print("=" * 50)
            print("[INSERT]")

            print()

            for _, insert in rowcompare_result["insert_rows"].iterrows():

                print(
                    f"sale_id : {insert['sale_id']}"
                )

            print()

        print("=" * 60)

        report_path = report_writer.write(
            count_result,
            sum_results,
            groupby_result,
            rowcompare_result
        )

        print("\n" + "=" * 60)

        print("Excel Report 생성 완료")

        print(f"저장 위치 : {report_path}")

        print("=" * 60)

    conn.close()


if __name__ == "__main__":
    main()