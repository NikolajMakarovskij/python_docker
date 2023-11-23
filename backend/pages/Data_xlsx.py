import pandas as pd
from utils.utils import DataMixin
from core.View import View
import streamlit as st


class DataView(View):
    @classmethod
    def get(cls):
        st.subheader('Считанные файлы')
        df = pd.DataFrame(DataMixin.get_files())
        st.write('Количество записей', list(df.count()), 'Список файлов', df, )
        st.subheader('Считанные данные из файлов')
        df = DataMixin.get_data()
        st.write('Количество Записей', list(df.count()), 'Записи', df)


DataView()
