import streamlit as st
import time
import pymysql
import pandas as pd



st.set_page_config(
    page_title="Hoaii_Zone_Demo8",
    page_icon="👩‍💻",
    layout="wide"
)

st.header('运维管理👩‍💻后台系统  V1.0 ')
st.warning('暂未上线')
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
def run_query(dianying):
    with conn.cursor() as cur:
        cur.execute(dianying)
        return cur.fetchall()

# 左边导航栏
sidebar = st.sidebar.radio(
    "导航栏👇",
    ( "项目管理", "用户管理", "权限管理")
)


# col1, col2 = st.columns(2)
# col1.markdown("#### 全部数据👇👇")
# with col1:   
#     btn_flag1 = st.button('点击查看')
# col2.markdown("#### 查询👇👇")
# with col2:   
#     btn_flag2 = st.button('点击查询')
# with   col2:
#     input = st.text_input('输入电影名称：(仅限TOP250)')


    

#     col1.dataframe(rows1)

# if btn_flag2:
#         # 下面是对的
#         # col2.write(input)
#     chaxun = "select * from dianying where 电影名称= '"+ input + "';"
#         # 下面是对的
#         # col2.write(chaxun)
#     rows2 = run_query(chaxun)
#         # # 'SELECT',input,'111'
#     col2.dataframe(rows2)
#     # st.write(f'cesh{input}')




# if sidebar == "项目管理":
#     st.subtitle("项目管理")
#     # 项目选择框
#     project_name = st.selectbox(
#         "请选择项目",
#         ["项目A", "项目B"]
#     )
#     if project_name:
#         # 表单
#         with st.form(project_name):
#             project_info_1 = st.text_input("项目信息1", project_name)
#             project_info_2 = st.text_input("项目信息2", project_name)
#             project_info_3 = st.text_input("项目信息3", project_name)
#             submitted = st.form_submit_button("提交")
#             if submitted:
#                 # 在这里添加真实的业务逻辑
#                 # 这是一个进度条
#                 bar = st.progress(0)
#                 for i in range(100):
#                     time.sleep(0.01)
#                     bar.progress(i)
#                 st.write("项目信息1:%s, 项目信息2:%s, 项目信息3:%s" % (project_info_1, project_info_2, project_info_3))
#                 st.success("提交成功")


# elif sidebar == "用户管理":
#     st.title("用户管理")
#     # 将页面分为左半边和右半边
#     left, right = st.beta_columns(2)
#     # 左半边页面展示部分
#     with left:
#         st.header("查看、更新用户信息")
#         user_name = st.selectbox(
#             "请选择用户",
#             ["郑立赛", "乔布斯", "王大拿"]
#         )
#         if user_name:
#             with st.form(user_name):
#                 phone_num = st.text_input("手机号", user_name)
#                 role = st.multiselect(
#                     "用户角色",
#                     ["大神", "大拿"],
#                     ["大神"]
#                 )
#                 user_group = st.multiselect(
#                     "请选择用户组",
#                     ["大神组", "大拿组"],
#                     ["大神组"]
#                 )
#                 submitted = st.form_submit_button("提交")
#                 if submitted:
#                     # 这里添加真实的业务逻辑
#                     st.write("用户名:%s, 手机号:%s, 用户角色:%s, 用户组:%s" % (user_name, phone_num, role, user_group))
#                     st.success("提交成功")
#     # 右半边页面展示部分
#     with right:
#         st.header("添加、删除用户")
#         user_action = st.selectbox(
#             "请选择操作",
#             ["添加用户", "删除用户"]
#         )
#         if user_action:
#             with st.form(user_action):
#                 if user_action == "添加用户":
#                     phone_num = st.text_input("手机号", user_name)
#                     role = st.multiselect(
#                         "用户角色",
#                         ["大神", "大拿"]
#                     )
#                     user_group = st.multiselect(
#                         "请选择用户组",
#                         ["大神组", "大拿组"]
#                     )
#                     submitted = st.form_submit_button("提交")
#                     if submitted:
#                         # 请在这里添加真实业务逻辑，或者单独写一个业务逻辑函数
#                         st.write("user_name:%s, phone_num:%s, role:%s, user_group:%s" % (user_name, phone_num, role, user_group))
#                         st.success("提交成功")
#                 else:
#                     user_group = st.multiselect(
#                         "请选择要删除的用户",
#                         ["郑立赛", "乔布斯", "王大拿"]
#                     )
#                     submitted = st.form_submit_button("提交")
#                     if submitted:
#                         # 请在这里添加真实业务逻辑，或者单独写一个业务逻辑函数
#                         st.write("user_name:%s, phone_num:%s, role:%s, user_group:%s" % (user_name, phone_num, role, user_group))
#                         st.success("提交成功")
# elif sidebar == "权限管理":
#     st.title("权限管理")
#     with st.form("auth"):
#         user = st.multiselect(
#             "选择用户",
#             ["郑立赛", "乔布斯", "王大拿"]
#         )
#         role = st.multiselect(
#             "选择用户角色",
#             ["大神", "大拿"]
#         )
#         user_group = st.multiselect(
#             "请选择用户组",
#             ["大神组", "大拿组"]
#         )
#         submitted = st.form_submit_button("提交")
#         if submitted:
#             # 请在这里添加真实业务逻辑，或者单独写一个业务逻辑函数
#             st.write(
#                 "用户:%s, 角色:%s, 用户组:%s" % (user, role, user_group))
#             st.success("提交成功")
