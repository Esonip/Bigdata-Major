from crawlers.site1_crawler import FPTShopCrawler
from crawlers.site2_crawler import NhaccuatuiCrawler

if __name__ == '__main__':
    print("Crawling from FPTShop")
    url = "https://fptshop.com.vn/dien-thoai"
    crawler = FPTShopCrawler(url)
    crawler.run()
    
    print("Crawling from Nhaccuatui")
    url = "https://www.nhaccuatui.com/bai-hat/nhac-tre-moi.html"
    crawler = NhaccuatuiCrawler(url)
    crawler.run()