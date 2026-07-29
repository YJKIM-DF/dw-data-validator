class HistoryWriter:

    def __init__(self, connection):

        self.connection = connection

    def save(
        self,
        validation_name,
        count_result,
        sum_result,
        groupby_result,
        rowcompare_result
    ):

        cursor = self.connection.cursor()

        insert_sql = """
        INSERT INTO valid.validation_history
        (
            validation_name,
            count_result,
            sum_result,
            groupby_result,
            rowcompare_result
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s
        )
        """

        cursor.execute(
            insert_sql,
            (
                validation_name,
                "PASS" if count_result else "FAIL",
                "" if not sum_result else "PASS" if all(result["result"] for result in sum_result) else "FAIL",
                "" if not groupby_result else "PASS" if groupby_result["result"] else "FAIL",
                "PASS" if rowcompare_result["result"] else "FAIL"
            )
        )

        self.connection.commit()

        cursor.close()