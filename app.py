import streamlit as st
import streamlit.components.v1 as components

# ضبط إعدادات الصفحة لتأخذ العرض الكامل
st.set_page_config(page_title="Lab 4 Dashboard", layout="wide")

# قراءة ملف الـ HTML
with open("dashboard.html", "r", encoding="utf-8") as f:
    html_code = f.read()

# عرض الداشبورد
components.html(html_code, height=900, scrolling=True)