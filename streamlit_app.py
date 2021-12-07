from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import pymysql
import bcrypt

import datetime
import time

def create_usertable():
     #c.execute('CREATE TABLE IF NOT EXISTS userstable(ID INTEGER auto_increment not null primary key, username TEXT, password TEXT)')
     c.callproc('create_userstable')
 
def add_userdata(username, password):
 
     hashAndSalt = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
     result = 0
     r1 = c.callproc('user_check',args=(username, result))
     r2 = c.execute("select @_user_check_1")
     result = c.fetchall()
     result = result[0][0]

     if result:
         st.warning("用户名已存在，请更换一个新的用户名。")
     else:
         #c.execute('INSERT INTO userstable(username,password) VALUES(%s,%s)',(username,password))
         #con.commit()
         result_1 = 0
         r_1 = c.callproc('add_user',args=(username, hashAndSalt, result_1))
         con.commit()
         r_2 = c.execute("select @_add_user_2")
         result_1 = c.fetchall()
         result_1 = result_1[0][0]
         if result_1:
             st.success("恭喜，您已成功注册。{}".format(result_1))
             st.info("请在左侧选择“登录”选项进行登录。")
         else:
             st.warning("出现未知错误，未注册成功，请重试或联系管理员！")
 
def login_user(username,password):
     #if c.execute('SELECT username FROM userstable WHERE username = %s',(username)):
         #c.execute('SELECT * FROM userstable WHERE username = %s AND password = %s',(username,password))
         #user_id = c.var(log_result.INTEGER)#存储过程返回值
         #c.callproc('login_user',[username,password,user_id])
         #c.execute('call login_user(%s,%s,@log_result)',(username,password))
         #data, result = callpro_sql('login_user', [1], username,password)
         result = 0
         u_id = 0
         hashAndSalt = ''
         r1 = c.callproc('login_user',args=(username,password,result))
         r2 = c.execute("select @_login_user_1, @_login_user_2")
         result = c.fetchall()
         u_id = result[0][1]
         if u_id > 0:
             result = result[0][0]
             result = result.encode('utf8')
             valid = bcrypt.checkpw(password.encode(), result)
             if valid:
                 return u_id
             else:
                 st.warning("用户名或密码错误，请从新输入或联系管理员！" )
         else:
             st.warning("用户名或密码错误，请从新输入或联系管理员！" )
             
         #return data
     #else:
         #st.warning("用户名不存在，请先选择注册按钮完成注册。", )

def main():
    # st.set_page_config(page_title="快乐母乳喂养",page_icon=":rainbow:",layout="wide",initial_sidebar_state="auto")
    st.set_page_config(page_title="快乐母乳喂养",page_icon=":rainbow:",initial_sidebar_state="auto")
    #st.title('快乐母乳喂养:heart:')
    #st.markdown('<br>',unsafe_allow_html=True)
    #st.markdown('<br>',unsafe_allow_html=True)

    if 'first_visit' not in st.session_state:
        st.session_state.first_visit=True
    else:
        st.session_state.first_visit=False
    # 初始化全局配置
    
    if st.session_state.first_visit:
        # 在这里可以定义任意多个全局变量，方便程序进行调用
        st.session_state.date_time = datetime.datetime.now() + datetime.timedelta(hours=8) # Streamlit Cloud的时区是UTC，加8小时即北京时间
        st.session_state.page = 0
        con = pymysql.connect(host="sql.j104.vhostgo.com", user="promiseway", password="52582939", database="promiseway", charset="utf8")
        c = con.cursor()
        
    # d=st.sidebar.date_input('Date',st.session_state.date_time.date())
    # t=st.sidebar.time_input('Time',st.session_state.date_time.time())
    t=f'{st.session_state.date_time.time()}'.split('.')[0]
    # st.sidebar.write(f'The current date time is {d} {t}')
    
    #隐藏菜单按钮    
    st.markdown(""" <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style> """, unsafe_allow_html=True)
        
    #调整页面边距
    padding = 1
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

# =============================================================================
# 登录管理开始
# =============================================================================
     menu = ["首页","登录","注册", "注销"]
 
     if 'count' not in st.session_state:
         st.session_state.count = 0
 
     choice = st.sidebar.selectbox("选项",menu)
     st.sidebar.markdown(
     """
     <style>
     [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
         width: 250px;
     }
     [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
         width: 250px;
         margin-left: -250px;
     }
     </style>
     """,
     unsafe_allow_html=True,)
 
     if choice =="首页":
         st.subheader("首页")
         st.markdown('''Streamlit文档的地址是：https://docs.streamlit.io/''')
         c1, c2 = st.columns(2)
         with c1:
             st.success('''Streamlit中文公众号名称是：Streamlit, 公众号二维码如下''')
             st.image("img1.png")
         with c2:
             st.success('''Streamlit中文交流群二维码如下''')
             st.image("img2.png")
 
     elif choice =="登录":
         st.sidebar.subheader("登录区域")
 
         username = st.sidebar.text_input("用户名")
         password = st.sidebar.text_input("密码",type = "password")
         if st.sidebar.checkbox("开始登录"):
             create_usertable()
             logged_user = login_user(username,password)
             if logged_user:
 
                 st.session_state.count += 1
 
                 if st.session_state.count >= 1:
 
                     st.sidebar.success("您已登录成功，您的用户名是 {}".format(username))
 
                     st.title("成功登录后可以看到的内容{}".format(logged_user))
                     st.balloons()
                     st.markdown(logged_user)
                     c1, c2 = st.columns(2)
                     with c1:
                         st.success('''Streamlit中文公众号名称是：Streamlit, 公众号二维码如下''')
                         st.image("img1.png")
                     with c2:
                         st.success('''Streamlit中文交流群二维码如下''')
                         st.image("img2.png")
 
             else:
                 st.sidebar.warning('用户名或密码错误，请重新输入！')
                 #st.sidebar.warning(data)
 
     elif choice =="注册":
        st.subheader("注册")
        new_user = st.sidebar.text_input("用户名")
        new_password = st.sidebar.text_input("密码",type = "password")

        if st.sidebar.button("注册"):
            create_usertable()
            add_userdata(new_user,new_password)

     elif choice =="注销":
        st.session_state.count = 0
        if st.session_state.count == 0:
            st.info("您已成功注销，如果需要，请选择左侧的登录按钮继续登录。")

# =============================================================================
# 登录管理结束
# =============================================================================
    
    col1, col2, col3 = st.columns(3)
    #left, col1, left_medium, col2, right_medium, col3, right = st.columns([0.1,1,0.1,1,0.1,1,0.1])
    # with left:
    #      st.empty()
    with col1:
        page1 = col1.button("视频")
    # with left_medium:
    #     st.empty()
    with col2:
        page2 = col2.button("图片")
    # with right_medium:
    #     st.empty()
    with col3:
        page3 = col3.button("音乐")
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
