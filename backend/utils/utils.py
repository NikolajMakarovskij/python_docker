from dataclasses import dataclass
import os
import pandas as pd


@dataclass
class DataMixin:
    """Набор методов для обработки данных"""
    path: str = './data'

    @classmethod
    def get_files(cls, path=path) -> list:
        """Возвращает список файлов"""
        files = os.listdir(path)
        files_xls = [f for f in files if f[-4:] == 'xlsx' or f[-3:] == 'xls']
        return files_xls

    @classmethod
    def get_data(cls, path=path) -> dict:
        """Возвращает данные из файлов"""
        files_xls = cls.get_files(path)
        lst = []
        for f in files_xls:
            data = pd.read_excel(F'{path}/{f}', None,)
            for item in data.values():
                lst.append(item)
        df = pd.concat([item for item in lst])
        df = pd.DataFrame(df)
        return df

    @classmethod
    def data_filling(cls, data: dict = None, column_name: list = None) -> dict:
        """Заполняет пустые данные в столбце"""
        df = data
        df[column_name] = df[column_name].fillna(method='ffill')
        return df

    @classmethod
    def data_filtered(cls, data: dict = None, filtered_data: str = None) -> dict:
        """Возвращает отфильтрованные данные"""
        data_filtered = data.loc[filtered_data]
        return data_filtered

    @classmethod
    def get_column_sum(cls, data: dict = None, column_name: list = None) -> float:
        """Возвращает сумму столбца"""
        column_sum = data[column_name].sum()
        return column_sum
