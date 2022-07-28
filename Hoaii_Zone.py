import streamlit as st

st.set_page_config(
    page_title="This is Hoaii_Zone",
    page_icon="👋",
)

st.write('# Welcome to Hoaii_Zone 👋👋')

st.sidebar.success("### 选择一个 Demo 😜")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(
    """
    
    Tools  👉  ***Python ｜ [Streamlit](https://docs.streamlit.io) ｜ Sublime Text｜ Mysql｜ Navicat***
    

    #### About ME
    -  ###### 💰 Work | TNU 
    -  ###### 🌿 Subject | Education Technology International & Chinese Language Education
    -  ###### 🌈 Study | Python & STEAM & NPL & PBL ……
    -  ###### 📧 Contact | [Email](mailto:837088178@qq.com) 

"""
)

with st.expander("🤔 这个网站用于什么??"):
        "Sorry , it's NOTHING. 😅"

with st.expander("🥹 记录下还不太会的操作"):
    '- 修改DataFrame的column字段名'
    "- pymysql(Mysql)+Streamlit下生成词云图"
    "- 上传git总有问题"
    "- 通过Streamlit上传图片，存储到Mysql"
    "- 显示图片有bug"
    "- 数据可视化有bug"
    '######  '
    '       要有人能给予我帮助 我就再苟一苟 没有我就不玩了🫥'



st.sidebar.markdown('# 🤩🤩')
st.sidebar.markdown('### 「 一个学了点教育 , 还学了点技术的伪程序媛👸🏻的人生理想ˉ🍻ˉ」')

'##### 点击左上角 > 按钮，选择一个demo体验吧！🫲'
