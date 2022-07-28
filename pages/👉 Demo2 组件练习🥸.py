import pandas as pd
import streamlit as st
import numpy as np
import time

st.set_page_config(
    page_title="Hoaii_Zone_Demo2",
    page_icon="🥸",
)

# 隐藏右边的菜单以及页脚
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

'### NO.1  心情指数😄'
if st.checkbox('开始测试“心情指数”'):
  with st.container():
    x = int(st.slider('请滑动'))
    if x>90:
      st.write('看来你的心情很不错！🌞')
    elif x>70:
      st.write('看来你的心情还可以，继续保持朝气吧！😌')
    elif x>50:
      st.write('要保持好心情呀！！💋')
    else :
      st.write('🤯🤯🤯亲，想开点')

'### NO.2  最爱美食🍜'
if st.checkbox('开始“挑美食”'):
  with st.container():
    options = st.multiselect(
         '选择你喜欢的美食吧！',
         ['汉堡', '烤肉', '火锅', '烧烤','烤鱼', '米线', '麻辣烫', '黄焖鸡'],
         ['烧烤'])
    # options 是 list，转成字符串
    mylist = options
    mystr2 = "、 ".join(mylist)   
    st.write('哈哈你选了', mystr2,'😂😂')
    if '烤肉' in mylist:
      st.write('我也超喜欢烤肉！')


'### NO.3  听音乐🎵'
if st.checkbox('开始“听音乐”'):
  with st.container():
    option = st.selectbox(
       '选择一首歌曲',
       ('阿飞的小蝴蝶', '夜曲','倔强','后来'))
    '👇以下歌曲是《',option,'》'
    if option=='阿飞的小蝴蝶':
      audio_file = open('./music/阿飞的小蝴蝶.wav', 'rb')
      audio_bytes = audio_file.read()
      st.audio(audio_bytes, format='audio/wav')
    elif  option=='夜曲':
      audio_file = open('./music/夜曲.wav', 'rb')
      audio_bytes = audio_file.read()
      st.audio(audio_bytes, format='audio/wav')
    elif  option=='倔强':
      audio_file = open('./music/倔强.wav', 'rb')
      audio_bytes = audio_file.read()
      st.audio(audio_bytes, format='audio/wav')
    elif  option=='后来':
      audio_file = open('./music/后来.wav', 'rb')
      audio_bytes = audio_file.read()
      st.audio(audio_bytes, format='audio/wav')

