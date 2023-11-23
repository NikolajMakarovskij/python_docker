import pandas as pd
from utils.utils import DataMixin
from core.View import View
import streamlit as st
from datetime import datetime


class FiltredDataView(View, DataMixin):
    cur_year = datetime.now()

    @classmethod
    def get(cls, cur_year=cur_year):
        data = cls.get_data()
        column_name = ['number', 'date']
        data = cls.data_filling(data, column_name)
        st.subheader('Текущий год, станция 2')
        filtered_data = (data['date'] >= cur_year.strftime('%Y')) & (data['station'] == 'two')
        st_two = cls.data_filtered(data, filtered_data)
        st.write(st_two)
        st.subheader('Текущий год, станция 3')
        filtered_data = (data['date'] >= cur_year.strftime('%Y')) & (data['station'] == 'three')
        st_three = cls.data_filtered(data, filtered_data)
        st.write(st_three)
        column_name = 'quantity'  # Костыль! Передать лучше строку. Если передать список, выводится объект,
        # значения которого необходимо выводить через цикл
        sum_st_two = cls.get_column_sum(st_two, column_name)
        sum_st_three = cls.get_column_sum(st_three, column_name)
        output_data = pd.DataFrame([{'station': 'two', '2023': sum_st_two}, {'station': 'three', '2023': sum_st_three}])
        st.subheader('Количество пассажиров')
        st.write(output_data)
        # st.write(sum_st_two)
        # st.write(sum_st_three)


FiltredDataView()
