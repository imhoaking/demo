import streamlit as st
import time
import pymysql
import pandas as pd
import time
# import cv2
import numpy as np



st.set_page_config(
    page_title="Hoaii_Zone_Demo8",
    page_icon="🥰",
    layout="wide"
)

st.header('致敬用户🥰')
st.info('感谢你点击到这个界面，谢谢支持啦，填个表单再走呗♥️')
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
def run_query(user11):
	with conn.cursor() as cur:
	    cur.execute(user11)
	    return cur.fetchall()

name=st.text_input('1.你的姓名')
email = st.text_input('2.你的邮箱')

# date = st.date_input('3.你的生日')
# # st.write(date)
hobby = st.multiselect('3.你的爱好',
        ('阅读', '运动','躺着','追剧','游戏','工作','购物','美食','社交','编程','其他'))
work=st.text_input('4.你的职业')
talk = st.text_area('5.想说点啥🤭')


if st.button('提交'):
	mylist = hobby
	hobby1 = "  ".join(mylist)
	insert= "insert into user11(name,email,hobby,talk,work) values ('%s','%s','%s','%s','%s')" % (name,email,hobby1,talk,work)
	# '查询语句：',insert
	run_query(insert)
	conn.commit()
	with st.spinner('稍等一下下...'):
		time.sleep(1)
	st.success('好嘞！提交成功!')
