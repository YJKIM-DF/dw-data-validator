from validator.base_validator import BaseValidator


class CountValidator(BaseValidator):

    def validate(self, source_df, target_df):
        """
        Source / Target Row Count 비교
        """

        source_count = len(source_df)
        target_count = len(target_df)

        return {
            "validation_type": "COUNT",
            "source_count": source_count,
            "target_count": target_count,
            "result": source_count == target_count
        }