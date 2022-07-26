import streamlit as st
# import mysql.connector
import pandas as pd
import pymysql




# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return pymysql.connect(host = "rm-bp1vdz5fi246je39cao.mysql.rds.aliyuncs.com",
port = 3306,
database = "dbdemo",
user = "dbdemo",
password = "Haoqing0")

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(zhenqikan):
    with conn.cursor() as cur:
        cur.execute(zhenqikan)
        return cur.fetchall()

rows1 = run_query("SELECT 序号,名称,出版周期,网站 from zhenqikan;")
# 中文字段
# pd.set_option('display.unicode.ambiguous_as_wide', True)
# pd.set_option('display.unicode.east_asian_width', True)


# Print results.
with st.expander("查看国际中文教育期刊（text）"):
    for row1 in rows1:
        st.write(f"{row1[0]}｜{row1[1]}")
    


with st.expander("查看国际中文教育期刊（table）"):
    st.dataframe(rows1)
   
    
 # 下载，还有点问题
 #    @st.cache
 #    def convert_df(row1):
 #     # IMPORTANT: Cache the conversion to prevent computation on every rerun
 #        return df.to_csv().encode('utf-8')
    

 #    csv = convert_df(rows1)

 #    st.download_button(
 #     label="下载",
 #     data=csv,
 #     file_name='hoa_国际中文教育期刊.csv',
 #     # mime='text/csv',
 # )
