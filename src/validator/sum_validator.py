from validator.base_validator import BaseValidator


class SumValidator(BaseValidator):

    def validate(self, source_df, target_df, compare_columns):
        """
        지정된 컬럼들의 합계를 비교한다.
        """

        results = []

        columns = [col.strip() for col in compare_columns.split(",")]

        for column in columns:

            source_sum = source_df[column].sum()
            target_sum = target_df[column].sum()

            results.append({
                "column": column,
                "source_sum": source_sum,
                "target_sum": target_sum,
                "result": source_sum == target_sum
            })

        return results