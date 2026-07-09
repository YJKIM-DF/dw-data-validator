import pandas as pd

from validator.base_validator import BaseValidator


class GroupByValidator(BaseValidator):

    def validate(
        self,
        source_df,
        target_df,
        group_by_columns,
        compare_columns
    ):
        """
        Group By 집계 결과를 비교한다.
        """

        groups = [
            col.strip()
            for col in group_by_columns.split(",")
        ]

        compares = [
            col.strip()
            for col in compare_columns.split(",")
        ]

        source_group = (
            source_df
            .groupby(groups)[compares]
            .sum()
            .reset_index()
        )

        target_group = (
            target_df
            .groupby(groups)[compares]
            .sum()
            .reset_index()
        )

        result_df = source_group.merge(
            target_group,
            on=groups,
            how="outer",
            suffixes=("_source", "_target")
        ).fillna(0)

        for column in compares:

            result_df[f"{column}_result"] = (
                result_df[f"{column}_source"]
                == result_df[f"{column}_target"]
            )

        difference_df = result_df[
            ~result_df[
                [f"{column}_result" for column in compares]
            ].all(axis=1)
        ]

        return {
            "validation_type": "GROUP_BY",
            "group_by_columns": groups,
            "compare_columns": compares,
            "result": difference_df.empty,
            "difference_df": difference_df
        }