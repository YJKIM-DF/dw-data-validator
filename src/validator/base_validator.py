from abc import ABC, abstractmethod


class BaseValidator(ABC):
    """
    모든 Validator의 부모 클래스
    """

    @abstractmethod
    def validate(self, source_df, target_df):
        """
        검증 수행

        Parameters
        ----------
        source_df : pandas.DataFrame
            Source 데이터
        target_df : pandas.DataFrame
            Target 데이터

        Returns
        -------
        dict
            검증 결과
        """
        pass