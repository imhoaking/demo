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

btn_flag = st.button('点击连接')
if btn_flag:
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
    
    

    # 全部数据集
    rows1 = run_query("SELECT 电影名称,年份,豆瓣打分 from dianying;")
    st.balloons()

    col1, col2 = st.columns(2)
    col1.markdown("#### 全部数据")
    col1.dataframe(rows1)
  




    col2.markdown("#### 图表")
    # col1.line_chart(rows1)

    



#     db_type = st.selectbox(

#     )

#     with st.expander('数据库参数'):
       
#         db_info_series = pd.Series(db_info)
        

#         tables_sql = 'show tables'
#         tables = pd.read_sql(tables_sql, conn)
#         all_table = tables[tables.columns.values[0]]
#         table = all_table[0]
      

# with col21:
#     st.success(f'表列表显示')
#     print(f'======表下拉框部分========')
#     if os.path.exists('all_table.csv'):
#         c_tables = pd.read_csv('all_table.csv')
#         all_table = c_tables[c_tables.columns.values[1]]
#         table = all_table[0]
#     if table in all_table.values:
#         table = st.selectbox(
#             '',
#             all_table
#         )

# with st.expander(f'查看{table}元数据'):
#     print(f'======元数据部分======')
#     print(f'current_table:{table}')
#     print(f'all_table:{all_table.values}')
#     print(f'conn:{conn}')
#     if os.path.exists('db_info_series.csv'):
#         c_db_info = pd.read_csv('db_info_series.csv').values
   

#         print(f'conn:{conn}')
#     if table in all_table.values:
#         schema_sql = f'desc {table}'
#         schema_df = pd.read_sql(schema_sql, conn)
#         st.table(schema_df[['Field', 'Type']])

