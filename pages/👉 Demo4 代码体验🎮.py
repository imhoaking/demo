
import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(
    page_title="Hoaii_Zone_Demo4",
    page_icon="🎮",
)

option1 = st.sidebar.checkbox('Eetric状态',0,1)
if option1:
  with st.expander("Etric状态"):
    st.metric(label="状态", value="正能量", delta="120% 😄",help='哈哈没啥')


option2 = st.sidebar.checkbox('输出json',0,1)
if option2:
  with st.expander("输出json"):
    st.json({
    	'foo': 'bar',
    	'baz': 'boz',
    	'stuff': [
    		'stuff 1',
    		'stuff 2',
    		'stuff 3',
    	    'stuff 5',
       	 ],
    	})


option3 = st.sidebar.checkbox('固定数',0,1)
if option3:
  with st.expander("固定数"):
    st.write("Here's our first attempt at using data to create a table:")
    st.write(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }))


option4 = st.sidebar.checkbox('随机数',0,1)
if option4:
  with st.expander("随机数"):
    df = pd.DataFrame(
    	np.random.randn(10, 10),
    	columns=('col %d' % i for i in range(10)))
    st.dataframe(df,600,100)  # Same as st.write(df)
    # st.dataframe(df.style.highlight_min(axis=0))
    st.table(df)

option5 = st.sidebar.checkbox('代码块高亮',0,1)
if option5:
  with st.expander("代码块高亮"):
    code = 'import * from time'
    st.code(code, language='python')

# def load_data(nrows):
#     # data = pd.read_csv(DATA_URL, nrows=nrows)
#     data = pd.read_csv('/Users/09987q/Downloads/qk.csv', nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     # data[0,1,2] = pd.to_datetime(data[0,1,2])
#     return data[0,1,2]

 # st.dataframe(data)


option6 = st.sidebar.checkbox('进度条',0,1)
if option6:
  with st.expander("进度条"):
    # Add a placeholder

    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
      # Update the progress bar with each iteration.
      latest_iteration.text(f'完成了 {i+1} % ')
      bar.progress(i + 1)
      time.sleep(0.1)
    ' OK 完成✅ '


