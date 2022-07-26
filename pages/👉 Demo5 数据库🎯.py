import streamlit as st
import pymysql

st.set_page_config(
    page_title="Hoaii_Zone_Demo5",
    page_icon="🎯",
)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
	return pymysql.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(zhenqikan):
    with conn.cursor() as cur:
        cur.execute(zhenqikan)
        return cur.fetchall()

rows1 = run_query("SELECT 序号,名称,出版周期,网站 from zhenqikan;")


# Print results.
with st.expander("查看国际中文教育期刊（text）"):
    for row1 in rows1:
        st.write(f"{row1[0]}｜{row1[1]}")
    


with st.expander("查看国际中文教育期刊（table）"):
    st.dataframe(rows1)
   

   
