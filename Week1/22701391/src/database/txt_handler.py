import os

class TXTHandler:
    @staticmethod
    def save_to_txt(data, filename="data/txt/data.txt"):
        
        # Tạo thư mục nếu nó không tồn tại
        directory = os.path.dirname(filename)
        os.makedirs(directory, exist_ok=True)
        
        with open(filename, "w", encoding="utf-8") as file:
            for item in data:
                for key, value in item.items():
                    file.write(f"{key}: {value}\n")
                file.write("\n")
        print(f"Saved to {filename}")