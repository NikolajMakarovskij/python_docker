from dataclasses import dataclass
import os
import pandas as pd


@dataclass
class Data:
    data_from_xlsx: dict = None

    @classmethod
    def get_files(cls, path=None) -> list:
        files = os.listdir(path)
        files_xls = [f for f in files if f[-4:] == 'xlsx']
        return files_xls

    @classmethod
    def get_data(cls) -> list:
        path = './data_xls'
        files_xls = Data.get_files(path)
        df = []
        for f in files_xls:
            data = pd.read_excel(F'{path}/{f}', None)
            df.append(data)
        return df

    @classmethod
    def write_xlsx(cls) -> None:
        df = Data.get_data()
        writer = pd.ExcelWriter('output.xlsx')
        df.to_excel(writer, 'sheet1')
