from db.connection import get_connection
from utils.config_reader import ConfigReader


def main():

    conn = get_connection()
    print("PostgreSQL 연결 성공!")

    reader = ConfigReader("config/validation_config.xlsx")

    config_df = reader.load()

    print("\nValidation Config")

    for _, row in config_df.iterrows():
        print(f"Validation Name : {row['VALIDATION_NAME']}")
        print(f"Source Table    : {row['SOURCE_TABLE']}")
        print(f"Target Table    : {row['TARGET_TABLE']}")
        print(f"PK Columns      : {row['PK_COLUMNS']}")
        print(f"Group By        : {row['GROUP_BY_COLUMNS']}")
        print(f"Compare Columns : {row['COMPARE_COLUMNS']}")
        print("-" * 50)

    conn.close()


if __name__ == "__main__":
    main()