import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pickle

# Path ke folder gesture 
DATA_DIR = "images"

# Siapkan list untuk data dan label
data = []
labels = []

# Baca semua folder di dalam images 
for gesture_name in os.listdir(DATA_DIR):
    gesture_folder = os.path.join(DATA_DIR, gesture_name)
    
    if not os.path.isdir(gesture_folder):
        continue

    # Baca semua file .npy dalam folder gesture
    for file_name in os.listdir(gesture_folder):
        if file_name.endswith(".npy"):
            file_path = os.path.join(gesture_folder, file_name)
            landmark = np.load(file_path)
            data.append(landmark)
            labels.append(gesture_name)

print(f"[+] Total data: {len(data)}")
print(f"[+] Kelas gesture ditemukan: {set(labels)}")

# Ubah ke numpy array
X = np.array(data)
y = np.array(labels)

# Split jadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Gunakan KNN (K-Nearest Neighbors)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

# Evaluasi
acc = model.score(X_test, y_test)
print(f"[✓] Akurasi pada data uji: {acc * 100:.2f}%")

# Simpan model ke file
MODEL_PATH = "model/gesture_model.pkl"
with open(MODEL_PATH, "wb") as f:
    pickle.dump(model, f)

print(f"[✓] Model disimpan ke: {MODEL_PATH}")
