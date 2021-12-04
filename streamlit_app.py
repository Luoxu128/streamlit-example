from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

import datetime as dt
#import pandas as pd
from mip import Model, xsum, BINARY, INTEGER, minimize, maximize

A = 213 #sleep_time_sum
m = 5  # X0 to X4, X0:day_one_sleep_time, X1:day_one_awake_time, X2:night_sleep_sum X3:night_one_awake_time X4:last_day_sleep
n = 6 #total blocks
feed_time = 5
awake_time_max = 22
awake_time_min = 12
night_sleep_max = 144
night_sleep_min = 96
period_min = 30
period_max = 60
result_x = {}
time_plan = {}
time_plan_note = {}

for j in range(1, n): #blocks in night
    # c1 = [n-j-1, 0, 1, 0]  # size of each item
    # c2 = [n-j-1, 0, -1, 0]
    # c3 = [1, 1, 0, 0]
    # c4 = [0, n-j, 0, j]
    # c5 = [0, 0, 1, 0]
    # c6 = [1, 0, 0, 0]
    # c7 = [0, 0, 0, 1]
    # c8 = [0, 1, 0, 0]
    # b = [A, 0, period_min, 288-A, night_sleep_min, night_sleep_max, 6, feed_time, awake_time_max, period_max]  # demand for each item
    # g = [1, 1, 0, 0]
    

    c1 = [n-j-2, 0, 1, 0, 1]  # size of each item
    c2 = [n-j-2, 0, -1, 0, 1]
    c3 = [1, 1, 0, 0, 0]
    c4 = [0, n-j, 0, j, 0]
    c5 = [0, 0, 1, 0, 0]
    c6 = [0, 0, 0, 0, 1]
    c7 = [0, 0, 0, 1, 0]
    c8 = [0, 1, 0, 0, 0]
    c9 = [1, 0, 0, 0, -1]
    c10 = [0, 1, 0, 0, 1]
    c11 = [1, 0, 0, 0, 0]
    c12 = [j, j, -1, 0, 0]
    b = [A, 0, period_min, 288-A, night_sleep_min, night_sleep_max, 8, feed_time, awake_time_max, period_max, 0, 24, awake_time_min, 24, 0]  # demand for each item
    g = [0, 0, 0, 0, 1]

    # creating the model
    model = Model()
    x = {(i): model.add_var(obj=0, var_type=INTEGER, name="x[%d]" % (i))
          for i in range(m)}
    #y = {j: model.add_var(obj=1, var_type=BINARY, name="y[%d]" % j)
    #     for j in range(n)}
    # y = {(i): model.add_var(obj=0, var_type=INTEGER, name="y[%d]" % (i))
    #       for i in range(m)}
    
    # constraints
    
    model.add_constr(xsum(c1[i] * x[i] for i in range(m)) == b[0]) #总睡眠时长限定
    model.add_constr(xsum(c2[i] * x[i] for i in range(m)) <= b[1]) #小睡总时长不长于夜间睡眠时长
    model.add_constr(xsum(c3[i] * x[i] for i in range(m)) >= b[2]) #吃玩睡模式下喂养间隔下限
    model.add_constr(xsum(c4[i] * x[i] for i in range(m)) == b[3]) #清醒时长限定
    model.add_constr(xsum(c5[i] * x[i] for i in range(m)) >= b[4]) #夜间睡眠时长下限
    model.add_constr(xsum(c5[i] * x[i] for i in range(m)) <= b[5]) #夜间睡眠时长上限
    model.add_constr(xsum(c6[i] * x[i] for i in range(m)) >= b[6]) #单次小睡时长下限
    model.add_constr(xsum(c7[i] * x[i] for i in range(m)) == b[7]) #夜间单次喂奶时长
    model.add_constr(xsum(c8[i] * x[i] for i in range(m)) <= b[8]) #白天最长清醒时长
    model.add_constr(xsum(c3[i] * x[i] for i in range(m)) <= b[9]) #吃玩睡模式下喂养间隔上限
    model.add_constr(xsum(c9[i] * x[i] for i in range(m)) >= b[10]) #最后一次小睡时间更短
    model.add_constr(xsum(c10[i] * x[i] for i in range(m)) >= b[11]) #最后一次喂奶间隔不短于2小时
    model.add_constr(xsum(c8[i] * x[i] for i in range(m)) >= b[12]) #白天最短清醒时长
    model.add_constr(xsum(c11[i] * x[i] for i in range(m)) <= b[13]) #单次小睡最长时长
    model.add_constr(xsum(c12[i] * x[i] for i in range(m)) <= b[14]) #控制夜间喂奶次数


    # for i in range(m):
    #     model.add_constr(x[i] +y[i] == b[3])
    # model.add_constr(xsum(c3[i] * y[i] for i in range(m)) <= b[4])
    # model.add_constr(xsum(c4[i] * y[i] for i in range(m)) <= b[5])
        #model.add_constr(xsum(c2[i] * x[i] for i in range(m)) <= b[1])
    
    #model.add_constr(xsum(c2[i] * x[i] for i in range(m)) >= 0)
    
    # additional constraints to reduce symmetry
    #for j in range(1, n):
    #    model.add_constr(y[j - 1] >= y[j])
    
    # model.objective = maximize(xsum(g[i] * x[i] for i in range(m)))
    model.objective = minimize(xsum(g[i] * x[i] for i in range(m)))
    # optimizing the model
    model.optimize()
    
    if model.objective_value:
        #printing the solution
        print('Objective value: {model.objective_value:.3}'.format(**locals()))
        #print(model.vars[3].x)
        print(model.objective_value)

        print('Solution: ', end='')
        print('j = ', j)
        print('          ', end='')
        for i in range(m):
            result_x[i] = x[i].x * 5
        for v in model.vars:
            if v.x > 1e-5:
                print('{v.name} = {v.x}'.format(**locals()))
                print('          ', end='')
        print('')
        count = 0
        time_plan[count] = count
        time_plan_note[count] = '一天开始，第一次奶'
        for i in range(n-2-j):
            count += 1
            time_plan[count] = time_plan[count-1] + result_x[1]
            time_plan_note[count] = '小睡开始'
            count += 1
            time_plan[count] = time_plan[count-1] + result_x[0]
            time_plan_note[count] = '小睡结束，喂奶'
        count += 1
        time_plan[count] = time_plan[count-1] + result_x[1]
        time_plan_note[count] = '小睡开始'
        count += 1
        time_plan[count] = time_plan[count-1] + result_x[4]
        time_plan_note[count] = '小睡结束，喂奶'
        count += 1
        time_plan[count] = time_plan[count-1] + result_x[1]
        time_plan_note[count] = '开始夜间睡眠'
        
        for i in range(j):
            count += 1
            time_plan[count] = time_plan[count-1] + result_x[0] + result_x[1]
            time_plan_note[count] = '夜醒喂奶'
            count += 1
            time_plan[count] = time_plan[count-1] + result_x[3]
            time_plan_note[count] = '夜醒喂奶结束，继续夜间睡眠'
        count += 1
        time_plan[count] = time_plan[count-1] + result_x[2] -(result_x[0] + result_x[1]) * j
        time_plan_note[count] = '夜间睡眠结束'
        day_begin = pd.to_timedelta('07:00:00')
        for i in range(len(time_plan)):
            st.markdown(day_begin + dt.timedelta(minutes=time_plan[i]), ':', time_plan_note[i] )
        print('')
    else:
        print('No result for j = ', j)

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
