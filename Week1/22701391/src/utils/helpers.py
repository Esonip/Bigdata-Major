import re

def clean_text(text):
    """Làm sạch văn bản"""
    text = re.sub(r'\s+', ' ', text)  # Loại bỏ khoảng trắng thừa
    text = text.strip()  # Loại bỏ khoảng trắng ở đầu và cuối
    return text