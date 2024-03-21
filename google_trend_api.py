from pytrends.request import TrendReq

pytrends = TrendReq(hl='ko', tz=540)  # hl=host language, tz=time zone

# setting
kw_list = ["애플파이", "에그타르트", "슈크림"]  # 단 게 땡기니까 달달구리구리한 것들로 키워드 리스트 생성
pytrends.build_payload(kw_list, cat=0,
                                timeframe='2024-01-01 2024-02-27',
                                geo='KR', gprop='')

data = pytrends.interest_over_time()

print(data)
