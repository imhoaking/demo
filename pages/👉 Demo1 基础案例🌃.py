import pandas as pd
import streamlit as st
import numpy as np
import time

st.set_page_config(
    page_title="Hoaii_Zone_Demo1",
    page_icon="🌃",
)


option = st.sidebar.selectbox(
    '选择一个有趣的小案例😯',
    ['none','BMI测试','满屏小气球','雪花'])
'### 你的选择是:', option


if option=="BMI测试":
	with st.container():
		number1 = st.number_input('👇输入你的身高/cm')
		'你的身高是',number1,'cm'
		number2 = st.number_input('👇输入你的体重/kg')
		'你的体重是', number2,'kg'
		if number1!=0:
			a=number2/number1/number1*10000
			'BMI是',str(a).split('.')[0] + '.' + str(a).split('.')[1][:2],'!'
elif option=="满屏小气球":
	with st.container():
		st.balloons()
		'# 🎈🎈🎈'
		st.sidebar.markdown('😍😍😍')
		st.sidebar.markdown('💗💗💗')
		if st.button('呜呜再演示一次🙆🏻‍♀️'):
			st.balloons()

elif option=="雪花":
	with st.container():
		st.snow()
		'# ❄️❄️❄️'
		st.sidebar.markdown('😍😍😍')
		st.sidebar.markdown('💗💗💗')
		if st.button('呜呜再演示一次🙆🏻‍♀️'):
		  	st.snow()



