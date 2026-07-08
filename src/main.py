from db.connection import get_connection
from db.query_executor import QueryExecutor
from utils.config_reader import ConfigReader

from validator.count_validator import CountValidator

def main():

    conn = get_connection()

    print("PostgreSQL 연결 성공!")

    reader = ConfigReader("config/validation_config.xlsx")

    config_df = reader.load()

    executor = QueryExecutor(conn)
    count_validator = CountValidator()

    for _, row in config_df.iterrows():

        print("\n" + "=" * 60)

        print(f"Validation Name : {row['VALIDATION_NAME']}")

        source_df = executor.get_table_data(row["SOURCE_TABLE"])

        target_df = executor.get_table_data(row["TARGET_TABLE"])

        count_result = count_validator.validate(
            source_df,
            target_df
        )

        print("\n[COUNT VALIDATION]")
        print(f"Source Count : {count_result['source_count']}")
        print(f"Target Count : {count_result['target_count']}")
        print(f"Result       : {'PASS' if count_result['result'] else 'FAIL'}")

        print("=" * 60)

    conn.close()


if __name__ == "__main__":
    main()