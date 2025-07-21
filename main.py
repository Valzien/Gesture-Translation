import cv2
import mediapipe as mp
import numpy as np
import pickle
from gtts import gTTS
from playsound import playsound
import os
import uuid
import threading
import time

# TTS Bahasa Indonesia (thread-safe)
def speak_indonesian(text):
    tts = gTTS(text=text, lang='id')
    filename = f"temp_{uuid.uuid4().hex}.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

# Load model gesture KNN
with open('model/gesture_model.pkl', 'rb') as f:
    model = pickle.load(f)

# MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

# Kamera
selected_cam_index = 1
cap = cv2.VideoCapture(selected_cam_index)

if not cap.isOpened():
    print(f"[!] Gagal membuka kamera di index {selected_cam_index}")
    exit()

print(f"[+] Menggunakan kamera index {selected_cam_index}")

# Mapping gesture → kalimat
gesture_to_text = {
    "peace": "Salam damai",
    "ok": "Oke siap",
    "good": "Bagus",
}

# Timer cooldown
last_spoken_time = 0
cooldown = 2  # dalam detik

# Loop utama
while True:
    success, img = cap.read()
    if not success:
        print("Gagal membaca frame dari kamera.")
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            # Ambil titik landmark tangan
            landmarks = []
            for lm in handLms.landmark:
                landmarks.extend([lm.x, lm.y])

            # Prediksi gesture
            if len(landmarks) == 42:
                prediction = model.predict([np.array(landmarks)])
                gesture_name = prediction[0]

                # Tampilkan hasil prediksi
                cv2.putText(img, f"Gesture: {gesture_name}", (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

                # Jika cukup waktu berlalu → TTS di thread
                current_time = time.time()
                if current_time - last_spoken_time > cooldown:
                    kalimat = gesture_to_text.get(gesture_name, f"Gerakan {gesture_name}")
                    threading.Thread(target=speak_indonesian, args=(kalimat,)).start()
                    last_spoken_time = current_time

    cv2.imshow("Gesture Prediction", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
