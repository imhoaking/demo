import streamlit as st
import time
import pymysql
import pandas as pd
from wordcloud import WordCloud



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
    rows1 = run_query("SELECT 评论人昵称,评论内容,评论时间  from erjiu;")
    rows3=run_query("SELECT 评论内容 from erjiu;")
    st.dataframe(rows1)
    input = st.text_input('查询关键字')
    if input:
    	chaxun = "select 评论人昵称,评论内容,评论时间 from erjiu where 评论内容 like '%"+ input + "%';"
    	# st.write('查询语句不给看：',chaxun)
    	st.write('查询结果⬇️')
    	rows2 = run_query(chaxun)
    	st.dataframe(rows2)

else :
	'点击左侧选项'


# wd = rows3
# # st.write(type(wd))
# # word = [i[0] for i in wd[['关键词']].values]
# # value = [i[0] for i in wd[['词频']].values]

# cloud =WordCloud()
# cloud = WordCloud(
#         # 文字的路径：本地的系统文件路
#         # 生成词云的图片背景
#         background_color="white",max_words=1300,margin=3,width=1800,height=800,random_state=42
#         # 参考图片（参数，没有引号）
# #         mask=bgImg
#     ).generate(str(wd))
#     # 将做成的结果生成图片
# # cloud.to_file("ciyun.png")
# cloud.to_file("ciyun.png")

