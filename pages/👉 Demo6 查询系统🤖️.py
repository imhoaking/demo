import streamlit as st
import pymysql
import pandas as pd
import os
from st_aggrid import AgGrid, DataReturnMode, GridUpdateMode, GridOptionsBuilder


st.set_page_config(
    page_title="Hoaii_Zone_Demo6",
    page_icon="🎬",
)

st.header('豆瓣电影TOP250🎬查询系统  V1.0')


# 隐藏右边的菜单以及页脚
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


col1, col2 = st.columns(2)
col1.markdown("#### 全部数据👇👇")
with col1:   
    btn_flag1 = st.button('点击查看')
col2.markdown("#### 查询👇👇")
with col2:   
    btn_flag2 = st.button('点击查询')
with   col2:
    input = st.text_input('输入电影名称：(仅限TOP250)')

# 连接数据库
@st.experimental_singleton
def init_connection():
    return pymysql.connect(**st.secrets["mysql"])

conn = init_connection()


@st.experimental_memo(ttl=600)
def run_query(dianying):
    with conn.cursor() as cur:
        cur.execute(dianying)
        return cur.fetchall()
    

if btn_flag1:
    
    # 全部数据集
    rows1 = run_query("SELECT * from dianying;")
    st.balloons()
        
    col1.dataframe(rows1)

if btn_flag2:
        # 下面是对的
        # col2.write(input)
    chaxun = "select * from dianying where 电影名称= '"+ input + "';"
        # 下面是对的
        # col2.write(chaxun)
    rows2 = run_query(chaxun)
        # # 'SELECT',input,'111'
    col2.dataframe(rows2)
    # st.write(f'cesh{input}')
 



# with st.expander(f'查看{table}元数据'):
#     print(f'======元数据部分======')
#     print(f'current_table:{table}')
#     print(f'all_table:{all_table.values}')
#     print(f'conn:{conn}')
#     if os.path.exists('db_info_series.csv'):
#         c_db_info = pd.read_csv('db_info_series.csv').values
   

        # print(f'conn:{conn}')
#     if table in all_table.values:
#         schema_sql = f'desc {table}'
#         schema_df = pd.read_sql(schema_sql, conn)
#         st.table(schema_df[['Field', 'Type']])

