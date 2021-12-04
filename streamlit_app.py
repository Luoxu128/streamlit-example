from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

import datetime
import time
#import streamlit as st

def main():
    st.set_page_config(page_title="快乐母乳喂养",page_icon=":rainbow:",layout="wide",initial_sidebar_state="auto")
    st.title('快乐母乳喂养:heart:')
    st.markdown('<br>',unsafe_allow_html=True)
    st.markdown('<br>',unsafe_allow_html=True)

    if 'first_visit' not in st.session_state:
        st.session_state.first_visit=True
    else:
        st.session_state.first_visit=False
    # 初始化全局配置
    if st.session_state.first_visit:
        # 在这里可以定义任意多个全局变量，方便程序进行调用
        st.session_state.date_time = datetime.datetime.now() + datetime.timedelta(hours=8) # Streamlit Cloud的时区是UTC，加8小时即北京时间


    form = st.form(key='my-form')
    name = form.text_input('请输入您的名字')
    submit = form.form_submit_button('提交')
    st.write('选择提交按钮后，你的名字将会显示在下方')
    if submit:
        st.write(f'欢迎 {name}回来')
    
    d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
    st.write('Your birthday is:', d)
    
    t = st.time_input('Set an alarm for', datetime.time(8, 45))
    st.write('Alarm is set for', t)
    
    #import streamlit as st
    
    localtime = time.localtime(time.time())
    #print "本地时间为 :", localtime
    #localtime = time.asctime(time.localtime(time.time()))
    hour = localtime.tm_hour
    minute = localtime.tm_min
    hour = st.slider('hour', 0, 23, hour)
    minute = st.slider('minute', 0, 59, minute)
    st.write('Time is', hour, ':', minute)
    
    tic1 = time.perf_counter()
    #time.sleep(2)#(此行可以换成需要计时的模块)
    toc1 = time.perf_counter()
    shijian1 = int(toc1-tic1)
    st.write(shijian1)
    
    if st.button('Say hello'):
         st.write('Why hello there')
    else:
         st.write('Goodbye')
    
    
    """
    # Welcome to Streamlit!
    
    Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
    
    If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
    forums](https://discuss.streamlit.io).
    
    In the meantime, below is an example of what you can do with just a few lines of code:
    """
    
    
    with st.echo(code_location='below'):
        total_points = st.slider("Number of points in spiral", 1, 5000, 3000)
        num_turns = st.slider("Number of turns in spiral", 1, 100, 9)
    
        Point = namedtuple('Point', 'x y')
        data = []
    
        points_per_turn = total_points / num_turns
    
        for curr_point_num in range(total_points):
            curr_turn, i = divmod(curr_point_num, points_per_turn)
            angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
            radius = curr_point_num / total_points
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            data.append(Point(x, y))
    
        st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
            .mark_circle(color='#0068c9', opacity=0.5)
            .encode(x='x:Q', y='y:Q'))

if __name__ == '__main__':
    main()
