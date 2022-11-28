# %%
import streamlit as st
from datetime import datetime
import pandas as pd
from scripts.helper_fuctions import read_txt_file, to_excel

st.title('РАСЧЕТ ПОКАЗАТЕЛЕЙ СМЕШИВАНИЯ')

items_txt = r"./data/actual_items.txt"

items = read_txt_file(items_txt)
item_discr = ['Цельное', "Измельченное", "Верхнее сито 5-7", "Крупный порошок", "РПС"]
indicator_discr = ['Действующие вещества', "Золы"]

order_num = st.text_input("Номер заказа")
item = st.selectbox('Номенклатура', items),
indicator = st.selectbox("Индикатор", indicator_discr),

columns = st.number_input('Введите количество компонентов для смешивания',
min_value=1, max_value=5)
cols = st.columns(columns)

input_dict = {}
for id, column in enumerate(cols):
    with column:
        st.header(f"Компонент {id + 1}")
        input_dict[id] = [
                          datetime.now(),
                          order_num,
                          item[0],
                          st.selectbox(f"Характеристика {id + 1}", item_discr),
                          st.text_input(f'Номер серии {id + 1}'),
                          st.number_input(f'Количество {id + 1}'),
                          st.number_input(f'Значение {id + 1}')]
    

if st.button('Рассчитать'):
    data = pd.DataFrame.from_dict(input_dict, orient='index', 
    columns=['Дата', 'Номер заказа', 'Наименование', 'Характеристика', 'Номер серии',
    'Количество', 'Значение'])
    st.write(data)

    avg = (data['Количество']*data['Значение']).sum() / data['Количество'].sum()
    st.write("Среднее значение показателя:", round(avg, 2))

    df_xlsx = to_excel(data)
    st.download_button(label='📥 Скачать исходные данные',
                                    data=df_xlsx ,
                                    file_name= f'data_{item[0]}.xlsx')
# %%
