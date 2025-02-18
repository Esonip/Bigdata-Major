# CRAWLER PROJECT

## Giới thiệu
Dự án xây dựng hệ thống thu thập dữ liệu từ các trang web như FPTShop và Nhaccuatui, sau đó lưu trữ vào các tệp CSV, TXT và cơ sở dữ liệu MongoDB.

## Cấu trúc thư mục
```
22701391/                       # Tên Project
│── docker/                     # Cấu hình Docker
│   ├── docker-compose.yml
│   ├── Dockerfile
│── src/
│   ├── crawlers/               # Chứa các script crawler
│   │   ├── __init__.py
│   │   ├── base_crawler.py      # Lớp cơ sở cho các crawler
│   │   ├── site1_crawler.py     # Crawler cho trang DienMayXanh
│   │   ├── site2_crawler.py     # Crawler cho trang VnExpress
│   ├── database/               # Chứa các module xử lý database
│   │   ├── __init__.py
│   │   ├── mongo_handler.py    
│   │   ├── txt_handler.py   
│   │   ├── csv_handler.py  
│   ├── utils/                  # Chứa các tiện ích hỗ trợ
│   │   ├── __init__.py
│   │   ├── logger.py    
│   │   ├── helpers.py  
│   ├── main.py                 # File chính
│── data/                       # Thư mục lưu trữ dữ liệu crawl được
│   ├── csv/
│   │   ├── fptshop_products.csv
│   │   ├── nhaccuatui_songs.csv
│   ├── txt/
│   │   ├── fptshop_products.txt
│   │   ├── nhaccuatui_songs.txt
│── config/
│   ├── settings.yml            # Cấu hình chung
│── requirements.txt            # Danh sách thư viện cần thiết
│── README.md                   # Tài liệu hướng dẫn
```

## Cài đặt
### 1. Cài đặt môi trường
Yêu cầu:
- Python 3.9+
- Docker & Docker Compose
- Cài đặt các thư viện cần thiết:
  ```bash
  pip install -r requirements.txt
  ```

### 2. Chạy chương trình
Chạy crawler bằng lệnh:
```bash
python src/main.py
```

### 3. Đóng gói & chạy với Docker
#### a) Xây dựng Docker Image
```bash
cd docker
docker-compose build
```
#### b) Chạy Docker Container
```bash
docker-compose up -d
```

#### c) Kiểm tra container hoạt động
```bash
docker ps
```

## Liên hệ
Nếu có vấn đề hoặc cần hỗ trợ, vui lòng liên hệ qua email: dothanhminhphu@gmail.com
