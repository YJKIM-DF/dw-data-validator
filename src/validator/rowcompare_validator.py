from validator.base_validator import BaseValidator


class RowCompareValidator(BaseValidator):

    def validate(
        self,
        source_df,
        target_df,
        pk_columns
    ):

        pks = [
            col.strip()
            for col in pk_columns.split(",")
        ]

        compare_columns = [
            column
            for column in source_df.columns
            if column not in pks
        ]

        source = source_df.set_index(pks)
        target = target_df.set_index(pks)

        insert_df = (
            target.loc[
                target.index.difference(source.index)
            ]
            .reset_index()
        )

        delete_df = (
            source.loc[
                source.index.difference(target.index)
            ]
            .reset_index()
        )

        common_index = source.index.intersection(target.index)

        update_rows = []

        for pk in common_index:

            source_row = source.loc[pk]
            target_row = target.loc[pk]

            changes = []

            for column in compare_columns:

                if source_row[column] != target_row[column]:

                    changes.append({
                        "column": column,
                        "source": source_row[column],
                        "target": target_row[column]
                    })

            if changes:

                update_rows.append({
                    "pk": pk,
                    "changes": changes
                })

        result = (
            insert_df.empty
            and delete_df.empty
            and len(update_rows) == 0
        )

        return {
            "validation_type": "ROW_COMPARE",
            "result": result,
            "pk_columns": pks,
            "compare_columns": compare_columns,
            "insert_rows": insert_df,
            "delete_rows": delete_df,
            "update_rows": update_rows
        }