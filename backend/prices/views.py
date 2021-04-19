from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


from .serializers import PriceListSerializer
from .models import MainPrice



from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import requests
import pandas as pd
import xmltodict
import json
from datetime import datetime



# 예회처리
# from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent.parent

import os, json
# from django.core.exceptions import ImproperlyConfigured # 예외처리 할 부분 불어오기
# secret_file = os.path.join(BASE_DIR, 'secrets.json')
# # json 변수 읽어오기
# with open(secret_file) as f:
#     secrets = json.loads(f.read())
# def get_secret(setting, secrets=secrets):
#     try:
#         print("check:", secrets[setting])
#         return secrets[setting]
#     except KeyError:
#         error_msg = "Set the {} environment variable".format(setting)
#         raise ImproperlyConfigured

# SECRET_KEY = get_secret("SECRET_KEY")

# Create your views here.
from rest_framework.decorators import authentication_classes, permission_classes
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_main_price(request):
    base_price = MainPrice.objects.all()
    serializer = PriceListSerializer(base_price, many=True)
    print(serializer.data)
    return Response(serializer.data)

def add_main_price(request):
    # 조회
    # queryset = MainPrice.objects.all()
    # for i in queryset:
    #     # 삭제
    #     print(1)
    #     if i.date == '20210415':
    #         print(2)
    #         delete_data = MainPrice.objects.get(id=i.id)
    #         delete_data.delete()
    #         print(f'{i.id}가 삭제됐습니다.')

    # 삭제
    queryset = MainPrice.objects.all()
    if queryset:
        queryset.delete()
    #생성
    yesterday_date = str(int(datetime.today().strftime("%Y%m%d"))-1)
    data_load = [['배추', '1001', '그물망', ['특', '상']], 
             ['풋고추', '1205', '상자', ['특', '상']], 
             ['양파', '1201', '그물망', ['특', '상']], 
             ['시금치', '1008', '단', ['특', '상']], 
             ['애호박', '0902', '상자', ['특', '상']],
             ['깻잎', '1011', '상자', ['특', '상']]]
    # SECRET_KEY = get_secret("SECRET_KEY")
    for each_data in data_load:
        key="jZ3%2FFq%2BXYo%2Be7JjXmVrkIBfYzl3XyQf6cSsyL5zUxo%2FBajw58wdOx31jgntb1MGCYtW0ieiVt5IcxCoBK2%2Bj6g%3D%3D"
        url = f'http://apis.data.go.kr/B552895/openapi/service/OrgPriceAuctionService/getExactProdPriceList?serviceKey={key}&'
        queryParams = urlencode({ quote_plus('numOfRows') : 2000000,
                                quote_plus('pageNo') : 1,
                                quote_plus('delngDe') : str(int(datetime.today().strftime("%Y%m%d"))-1),   # 일요일은 안됨
                                quote_plus('prdlstCd') : each_data[1],
                                #  quote_plus('stdSpciesNewCode') : 'stdSpciesNewCode',
                                quote_plus('whsalNm') : '서울가락도매시장'
                                })
        url2 = url + queryParams
        response = urlopen(url2)
        # print(type(response)) # HTTPSresponse 
        results = response.read().decode("utf-8")
        results_to_json = xmltodict.parse(results)
        data = json.loads(json.dumps(results_to_json))

        data_f=data['response']['body']['items']['item']

        price_sum = 0
        cnt = 0
        plot_data = []
        for i in data_f:
            a = int(i['sbidPric'])//float(i['delngPrut']) # 가격 // 거래단량
            # if a > 5000:
            #   continue

            if not i['stdFrmlcNewNm'] == each_data[2]:
                continue
            if not i['stdQlityNewNm'] in each_data[3]:
                continue
            price_sum += a
            plot_data.append(a)
            cnt+=1
        price_data = price_sum//len(data_f)
        


        volumn_sum = 0
        cnt = 0
        for i in data_f:
            a = int(i['delngQy'])*float(i['delngPrut']) # 거래량 * 거래단량
            # if a > 5000:
            #   continue
            if not i['stdFrmlcNewNm'] == each_data[2]:
                continue    
            if not i['stdQlityNewNm'] in each_data[3]:
                continue
            volumn_sum += a
            cnt+=1
        volumn = volumn_sum


        main_data = MainPrice(date=str(int(datetime.today().strftime("%Y%m%d"))-1), 
                                data_name=each_data[0], 
                                price_data=price_data, 
                                volumn=volumn)
        main_data.save()
    
    # main_data = MainPrice(date='20210415', data_name='배추e', price_data='7231', volumn='2.3')
    # main_data.save()
    return HttpResponse(status=201)

