from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import requests
import pandas as pd
import xmltodict
import json
# 위에서 20210119 부터 20210120 까지 데이터를 불러옵니다
key='jZ3%2FFq%2BXYo%2Be7JjXmVrkIBfYzl3XyQf6cSsyL5zUxo%2FBajw58wdOx31jgntb1MGCYtW0ieiVt5IcxCoBK2%2Bj6g%3D%3D'
url = f'http://apis.data.go.kr/B552895/openapi/service/OrgPriceAuctionService/getExactProdPriceList?serviceKey={key}&'
queryParams = urlencode({ quote_plus('pageNo') : 1, quote_plus('numOfRows') : 10,quote_plus('startCreateDt') : '20210119',
                        quote_plus('endCreateDt') : '20210120'})
url2 = url + queryParams
response = urlopen(url2)
# print(type(response)) # HTTPSresponse 
results = response.read().decode("utf-8")
# print(type(results))   # str
results_to_json = xmltodict.parse(results)
data = json.loads(json.dumps(results_to_json))
print(type(data))   # dic
print(data)   
# {'accDefRate': '1.5093139972', 'accExamCnt': '4269316', 'accExamCompCnt': '4092389', 'careCnt': '17897', 
# 'clearCnt': '42953', 'createDt': '2021-01-01 09:36:53.691',                              'deathCnt': '917', 'decideCnt': '61767', 
# 'examCnt': '176927', 'resutlNegCnt': '4030622', 'seq': '372', 
# 'stateDt': '20210101', 'stateTime': '00:00', 'updateDt': '2021-01-03 10:35:39.056'}
corona=data['response']['body']['items']['item']
#추가하고 싶은 리스트 생성
Date=[]
Cnt=[]
clear_cnt=[]
care_cnt=[]
death_cnt=[]
exam_cnt=[]     # examCnt   검사중
for i in corona:
    Date.append(i['stateDt'])  #'stateDt': '20200801'
    Cnt.append(i['decideCnt'])  # decideCnt': '14336'   누적확진자
    clear_cnt.append(i['clearCnt'])   # 13233           격리 해제환자
    care_cnt.append(i['careCnt'])     # 802             치료중 환자
    death_cnt.append(i['deathCnt'])    #301             사망자 수
df=pd.DataFrame([Date,Cnt,clear_cnt,care_cnt,death_cnt]).T
df.columns=['날짜','누적확진자','격리해제환자','치료중환자','사망자수'] 
df=df.sort_values(by='날짜', ascending=True)
# df.columns=['Date','acc_cnt','clear_cnt','care_cnt','death_cnt']
# df=df.sort_values(by='Date', ascending=True)
# df.head()
# df.info()
# df.describe()
# csv 파일 생성
df.to_csv('sample.csv')
# 메모장
df.to_csv('sample.txt')