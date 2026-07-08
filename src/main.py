from db.connection import get_connection
from db.query_executor import QueryExecutor
from utils.config_reader import ConfigReader


def main():

    conn = get_connection()

    print("PostgreSQL 연결 성공!")

    reader = ConfigReader("config/validation_config.xlsx")

    config_df = reader.load()

    executor = QueryExecutor(conn)

    for _, row in config_df.iterrows():

        print("\n" + "=" * 60)

        print(f"Validation Name : {row['VALIDATION_NAME']}")

        source_df = executor.get_table_data(row["SOURCE_TABLE"])

        target_df = executor.get_table_data(row["TARGET_TABLE"])

        print(f"ODS Row Count  : {len(source_df)}")

        print(f"FACT Row Count : {len(target_df)}")

        print("\n[ODS]")
        print(source_df)

        print("\n[FACT]")
        print(target_df)

        print("=" * 60)

    conn.close()


if __name__ == "__main__":
    main()