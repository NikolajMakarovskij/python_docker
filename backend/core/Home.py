import streamlit as st
from core.View import View


class IndexView(View):
    @classmethod
    def get(cls):
        st.title('Главная')
        st.subheader('Выберете страницу на панели слева')