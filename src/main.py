from db.connection import get_connection
from db.query_executor import QueryExecutor
from utils.config_reader import ConfigReader

from validator.count_validator import CountValidator
from validator.sum_validator import SumValidator

def main():

    conn = get_connection()

    print("PostgreSQL 연결 성공!")

    reader = ConfigReader("config/validation_config.xlsx")

    config_df = reader.load()

    executor = QueryExecutor(conn)

    count_validator = CountValidator()
    sum_validator = SumValidator()

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

        print("=" * 60)

    conn.close()


if __name__ == "__main__":
    main()