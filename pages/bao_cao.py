import streamlit as st


st.set_page_config(layout="wide") #Chỉnh cho layout full trang

col1,col2,col3,col4 = st.columns(4) # => (col1,col2,col3,col4,col5,col6) 

with col1:
    st.metric("Doanh thu hôm nay","đ 12.5M", "5%")
with col2:
    st.metric("Người dùng mới","327", "+12")
with col3:
    st.metric("Đơn hàng","142", "-3")
with col4:
    st.metric("Tỉ lệ chuyển đổi","3.8%", "+0.4%")