from db.connection import get_connection


def main():

    conn = get_connection()

    print("PostgreSQL 연결 성공!")

    conn.close()


if __name__ == "__main__":
    main()