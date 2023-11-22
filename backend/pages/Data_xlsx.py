from utils.utils import DataMixin
import streamlit as st


class DataView():

    def get():
        st.subheader('Считанные файлы')
        st.write(DataMixin.get_files())
        st.subheader('Считанные данные из файлов')
        st.write(DataMixin.get_data())


DataView.get()