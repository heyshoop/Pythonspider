#mongoDB数据可视化处理
from plistlib import Data

import pandas as pd
import plotly
import plotly.graph_objs
from matplotlib.axis import XAxis, YAxis
from bokeh.charts import Scatter
from bokeh.plotting import Figure
from openpyxl.chart.layout import Layout
from pymongo import MongoClient

#数据库设置
conn = MongoClient('127.0.0.1',27017)
db = conn.bilibili
biliavinfo = db.bili_avinfo

df = pd.DataFrame(list(biliavinfo.find({},{"_id":0})))
#df.rename(columns={0: '_id', 1: 'author', 2: 'author_name', 3: 'av', 4:'coin',5:'collect',6:'ctime',7:'danmu',8:'desc',9:'module',10:'mtime',11:'play',12:'share',13:'tid',14:'title',15:'url'}, inplace=True);
df.rename(columns={0: 'author_name', 1: 'play', 2: 'danmu', 3: 'share', 4:'coin',5:'title'}, inplace=True);
df = df.sort_values(['play'], ascending=[0])
#定义纵横坐标
trace1 = Scatter(x=df['play'],y=df['coin'],text=df['author_name']+":"+df['title'], mode='markers')
#定义纵横坐标显示
layout = Layout(
    title='哔哩哔哩近9月数据统计 ',
    xaxis=XAxis( type='log', title='播放量' ),
    yaxis=YAxis( title='投币数' ),
)
#生成页面
data = Data([trace1])
fig = Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='BiliBli.html')