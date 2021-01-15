from carrefour.items import CarrefourItem
import scrapy
import time
import json
from datetime import datetime
import requests

class CarrefourSpider(scrapy.Spider):
    name:str = "carrefour"
    NowDateTime = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S")         
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    }      
    def start_requests(self):        
        for sid in range(1, 3500):
            url = f'https://online.carrefour.com.tw/ProductShowcase/Catalog/CategoryJson?categoryId={sid}&orderBy=21&pageIndex=2&pageSize=1000&isLoadThree=false'
            res = requests.post(url, headers=self.headers)
            json_data = res.json()
            page = int(json_data['content']["Count"])//1000 + 1
            for i in range(page):
                url = f'https://online.carrefour.com.tw/ProductShowcase/Catalog/CategoryJson?categoryId={sid}&orderBy=21&pageIndex={i+1}&pageSize=1000&isLoadThree=false'
                yield scrapy.Request(url=url, callback=self.parse, method="POST")#, meta={"proxy": list(ScyllaProxies().random_proxy().values())[0]})

    def parse(self, response):           
        json_data = response.json()        
        item = CarrefourItem()
        domain = "https://online.carrefour.com.tw/tw"
        for j in json_data["content"]["ProductListModel"]:
            item['product_id'] = j["Id"]
            item["name"] = j["Name"]
            item["url"] = domain + j["SeName"]
            item["brand"] = j["BrandName"]
            item["price"] = j["Price"]
            item["special_price"] = j["SpecialPrice"]
            item["specification"] = j["Specification"]
            item["strcategory"] = j["StrCategory"]
            yield item
