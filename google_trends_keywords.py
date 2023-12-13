from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

#!pip install pytrends  패키지 설치
#!pip install plotly  패키지 설치


# hl = host language, tz = timezone
pytrends = TrendReq(hl='ko', tz=540)    #hl 언어(한국어), tz 한국시간기준


#시간 타임존은 https://forbrains.co.uk/international_tools/earth_timezones?ref=hackernoon.com 여기에서 찾으면 된다.

kw_list = ["삼성 갤럭시 워치", "애플워치"]  #kw_list : 데이터를 가져올 키워드 목록 (한 번에 5 개 키워드로 제한)

pytrends.build_payload(kw_list, cat=0, timeframe='2023-12-01 2023-12-03', geo='KR') #geo : 지리적 위치. #timeframe : 관심있는 시간 프레임.
data = pytrends.interest_over_time()
data = data.reset_index()

print(data.head(20))  # Top 20 개 데이터만 보기

fig = px.line(data, x="date", y=kw_list, title='구글 검색 트렌드')
fig.show()

# 그래프로 트렌드 보기

#plt.figure()
#plt.plot(df.index, df.갤럭시워치4, label='ratio')
#plt.plot(df.index, df.chicken, label='ratio')
#plt.plot(df.index,df.space, label='ratio')
#plt.legend(['갤럭시워치4'])