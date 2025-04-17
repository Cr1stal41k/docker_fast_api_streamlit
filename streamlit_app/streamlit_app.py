import streamlit as st
import numpy as np
from requests.models import Response

from src.query.requests import make_request

st.title("Приложение Streamlit!")

idx = st.text_input("Введите ID", "123")
q = st.text_input("Введите уточняющую информацию", None)

if st.button("Отправить запрос", type="primary"):
    response: Response = make_request(idx, q)
    if response.status_code == 200:
        st.badge("Запрос выполнен успешно", icon=":material/check:", color="green")
        st.write(f"Ответ от сервера: {response.json()}")
    else:
        st.badge("⚠️Запрос выполнен с ошибкой", color="red")

col1, col2 = st.columns([3, 1])
data = np.random.randn(10, 1)

col1.subheader("Chart")
col1.line_chart(data)

col2.subheader("Variables")
col2.write(data)