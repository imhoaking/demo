import pandas as pd
import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt
# import plotly.figure_factory as ff
from bokeh.plotting import figure
import graphviz
# from PIL import Image




'# 显示pyplot图 bug'
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

'# 显示bokeh图'
x = [1, 2, 3, 4, 5]
y = [60, 71, 50, 42, 57]
p = figure(
  title='boken小例子',
  x_axis_label='x',
  y_axis_label='y')

p.line(x, y, legend='somemm', line_width=7)
st.bokeh_chart(p)


'# 显示Graphviz图'
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

'# 显示多选框'
options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow'])

st.write('You selected:', options)

st.metric(label="Temperature", value="体重的的", delta="-1.2 °F",help='Njjone')
