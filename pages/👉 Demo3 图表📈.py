import pandas as pd
import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt
from bokeh.plotting import figure
import graphviz

st.set_page_config(
    page_title="Hoaii_Zone_Demo3",
    page_icon="📈",
)

# 隐藏右边的菜单以及页脚
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# '# 显示pyplot图 bug'
# arr = np.random.normal(1, 1, size=100)
# plt.hist(arr, bins=20)
# st.pyplot(plt.hist(arr, bins=20))

# '# 显示plotly图'
# # Add histogram data
# x1 = np.random.randn(20) +10
# x2 = np.random.randn(20)
# x3 = np.random.randn(20) -10
# # Group data together
# hist_data = [x1, x2, x3]
# group_labels = ['学生1', '学生2', '学生3']

# # Create distplot with custom bin_size
# fig = ff.create_distplot(
#   hist_data, group_labels, bin_size=[8, 9, 3])

# # Plot!
# st.plotly_chart(fig)

st.sidebar.markdown('### 「 疯狂图表🤯 」')


'### 显示折线图、区域图、棒状图'
option1=st.checkbox('👈点击查看1')
if option1:
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])
    '#### 折线图'
    st.line_chart(chart_data)
    '#### 区域图'
    st.area_chart(chart_data)
    '#### 棒状图'
    st.bar_chart(chart_data)


'### 显示bokeh图'
option2=st.checkbox('👈点击查看2')
if option2:
	x = [1, 2, 3, 4, 5]
	y = [60, 57, 66, 55, 71]
	p = figure(
	  title='boken小例子',
	  x_axis_label='x',
	  y_axis_label='y')

	p.line(x, y, legend='somemm', line_width=5)
	st.bokeh_chart(p)


'### 显示Graphviz图'
option3=st.checkbox('👈点击查看3')
if option3:
# Create a graphlib graph object
	graph = graphviz.Digraph()
	graph.edge('run', 'intr')
	graph.edge('intr', 'runbl')
	graph.edge('runbl', 'run')
	graph.edge('run', 'kernel')
	graph.edge('kernel', 'zombie')
	graph.edge('kernel', 'sleep')
	graph.edge('kernel', 'runmem')
	graph.edge('sleep', 'swap')
	graph.edge('swap', 'runswap')
	graph.edge('runswap', 'new')
	graph.edge('runswap', 'runmem')
	graph.edge('new', 'runmem')
	graph.edge('sleep', 'runmem')

	st.graphviz_chart(graph)


# '# 显示图片'
# image = Image.open('./pics/pic1.JPG')
# st.image(image, caption='sea hah',use_column_width=True)

# if st.button('Say hello'):
#   st.write('Why hello there')
# else:
#   st.write('Goodbye')



