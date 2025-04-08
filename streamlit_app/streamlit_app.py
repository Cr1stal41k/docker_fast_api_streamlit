import streamlit as st

from src.query.requests import make_request

st.title("Приложение Streamlit!")

idx = st.text_input("Введите ID", "123")
q = st.text_input("Введите уточняющую", None)

if st.button("Отправить запрос", type="primary"):
    response: dict = make_request(idx, q)
    st.write(f"Ответ от сервера: {response}")
