# Sử dụng Python 3.9
FROM python:3.9

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép requirements.txt trước để cài đặt dependencies
COPY ../requirements.txt /app/requirements.txt

# Cài đặt thư viện
RUN pip install --no-cache-dir -r /app/requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . /app

# Chạy chương trình chính
CMD ["python", "src/main.py"]