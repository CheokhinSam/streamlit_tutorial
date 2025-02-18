import streamlit as st

# 設定的標題
st.title('我的第一個 Streamlit 應用')

# 添加文本
st.write('這是一個簡單的 Streamlit 演示')

# 添加一個滑塊
st.write('添加一個滑塊')
number = st.slider('選擇一個數字', 0, 100, 50)
st.write('您選擇的數字是:', number)

# 添加一個按鈕
st.write('添加一個按鈕')
if st.button('點擊我'):
    st.write('您點擊了按鈕！')

# 添加輸入框
st.write('添加輸入框')
name = st.text_input('輸入您的名字')
st.write('您輸入的名字是:', name)

# 顯示一個用戶的消息
st.write('顯示一個用戶的消息')
st.chat_message("user").write("你好，你今天過得如何？")

# 顯示一個助手的消息
st.write('顯示一個助手的消息')
st.chat_message("assistant").write("我很好，謝謝你！今天你呢？")

st.write('_______________________________')

# 創建一個聊天輸入框
st.write('創建一個聊天輸入框')
user_input = st.chat_input("請輸入您的問題或評論...")

# 檢查是否有用戶輸入
st.write('檢查是否有用戶輸入')
if user_input:
    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write("我收到您的消息：" + user_input)