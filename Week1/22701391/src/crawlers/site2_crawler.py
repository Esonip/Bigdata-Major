import os
import sys
from bs4 import BeautifulSoup
from .base_crawler import BaseCrawler
from database import CSVHandler, TXTHandler, MongoHandler
from utils import setup_logger, clean_text

# Thiết lập logger
logger = setup_logger('site2_crawler', 'site2_crawler.log')

class NhaccuatuiCrawler(BaseCrawler):
    def __init__(self, base_url):
        super().__init__(base_url)

    def parse_page(self, html):
        """Phân tích HTML và lấy thông tin bài hát từ Nhaccuatui"""
        soup = BeautifulSoup(html, "html.parser")
        songs = []
        
        song_list = soup.find_all("div", class_="info_song")
        
        for song in song_list:
            try:
                title_tag = song.find("a", class_="name_song")
                artist_tag = song.find("a", class_="name_singer")

                title = clean_text(title_tag.text) if title_tag else "N/A"
                artist = clean_text(artist_tag.text) if artist_tag else "N/A"
                link = title_tag["href"] if title_tag else "#"

                songs.append({
                    "Tên bài hát": title,
                    "Nghệ sĩ": artist,
                    "Link": link
                })
            except AttributeError:
                continue
        
        return songs

    def run(self):
        """Chạy quá trình crawl"""
        html = self.fetch_page()
        if html:
            songs = self.parse_page(html)
            if songs:
                self.save_to_csv(songs, "data/csv/nhaccuatui_songs.csv")
                self.save_to_txt(songs, "data/txt/nhaccuatui_songs.txt")
                self.save_to_mongo(songs, db_name="bigdata_week1", collection_name="nhaccuatui")
            else:
                logger.error("Không tìm thấy bài hát nào!")
        
# Chạy crawler cho danh sách bài hát trên ZingMP3
if __name__ == "__main__":
    base_url = "https://www.nhaccuatui.com/bai-hat/nhac-tre-moi.html"
    crawler = NhaccuatuiCrawler(base_url)
    crawler.run()