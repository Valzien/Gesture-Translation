import cv2
import mediapipe as mp
import os
import numpy as np

GESTURE_NAME = input("Masukkan nama gesture (contoh: peace, ok, fist): ").strip()
SAVE_DIR = f'images/{GESTURE_NAME}'
os.makedirs(SAVE_DIR, exist_ok=True)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(1)  # External camera

count = 0
max_count = 100  # Jumlah gambar per gesture

print("[INFO] Tekan 's' untuk simpan data, 'q' untuk keluar.")

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    cv2.putText(img, f"Gesture: {GESTURE_NAME} | Tersimpan: {count}/{max_count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
    cv2.imshow("Capture Gesture", img)

    key = cv2.waitKey(1)
    if key == ord('s') and result.multi_hand_landmarks:
        # Ambil titik koordinat
        for handLms in result.multi_hand_landmarks:
            landmarks = []
            for lm in handLms.landmark:
                landmarks.append([lm.x, lm.y])
            landmarks = np.array(landmarks).flatten()
            np.save(f"{SAVE_DIR}/{GESTURE_NAME}_{count}.npy", landmarks)
            print(f"[+] Tersimpan: {SAVE_DIR}/{GESTURE_NAME}_{count}.npy")
            count += 1

            if count >= max_count:
                print("[INFO] Selesai mengumpulkan data.")
                cap.release()
                cv2.destroyAllWindows()
                exit()

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
