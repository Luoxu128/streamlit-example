from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

import datetime
import time

def main():
    st.set_page_config(page_title="快乐母乳喂养",page_icon=":rainbow:",layout="centered",initial_sidebar_state="auto")
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
        st.session_state.page = 0

    # d=st.sidebar.date_input('Date',st.session_state.date_time.date())
    # t=st.sidebar.time_input('Time',st.session_state.date_time.time())
    t=f'{st.session_state.date_time.time()}'.split('.')[0]
    # st.sidebar.write(f'The current date time is {d} {t}')

    st.markdown(""" <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style> """, unsafe_allow_html=True)
        
    padding = 2
    st.markdown(f""" <style>
        .reportview-container .main .block-container{{
            padding-top: {padding}rem;
            padding-right: {padding}rem;
            padding-left: {padding}rem;
            padding-bottom: {padding}rem;
        }} </style> """, unsafe_allow_html=True)

    st.markdown(
        '<meta name="viewport" content="width=device-width, initial-scale=1" />', 
        unsafe_allow_html=True,
        )    

    st.markdown(
        '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">',
        unsafe_allow_html=True,
        )


    #横向菜单方案一
    test_html = f"""
        <html>
                <div id="test_div">
                    <p>我是小P</p>
                    <li class="nav-item"><a class="nav-link">我是li1</a></li>
                    <li class="nav-item">我是li2</li>
                    <li class="nav-item">我是li3</li>
                    <h3>我是h3，说h1太大了，让我来充数</h3>
                </div>
                
        </html>    """

    st.markdown(test_html, unsafe_allow_html=True)
    
    query_params = st.experimental_get_query_params()
    tabs = ["首页", "图片", "音乐", "视频"]
    if "tab" in query_params:
        active_tab = query_params["tab"][0]
    else:
        active_tab = "首页"
    
    if active_tab not in tabs:
        st.experimental_set_query_params(tab="首页")
        active_tab = "首页"
    
    li_items = "".join(
        f"""
        <li class="nav-item">
            <a class="nav-link{' active' if t==active_tab else ''}" href="/?tab={t}">{t}</a>
        </li>
        """
        for t in tabs
    )
    tabs_html = f"""
        <ul class="nav nav-tabs">
        {li_items}
        </ul>
    """
    
    st.markdown(tabs_html, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
    if active_tab == "首页":
        st.info("中国人自己的空间站时代来临了")
    
    elif active_tab == "图片":
        st.info("请欣赏雪山景色")
    
    elif active_tab == "音乐":
        st.info('点击播放按钮播放mp3音乐')
    
    elif active_tab == "视频":
        st.info('点击播放按钮播放mp4视频')
    
    else:
        st.error("出错了。")
    #横向菜单方案一结束    
    
    col1, col2, col3 = st.columns(3)
    #left, col1, left_medium, col2, right_medium, col3, right = st.columns([0.1,1,0.1,1,0.1,1,0.1])
    # with left:
    #      st.empty()
    with col1:
        page1 = st.button("视频")
    # with left_medium:
    #     st.empty()
    with col2:
        page2 = st.button("图片")
    # with right_medium:
    #     st.empty()
    with col3:
        page3 = st.button("音乐")
    # with right:
    #     st.empty()
        
    if page1:
        st.session_state.page = 1
    if page2:
        st.session_state.page = 2
    if page3:
        st.session_state.page = 3
    if st.session_state.page == 1:
        st.info('测试菜单项')

        html_string = '''
        <h1>HTML string in RED</h1>
        
        <script language="javascript">
          document.querySelector("h1").style.color = "red";
          console.log("Streamlit runs JavaScript");
          alert("Streamlit runs JavaScript");
        </script>
        '''
        components.html(html_string)  # JavaScript works

        st.markdown(html_string, unsafe_allow_html=True)  # JavaScript doesn't work
    
        form = st.form(key='my-form')
        name = form.text_input('请输入您的名字')
        submit = form.form_submit_button('提交')
        st.write('选择提交按钮后，你的名字将会显示在下方')
        if submit:
            st.write(f'欢迎 {name}回来')
    
        d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
        st.write('Your birthday is:', d)
        
        #t = st.time_input('Set an alarm for', datetime.time(8, 45))
        st.write('Alarm is set for', t)
    
    if st.session_state.page == 2:
        st.info("请欣赏雪山景色")
        #转换时间为时间戳，加8小时时差，再转换为时间元组
        ep = datetime.datetime(1970, 1, 1)
        dt = datetime.datetime.now()
        dt = (dt - ep )/datetime.timedelta(seconds=1) + 3600*8
        localtime = time.gmtime(dt)
        #localtime = time.localtime(time.time())
        #print "本地时间为 :", localtime
        #localtime = time.asctime(time.localtime(time.time()))
        hour = localtime.tm_hour
        minute = localtime.tm_min
        hour = st.slider('hour', 0, 23, hour)
        minute = st.slider('minute', 0, 59, minute)
        st.write('Time is', hour, ':', minute)
        st.write(f'当前时间为 {t}')
        
        tic1 = time.perf_counter()
        #time.sleep(2)#(此行可以换成需要计时的模块)
        toc1 = time.perf_counter()
        shijian1 = int(toc1-tic1)
        st.write(shijian1)
        
        if st.button('Say hello'):
             st.write('Why hello there')
        else:
             st.write('Goodbye')


    if st.session_state.page == 3:
        st.info('点击播放按钮播放mp3音乐')
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
    

    # st.markdown("""
    # <style>
    # div.stButton > button:first-child {
    #     color:blue;background-color: #00ff99;a:hover{color:#00ffff;}
    # }
    # </style>""", unsafe_allow_html=True)

    
    """
    # Welcome to Streamlit!
    
    Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:
    
    If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
    forums](https://discuss.streamlit.io).
    
    In the meantime, below is an example of what you can do with just a few lines of code:
    """
    
    

if __name__ == '__main__':
    main()
