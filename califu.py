import requests
import json
import os
from bs4 import BeautifulSoup
from datetime import datetime
import time


# ss = requests.session()

# url = 'https://online.carrefour.com.tw/CarrefourECHome/GetSalesPromotion'
# s = '''User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'''
# headers = {r.split(': ')[0].replace(':', ''): r.split(': ')[1] for r in s.split('\n')}
# data = {"langId": 1}
# res = ss.post(url, headers=headers, data=data)
# json_data = res.json()
# for j in json_data["content"]["PromotionModelList"]:
#     for jp in j["ProductModelList"]:
#         print(jp["Id"])
#         print(jp["BrandName"])
#         print(jp["Name"])
#         print(jp["Price"])
#         print(jp["SpecialPrice"])

ss = requests.session()
api_list_dict = {}
for i in range(1, 3500):
    url = 'https://online.carrefour.com.tw/ProductShowcase/Catalog/CategoryJson?categoryId=1&orderBy=21&pageIndex=2&pageSize=20&isLoadThree=false'
    s = '''User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'''
    headers = {r.split(': ')[0].replace(':', ''): r.split(': ')[1] for r in s.split('\n')}
    res = ss.post(url, headers=headers)
    try:
        json_data = res.json()
        print(int(json_data['content']["Count"])//1000)
        print(i)
        print(json_data["content"]["ProductListModel"][0]["BrandName"])
        print(len(json_data["content"]["ProductListModel"]))
        time.sleep(5)
    except Exception as e:
        print(e)




# ss = requests.session()

# url = 'https://online.carrefour.com.tw/ProductShowcase/Catalog/GetMenuJson'
# s = '''User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'''
# headers = {r.split(': ')[0].replace(':', ''): r.split(': ')[1] for r in s.split('\n')}
# data = {"langId": 1}
# res = ss.post(url, headers=headers, data=data)
# json_data = res.json()
# for j in json_data["content"]:
#     print(j["Name"])
#     for jp in j["Manufacturers"]:
#         print(jp["Name"])

# ss = requests.session()

# url = 'https://online.carrefour.com.tw/ProductShowcase/Commodities/SearchLazy'
# s = '''User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'''
# headers = {r.split(': ')[0].replace(':', ''): r.split(': ')[1] for r in s.split('\n')}
# data = {"key": "%E5%8F%B0%E7%81%A3%E8%B1%AC"}
# res = ss.post(url, headers=headers, data=data)
# url = 'https://online.carrefour.com.tw/CarrefourECProduct/QueryRecentSearchKeywords'
# s = '''User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'''
# headers = {r.split(': ')[0].replace(':', ''): r.split(': ')[1] for r in s.split('\n')}
# res = ss.post(url, headers=headers)
# print(ss.cookies)
# print(res.json())

