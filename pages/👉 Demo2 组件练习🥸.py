import pandas as pd
import streamlit as st
import numpy as np
import time


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

'### NO.2  听音乐🎵'
if st.checkbox('开始“听音乐”'):
  with st.container():
    option = st.selectbox(
       '选择一首歌曲',
       ('阿飞的小蝴蝶', '夜曲','倔强','后来'))
    '👇以下歌曲是《',option,'》'
    if option=='阿飞的小蝴蝶':
      audio_file = open('./music/阿飞的小蝴蝶.mp3', 'rb')
      audio_bytes = audio_file.read()
      st.audio(audio_bytes, format='阿飞的小蝴蝶.mp3')
    elif  option=='夜曲':
      audio_file = open('./music/夜曲.mp3', 'rb')
      audio_bytes = audio_file.read()
      st.audio(audio_bytes, format='夜曲.mp3')
    elif  option=='倔强':
      audio_file = open('./music/倔强.mp3', 'rb')
      audio_bytes = audio_file.read()
      st.audio(audio_bytes, format='倔强.mp3')
    elif  option=='后来':
      audio_file = open('./music/后来.mp3', 'rb')
      audio_bytes = audio_file.read()
      st.audio(audio_bytes, format='后来.mp3')

