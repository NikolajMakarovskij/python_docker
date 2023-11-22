from dataclasses import dataclass
import os
import pandas as pd


@dataclass
class DataMixin:
    data_from_xlsx: dict = None
    path: str = './data'

    @classmethod
    def get_files(cls, path=path) -> list:
        files = os.listdir(path)
        files_xls = [f for f in files if f[-4:] == 'xlsx' or f[-3:] == 'xls']
        return files_xls

    @classmethod
    def get_data(cls, path=path) -> list:
        files_xls = cls.get_files(path)
        df = []
        for f in files_xls:
            data = pd.read_excel(F'{path}/{f}', None)
            df.append(data)
        return df

#    @classmethod
#   def write_xlsx(cls) -> None:
#        df = cls.get_data()
#        writer = pd.ExcelWriter('output.xlsx')
#        df.to_excel(writer, None)
