import os
import string

# Nama folder utama
main_folder = "images"

# Buat folder utama jika belum ada
os.makedirs(main_folder, exist_ok=True)

# Buat subfolder A sampai Z
for letter in string.ascii_uppercase:
    path = os.path.join(main_folder, letter)
    os.makedirs(path, exist_ok=True)

print("Folder gesture_dataset dengan subfolder A-Z berhasil dibuat.")
