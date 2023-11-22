import streamlit as st

from utils.utils import DataMixin


class IndexView():

    def get():
        st.title('Title')
        st.subheader('Raw data')
        st.write(DataMixin.get_data())