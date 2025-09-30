import os
from datetime import datetime
import mss

# 📅 Získání aktuálního data a času
now = datetime.now()
folder_name = now.strftime("%Y-%m")  # např. "2025-09"
file_name = now.strftime("%Y-%m-%d__%H-%M-%S") + ".png"

# 📁 Cílová složka
base_path = r"C:\Users\Rumlar\Documents\_privat\work-screenshots"
full_path = os.path.join(base_path, folder_name)

# 📁 Vytvoření složky, pokud neexistuje
os.makedirs(full_path, exist_ok=True)

# 📸 Screenshot pomocí mss
with mss.mss() as sct:
    screenshot = sct.shot(output=os.path.join(full_path, file_name))

# print(f"Screenshot uložen jako: {screenshot}")
