import streamlit as st
import pymysql
import pandas as pd
import os

st.set_page_config(
    page_title="Hoaii_Zone_Demo6",
    page_icon="🎬",
)

st.header('豆瓣电影TOP250🎬查询系统  V1.0')

# 抽取全局参数
all_table = pd.Series(['default_table'])
table = 'default'
conn = ''
btn_flag = True

print('===============')



# 页面布局第二行四列
col20, col_block, col21, col22, col23 = st.columns([2, 1, 2, 1, 2])
with col20:
    db_type = st.selectbox(
        '数据库类型',
        ['MySQL', 'Postgres', 'Hive']
    )

    with st.expander('数据库参数'):
        host_name = st.text_input('Host', value='localhost')
        port = st.text_input('Port', value=3306)
        user_name = st.text_input('User', value='root')
        user_pass = st.text_input('Password', value='root')
        db_name = st.text_input('db', value='test')

    btn_flag = st.button('点击连接')
    if btn_flag:
        st.balloons()
        print('========数据库连接部分========')
        conn = pymysql.connect(
            host=host_name,
            user=user_name,
            password=user_pass,
            port=int(port),
            db=db_name,
            charset='utf8'
        )
        db_info = [host_name, port, user_name, user_pass, db_name]
        db_info_series = pd.Series(db_info)
        db_info_series.to_csv('db_info_series.csv')
        print(f'save db_info to csv success!')
        tables_sql = 'show tables'
        tables = pd.read_sql(tables_sql, conn)
        all_table = tables[tables.columns.values[0]]
        table = all_table[0]
        all_table.to_csv('all_table.csv')
        print(f'save all_table to csv success!')

with col21:
    st.success(f'表列表显示')
    print(f'======表下拉框部分========')
    if os.path.exists('all_table.csv'):
        c_tables = pd.read_csv('all_table.csv')
        all_table = c_tables[c_tables.columns.values[1]]
        table = all_table[0]
    if table in all_table.values:
        table = st.selectbox(
            '',
            all_table
        )

with st.expander(f'查看{table}元数据'):
    print(f'======元数据部分======')
    print(f'current_table:{table}')
    print(f'all_table:{all_table.values}')
    print(f'conn:{conn}')
    if os.path.exists('db_info_series.csv'):
        c_db_info = pd.read_csv('db_info_series.csv').values
        conn = pymysql.connect(
            host=c_db_info[0][1],
            user=c_db_info[2][1],
            password=c_db_info[3][1],
            port=int(c_db_info[1][1]),
            db=c_db_info[4][1],
            charset='utf8'
        )
        print(f'conn:{conn}')
    if table in all_table.values:
        schema_sql = f'desc {table}'
        schema_df = pd.read_sql(schema_sql, conn)
        st.table(schema_df[['Field', 'Type']])

with col23:
    st.success(f'{table}数据')
    print(f'======数据展示部分======')
    print(f'current_table:{table}')
    print(f'all_table:{all_table.values}')
    if table in all_table.values:
        query_sql = f'select * from {table}'
        query_df = pd.read_sql(query_sql, conn)
        st.table(query_df)
