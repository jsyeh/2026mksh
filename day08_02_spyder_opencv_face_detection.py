# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 09:40:12 2026

@author: user
"""

# day08_02_spyder_opencv_face_detection
# prompt: 我想要在剛剛的程式延伸, 能夠偵測到人臉, 用一些線條或圓形, 把臉框起來。請問要再做什麼修改?


import cv2

# 載入 OpenCV 內建的人臉偵測模型
face_model_path = (
    cv2.data.haarcascades
    + "haarcascade_frontalface_default.xml"
)

face_detector = cv2.CascadeClassifier(face_model_path)

# 檢查模型是否載入成功
if face_detector.empty():
    print("人臉偵測模型載入失敗")
    raise SystemExit

# 開啟 Webcam
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("無法開啟攝影機")
    raise SystemExit

try:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("無法讀取攝影機畫面")
            break

        # 左右鏡像
        frame = cv2.flip(frame, 1)

        # 人臉偵測通常使用灰階影像
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 偵測人臉
        faces = face_detector.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(60, 60)
        )

        # faces 裡每一筆資料都是 x, y, w, h
        for x, y, w, h in faces:

            # 畫矩形框
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                3
            )

        cv2.imshow("Face Detection", frame)

        # 按 ESC 離開
        key = cv2.waitKey(1)

        if key == 27:
            break

finally:
    cap.release()
    cv2.destroyAllWindows()