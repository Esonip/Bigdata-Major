# CRAWLER PROJECT

## Giới thiệu
Dự án này là một hệ thống thu thập dữ liệu từ các trang web như DienMayXanh và VnExpress, sau đó lưu trữ vào các tệp CSV, TXT hoặc cơ sở dữ liệu như MongoDB, MySQL, PostgreSQL.

## Cấu trúc thư mục
```
CRAWLER_PROJECT/
│── config/
│   ├── settings.yml            # Cấu hình chung của dự án
│
│── data/                       # Thư mục lưu trữ dữ liệu crawl được
│   ├── csv/
│   │   ├── dienmayxanh_products.csv
│   │   ├── vnexpress_news.csv
│   ├── txt/
│       ├── dienmayxanh_products.txt
│       ├── vnexpress_news.txt
│
│── docker/                     # Cấu hình Docker
│   ├── docker-compose.yml
│   ├── Dockerfile
│
│── src/
│   ├── crawlers/               # Chứa các script crawler
│   │   ├── __init__.py
│   │   ├── base_crawler.py      # Lớp cơ sở cho các crawler
│   │   ├── site1_crawler.py     # Crawler cho trang DienMayXanh
│   │   ├── site2_crawler.py     # Crawler cho trang VnExpress
│   ├── database/               # Chứa các module xử lý database
│   ├── utils/                  # Chứa các tiện ích hỗ trợ
│   ├── main.py                 # File chạy chính của dự án
│
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
docker build -t crawler_project .
```
#### b) Chạy Docker Container
```bash
docker-compose -f docker/docker-compose.yml up -d
```

#### c) Kiểm tra logs
```bash
docker logs -f crawler_project
```

## Liên hệ
Nếu có vấn đề hoặc cần hỗ trợ, vui lòng liên hệ qua email: support@example.com
