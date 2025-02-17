import os
import sys
from bs4 import BeautifulSoup
from .base_crawler import BaseCrawler
from database import CSVHandler, TXTHandler, MongoHandler
from utils import setup_logger, clean_text

# Thiết lập logger
logger = setup_logger('site1_crawler', 'site1_crawler.log')

class FPTShopCrawler(BaseCrawler):
    def __init__(self, url):
        super().__init__(url)

    def parse_page(self, html):
        """Phân tích HTML và lấy thông tin sản phẩm từ FPT Shop"""
        soup = BeautifulSoup(html, "html.parser")
        products = []

        product_list = soup.find_all("div", class_="flex-1")

        for product in product_list:
            try:
                name_tag = product.find("h3", class_="ProductCard_cardTitle__HlwIo")
                price_tag = product.find("p", class_="Price_currentPrice__PBYcv")

                name = clean_text(name_tag.text) 
                price = clean_text(price_tag.text) 
                link = "https://fptshop.com.vn" + name_tag.find("a")["href"] if name_tag else "#"

                products.append({"Tên sản phẩm": name, "Giá": price, "Link": link})
            except AttributeError:
                continue
        
        return products

    def run(self):
        """Chạy quá trình crawl"""
        html = self.fetch_page()
        if html:
            products = self.parse_page(html)
            if products:
                self.save_to_csv(products, "data/csv/fptshop_products.csv")
                self.save_to_txt(products, "data/txt/fptshop_products.txt")
                self.save_to_mongo(products, db_name="bigdata_week1", collection_name="fptshop")
            else:
                logger.error("Không tìm thấy sản phẩm nào!")

# Chạy crawler cho danh mục điện thoại trên FPT Shop
if __name__ == "__main__":
    url = "https://fptshop.com.vn/dien-thoai"
    crawler = FPTShopCrawler(url)
    crawler.run()
