import os
import pandas as pd

class CSVHandler:
    @staticmethod
    def save_to_csv(data, filename="data/csv/data.csv", mode="w"):
        # Tạo thư mục nếu chưa tồn tại
        directory = os.path.dirname(filename)
        os.makedirs(directory, exist_ok=True)

        # Chuyển đổi dữ liệu thành DataFrame
        df = pd.DataFrame(data)
        df.to_csv(filename, mode=mode, index=False, encoding="utf-8",)

        print(f"Saved to {filename}")
