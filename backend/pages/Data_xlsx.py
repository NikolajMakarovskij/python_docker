from utils.utils import DataMixin
from core.View import View
import streamlit as st


class DataView(View):
    @classmethod
    def get(cls):
        st.subheader('Считанные файлы')
        st.write(DataMixin.get_files())
        st.subheader('Считанные данные из файлов')
        st.write(DataMixin.get_data())


DataView()