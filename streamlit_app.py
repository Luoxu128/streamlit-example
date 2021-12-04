from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

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


    d=st.sidebar.date_input('Date',st.session_state.date_time.date())
    t=st.sidebar.time_input('Time',st.session_state.date_time.time())
    t=f'{t}'.split('.')[0]
    st.sidebar.write(f'The current date time is {d} {t}')

    col1,col2,col3 = st.columns(3)
    # bootstrap collapse example
    with col1:
       components.html(
           """
           <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
           <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
            <div id="accordion">
              <div class="card">
                <div class="card-header" id="headingOne">
                  <hclass="mb-0">
                    <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                    第一个折叠菜单
                    </button>
                  </h5>
                </div>
                <div id="collapseOne" class="collapse in" aria-labelledby="headingOne" data-parent="#accordion">
                  <div class="card-body">
                    人的一生应当这样度过：当回忆往事的时候，他不会因为虚度年华而悔恨，也不会因为碌碌无为而羞愧；在临死的时候，他能够说：我的整个生命和全部精力，都已经献给了世界上最壮丽的事业——为人类的解放而斗争。
                 </div>
               </div>
             </div>
             <div class="card">
               <div class="card-header" id="headingTwo">
                 <hclass="mb-0">
                   <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                  第二个折叠菜单
                  </button>
                </h5>
               </div>
               <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
                 <div class="card-body" style="background-image: linear-gradient(to right,#ff4d88, white);color:red;">
                   带着感恩的心启程，学会爱，爱父母，爱自己，爱朋友，爱他人。
                 </div>
               </div>
             </div>
          </div>
          """,
          height=600,
      )
    with col2:
       components.html(
           """
           <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
           <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
           <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
          <div id="accordion">
            <div class="card">
              <div class="card-header" id="headingOne">
                <hclass="mb-0">
                  <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                  第三个折叠菜单
                   </button>
                 </h5>
               </div>
               <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
                <div class="card-body">
                  Where there is life， there is hope!
                </div>
              </div>
            </div>
            <div class="card">
               <div class="card-header" id="headingTwo">
                 <hclass="mb-0">
                   <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                   第四个折叠菜单
                  </button>
                </h5>
              </div>
              <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
                <div class="card-body">
                  业精于勤，荒于嬉；行成于思，毁于随。
                </div>
               </div>
             </div>
           </div>
          """,
          height=600,
      )
    with col3:
      components.html(
          """
          <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
          <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
           <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
           <div id="accordion">
            <div class="card">
              <div class="card-header" id="headingOne">
                <hclass="mb-0">
                  <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne"
                   style="background-image: linear-gradient(to right,#00ff00, white);color:red;">
                  第五个折叠菜单
                  </button>
                </h5>
              </div>
               <div id="collapseOne" class="collapse in" aria-labelledby="headingOne" data-parent="#accordion">
                 <div class="card-body" style="background-image: linear-gradient(to right,#00ccff, white);color:red;">
                   我不去想是否能够成功，既然选择了远方，便只顾风雨兼程！
                 </div>
               </div>
             </div>
    
             <div class="card">
               <div class="card-header" id="headingTwo">
                 <hclass="mb-0">
                   <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
                   第六个折叠菜单
                   </button>
                 </h5>
               </div>
               <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
                 <div class="card-body">
                   没有创造的生活不能算生活，只能算活着。
                 </div>
               </div>
             </div>
           </div>
           """,
           height=600,
       )

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
