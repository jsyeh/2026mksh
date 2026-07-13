# day06_01_spyder_opencv_capture.py
# 從 ChatGPT 得到的程式 
# 修改自 day04_07_processing_java_video_library_Capture_start_read

import cv2

# 開啟第一台攝影機
cam = cv2.VideoCapture(0)  # 0:第1台 1:第2台 ...
# cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# 設定解析度
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # 視訊寬度
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # 視訊高度

while True:  # 迴圈會一直跑, 直到有 break 跳開結束

    # 讀取一張畫面
    ret, frame = cam.read()

    if not ret:  # 若沒有成功, 就離開
        break

    # 顯示畫面
    cv2.imshow("Capture", frame)

    if cv2.waitKey(1) == 27:  # 按 Esc 離開 (改成按 Esc 離開)
        break  # waitKey(等多久? 單位 ms)


cam.release()  # 把 camera 正確關閉 (收尾很重要)
cv2.destroyAllWindows()  # 把剛剛開啟的 OpenCV 視窗全部關掉