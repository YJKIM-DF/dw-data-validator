class Validator:
    """
    Validation 수행 클래스

    - Count Validation
    - Sum Validation
    - Group By Validation
    - Row Compare Validation
    """

    def _split_columns(self, columns):
        """
        문자열 형태의 컬럼 목록을 List로 변환한다.

        Example)
            "col1,col2,col3"
                ↓
            ["col1", "col2", "col3"]
        """

        return [
            column.strip()
            for column in columns.split(",")
        ]



    def validate_count(self, source_df, target_df):
        """
        Source / Target Row Count를 비교한다.
        """

        source_count = len(source_df)
        target_count = len(target_df)

        return {
            "validation_type": "COUNT",
            "source_count": source_count,
            "target_count": target_count,
            "result": source_count == target_count
        }


    def validate_sum(
        self,
        source_df,
        target_df,
        compare_columns
    ):
        """
        Compare Column의 합계를 비교한다.
        """

        columns = self._split_columns(compare_columns)

        results = []

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


    def validate_groupby(
        self,
        source_df,
        target_df,
        group_by_columns,
        compare_columns
    ):
        """
        Group By 집계 결과를 비교한다.
        """

        groups = self._split_columns(group_by_columns)
        compares = self._split_columns(compare_columns)

        # Source Group By
        source_group = (
            source_df
            .groupby(groups)[compares]
            .sum()
            .reset_index()
        )

        # Target Group By
        target_group = (
            target_df
            .groupby(groups)[compares]
            .sum()
            .reset_index()
        )

        # Group By 결과 Merge
        result_df = (
            source_group
            .merge(
                target_group,
                on=groups,
                how="outer",
                suffixes=("_source", "_target")
            )
            .fillna(0)
        )

        # 집계 결과 비교
        for column in compares:

            result_df[f"{column}_result"] = (
                result_df[f"{column}_source"]
                == result_df[f"{column}_target"]
            )

        # 차이가 발생한 Group만 추출
        difference_df = result_df[
            ~result_df[
                [
                    f"{column}_result"
                    for column in compares
                ]
            ].all(axis=1)
        ]

        return {
            "validation_type": "GROUP_BY",
            "group_by_columns": groups,
            "compare_columns": compares,
            "result": difference_df.empty,
            "difference_df": difference_df
        }


    def validate_rowcompare(
        self,
        source_df,
        target_df,
        pk_columns
    ):
        """
        Primary Key 기준으로
        INSERT / UPDATE / DELETE 데이터를 비교한다.
        """

        # Primary Key
        pks = self._split_columns(pk_columns)

        # 비교 대상 컬럼
        compare_columns = [
            column
            for column in source_df.columns
            if column not in pks
        ]

        # Primary Key를 Index로 변경
        source = source_df.set_index(pks)
        target = target_df.set_index(pks)

        # INSERT 대상
        insert_df = (
            target.loc[
                target.index.difference(source.index)
            ]
            .reset_index()
        )

        # DELETE 대상
        delete_df = (
            source.loc[
                source.index.difference(target.index)
            ]
            .reset_index()
        )

        # UPDATE 대상 확인
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

        # Validation 결과
        result = (
            insert_df.empty
            and delete_df.empty
            and not update_rows
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