import streamlit as st
import time
import pymysql
import pandas as pd



st.set_page_config(
    page_title="Hoaii_Zone_Demo7",
    page_icon="📺",
    layout="wide"
)


st.header('影视评论📺系统 V1.0')
st.subheader('《回村三天，二舅治好了我的精神内耗》')
'截止2022-07-28 全站排行榜最高第1名 播放量2973.2w+ 评论5.7w+'
'利用八爪鱼采集器采集到前500条“最热”评论'


# 隐藏右边的菜单以及页脚
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# # 连接数据库
@st.experimental_singleton
def init_connection():
    return pymysql.connect(**st.secrets["mysql"])

conn = init_connection()


@st.experimental_memo(ttl=600)
def run_query(erjiu):
    with conn.cursor() as cur:
        cur.execute(erjiu)
        return cur.fetchall()

# 左边导航栏
sidebar = st.sidebar.radio(
    "导航栏",
    ( "全部评论",)
)

if sidebar == "全部评论":
    '###  全部评论👇👇'
    rows1 = run_query("SELECT * from erjiu;")
    st.dataframe(rows1)
    input = st.text_input('查询关键字')
    if input:
    	chaxun = "select * from erjiu where 评论内容 like '%"+ input + "%';"
    	st.write('查询语句：',chaxun)
    	st.write('查询结果⬇️')
    	rows2 = run_query(chaxun)
    	st.dataframe(rows2)

else :
	'点击左侧选项'

# col1, col2 = st.columns(2)
# col1.markdown("#### 全部数据👇👇")
# with col1:   
#     btn_flag1 = st.button('点击查看')
# col2.markdown("#### 查询👇👇")
# with col2:   
#     btn_flag2 = st.button('点击查询')
# with   col2:
#     
