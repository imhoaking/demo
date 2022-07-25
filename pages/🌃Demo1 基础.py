import pandas as pd
import streamlit as st
import numpy as np
import time


'### 这里是滑块'
x = st.slider('身高')

st.write(x, 'squared is', x * x)


'### 这里是st.write'
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
# pandas只能是数

'### 这里是pd.DataFrame'
df = pd.DataFrame(
	np.random.randn(50, 20),
	columns=('col %d' % i for i in range(20)))
st.dataframe(df,400,200)  # Same as st.write(df)
st.dataframe(df.style.highlight_min(axis=0))
st.table(df)


# def load_data(nrows):
#     # data = pd.read_csv(DATA_URL, nrows=nrows)
#     data = pd.read_csv('/Users/09987q/Downloads/qk.csv', nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     # data[0,1,2] = pd.to_datetime(data[0,1,2])
#     return data[0,1,2]

 # st.dataframe(data)

'### 这里是复选框'
if st.checkbox('变！显示图标'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])
    '折线图'
    st.line_chart(chart_data)
    '区域图'
    st.area_chart(chart_data)
    '棒状图'
    st.bar_chart(chart_data)

'### 这里是列表选择框'
option = st.selectbox(
    'Which number do you like best?',
    [88,123,99,66])

'You selected:  😄', option



'### 这里是复选框（侧栏）'
option = st.sidebar.checkbox('复选框要不要选',0,1)
if option:
	'复选框，（你选啦！）'
else :
	'复选框,（怎么没选！）'

'### 代码块高亮'
code = 'import * from time'
st.code(code, language='python')


'### 输出json'
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



'### 进度条'
'Starting a long computation...'
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)
'...and now we\'re done!'