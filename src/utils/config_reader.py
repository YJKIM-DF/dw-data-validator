import pandas as pd


class ConfigReader:
    """
    Excel 설정파일 Reader
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        """
        ValidationConfig Sheet 읽기
        """

        df = pd.read_excel(
            self.file_path,
            sheet_name="ValidationConfig"
        )

        return df