import os
import requests
import pandas as pd
from database.csv_handler import CSVHandler
from database.txt_handler import TXTHandler
from database.mongo_handler import MongoHandler

class BaseCrawler:
    def __init__(self, url, headers=None):
        self.url = url
        self.headers = headers or {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
        }

    def fetch_page(self):
        """Gửi request và lấy nội dung trang"""
        response = requests.get(self.url, headers=self.headers)
        
        if response.status_code == 200:
            return response.text
        else:
            print(f"Lỗi khi truy cập: {response.status_code}")
            return None

    def save_to_csv(self, data, filename):
        CSVHandler.save_to_csv(data, filename)

    def save_to_txt(self, data, filename):
        TXTHandler.save_to_txt(data, filename)

    def save_to_mongo(self, data, db_name, collection_name):
        mongo = MongoHandler(db_name=db_name, collection_name=collection_name)
        mongo.save_to_mongo(data)