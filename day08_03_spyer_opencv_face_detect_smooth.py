# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 10:03:06 2026

@author: user
"""
# day08_03_spyer_opencv_face_detect_smooth
# Prompt: face detect 出來的人臉會有點抖動, 為什麼? 請問要怎麼改成沒有抖動的版本?

import cv2

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades
    + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("無法開啟攝影機")
    raise SystemExit

# 平滑後的人臉座標
smooth_x = None
smooth_y = None
smooth_w = None
smooth_h = None

# 平滑係數
# 越小越平穩，但反應較慢
# 越大反應越快，但比較容易抖動
alpha = 0.20

try:
    while True:

        ret, frame = cap.read()

        if not ret:
            print("無法讀取畫面")
            break

        frame = cv2.flip(frame, 1)

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        faces = face_detector.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(60, 60)
        )

        if len(faces) > 0:

            # 找出面積最大的人臉
            x, y, w, h = max(
                faces,
                key=lambda face: face[2] * face[3]
            )

            # 第一次找到人臉時，直接使用偵測結果
            if smooth_x is None:
                smooth_x = x
                smooth_y = y
                smooth_w = w
                smooth_h = h

            else:
                # 指數移動平均
                smooth_x = (
                    alpha * x
                    + (1 - alpha) * smooth_x
                )

                smooth_y = (
                    alpha * y
                    + (1 - alpha) * smooth_y
                )

                smooth_w = (
                    alpha * w
                    + (1 - alpha) * smooth_w
                )

                smooth_h = (
                    alpha * h
                    + (1 - alpha) * smooth_h
                )

            # 畫圖時需要整數座標
            sx = int(smooth_x)
            sy = int(smooth_y)
            sw = int(smooth_w)
            sh = int(smooth_h)

            cv2.rectangle(
                frame,
                (sx, sy),
                (sx + sw, sy + sh),
                (0, 255, 0),
                3
            )

        cv2.imshow(
            "Smooth Face Detection",
            frame
        )

        # 按 ESC 離開
        if cv2.waitKey(1) == 27:
            break

finally:
    cap.release()
    cv2.destroyAllWindows()