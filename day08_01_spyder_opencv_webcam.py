# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 09:32:57 2026
@author: user
"""
# day08_01_spyder_opencv_webcam
# 我們想在 Spyder 裡, 使用 OpenCV 讀入webcam視訊鏡頭的畫面, 即時更新。
# 要做哪些步驟? 有哪些可能卡住的地方?
# 因為中文的注音輸入法, 會卡住 q 鍵, 可以改成 ESC 鍵退出 OpenCV 程式嗎?
import cv2

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

while cap.isOpened():

    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1)

    # ESC 離開
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()