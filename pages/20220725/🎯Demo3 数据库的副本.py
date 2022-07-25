import pandas as pd
import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
from bokeh.plotting import figure
import graphviz
from PIL import Image
import mysql.connector

# streamlit_app.py

import streamlit as st
import mysql.connector

# Initialize connection.
# Uses st.experimental_singleton to only run once.
@st.experimental_singleton
def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(movie):
    with conn.cursor() as cur:
        cur.execute(movie)
        return cur.fetchall()

rows = run_query("SELECT * from movie_name;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")


# progress_bar = st.progress(0)
# status_text = st.empty()
# chart = st.line_chart(np.random.randn(10, 2))

# for i in range(100):
#     # Update progress bar.
#     progress_bar.progress(i + 1)

#     new_rows = np.random.randn(10, 2)

#     # Update status text.
#     status_text.text(
#         'The latest random number is: %s' % new_rows[-1, 1])

#     # Append data to the chart.
#     chart.add_rows(new_rows)

#     # Pretend we're doing some computation that takes time.
#     time.sleep(0.1)

# status_text.text('Done!')
# st.balloons()



'# 添加记录'
if st.button('Say hello'):
	st.write('Why hello there')
	# Get some data.
	data = np.random.randn(10, 2)

	# Show the data as a chart.
	chart = st.line_chart(data)

	# Wait 1 second, so the change is clearer.
	time.sleep(1)

	# Grab some more data.
	data2 = [1,1,1,1,12,1,1,3,1,1]
	chart = st.line_chart(data2)
	# Append the new data to the existing chart.
	# chart.add_rows(data2)


'# 下载'
df = pd.read_csv("qk.csv")

@st.cache
def convert_df(df):
   return df.to_csv().encode('utf-8')


csv = convert_df(df)

st.download_button(
   "Press to Download",
   csv,
   "file.csv",
   "text/csv",
   key='download-csv'
)


'# 容器'
with st.expander("See explanation"):
     st.write("""
         The chart above shows some numbers I picked for you.
         I rolled actual dice for these, so they're *guaranteed* to
         be random.
     """)






from streamlit_echarts import st_echarts

options = {
    "xAxis": {
        "type": "category",
        "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    },
    "yAxis": {"type": "value"},
    "series": [
        {"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line"}
    ],
}
st_echarts(options=options)

'# 容器'
container = st.container()
container.write("This is inside the container")
st.write("This is outside the container")

# Now insert some more in the container
container.write("This is inside too")

'# 排列容器'
col1, col2, col3 ,col4 = st.columns(4)

with col1:
    st.header("A cat")
    st.header("A cat")
    st.header("A cat")

with col2:
    st.header("A dog")

with col3:
    st.header("An owl")

'# 标签容器'
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")

with tab2:
    st.header("A dog")

with tab3:
    st.header("An owl")




'# 表单'
with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")


form1 = st.form("my_fo1rm")
form1.slider("Inside the form")
st.slider("Outside the form")

# Now add a submit button to the form:
form1.form_submit_button("Submit")
