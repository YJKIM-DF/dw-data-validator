import pandas as pd


class QueryExecutor:

    def __init__(self, connection):
        self.connection = connection

    def get_table_data(self, table_name):

        sql = f"""
        SELECT *
        FROM {table_name}
        ORDER BY 1
        """

        cursor = self.connection.cursor()

        cursor.execute(sql)

        rows = cursor.fetchall()

        columns = [desc[0] for desc in cursor.description]

        df = pd.DataFrame(rows, columns=columns)

        cursor.close()

        return df