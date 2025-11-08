import streamlit as st

#Trên web chỉ có 1 sidebar duy nhất
#st.sidebar.widget
st.sidebar.title("Menu")

with st.sidebar.expander("Quản trị",True):
    select_menu = st.radio("Menu",["Menu item 1","Menu item 2", "Menu item 3"])

st.sidebar.markdown("<hr />",True)


