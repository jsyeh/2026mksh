# -*- coding: utf-8 -*-
# day08_04_spyder_face_detect_hat.py
import cv2


def overlay_png(background, foreground, x, y):
    """把透明 PNG 疊到背景畫面上。"""

    bg_h, bg_w = background.shape[:2]
    fg_h, fg_w = foreground.shape[:2]

    if x >= bg_w or y >= bg_h:
        return

    if x + fg_w <= 0 or y + fg_h <= 0:
        return

    fg_x1 = max(0, -x)
    fg_y1 = max(0, -y)
    fg_x2 = min(fg_w, bg_w - x)
    fg_y2 = min(fg_h, bg_h - y)

    bg_x1 = max(0, x)
    bg_y1 = max(0, y)
    bg_x2 = bg_x1 + (fg_x2 - fg_x1)
    bg_y2 = bg_y1 + (fg_y2 - fg_y1)

    foreground_crop = foreground[
        fg_y1:fg_y2,
        fg_x1:fg_x2
    ]

    if foreground_crop.size == 0:
        return

    foreground_bgr = foreground_crop[:, :, :3]

    alpha = foreground_crop[:, :, 3] / 255.0
    alpha = alpha[:, :, None]

    background_crop = background[
        bg_y1:bg_y2,
        bg_x1:bg_x2
    ]

    blended = (
        foreground_bgr * alpha
        + background_crop * (1.0 - alpha)
    )

    background[
        bg_y1:bg_y2,
        bg_x1:bg_x2
    ] = blended.astype("uint8")


# 載入人臉偵測模型
face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades
    + "haarcascade_frontalface_default.xml"
)

if face_detector.empty():
    print("人臉偵測模型載入失敗")
    raise SystemExit


# 載入透明帽子圖片
hat = cv2.imread(
    "hat.png",
    cv2.IMREAD_UNCHANGED
)

if hat is None:
    print("找不到 hat.png")
    print("請確認 hat.png 與程式放在相同資料夾")
    raise SystemExit

# 確認帽子有透明通道
if len(hat.shape) != 3 or hat.shape[2] != 4:
    print("hat.png 必須是透明背景的四通道 PNG")
    raise SystemExit


# 開啟 Webcam
cap = cv2.VideoCapture(
    1,
    cv2.CAP_DSHOW
)

if not cap.isOpened():
    print("無法開啟攝影機")
    raise SystemExit


# 平滑人臉框座標
smooth_x = None
smooth_y = None
smooth_w = None
smooth_h = None

alpha_smooth = 0.20

missing_frames = 0
max_missing_frames = 10


try:
    while True:

        ret, frame = cap.read()

        if not ret:
            print("無法讀取攝影機畫面")
            break

        # 自拍鏡像
        frame = cv2.flip(frame, 1)

        # 灰階影像用來偵測人臉
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

            missing_frames = 0

            # 找畫面中最大的人臉
            x, y, w, h = max(
                faces,
                key=lambda face: face[2] * face[3]
            )

            if smooth_x is None:
                smooth_x = float(x)
                smooth_y = float(y)
                smooth_w = float(w)
                smooth_h = float(h)

            else:
                smooth_x = (
                    alpha_smooth * x
                    + (1 - alpha_smooth) * smooth_x
                )

                smooth_y = (
                    alpha_smooth * y
                    + (1 - alpha_smooth) * smooth_y
                )

                smooth_w = (
                    alpha_smooth * w
                    + (1 - alpha_smooth) * smooth_w
                )

                smooth_h = (
                    alpha_smooth * h
                    + (1 - alpha_smooth) * smooth_h
                )

        else:
            missing_frames += 1

            if missing_frames > max_missing_frames:
                smooth_x = None
                smooth_y = None
                smooth_w = None
                smooth_h = None


        # 有有效的人臉位置時，放上帽子
        if smooth_x is not None:

            sx = int(smooth_x)
            sy = int(smooth_y)
            sw = int(smooth_w)
            sh = int(smooth_h)

            # 帽子寬度比人臉略寬
            hat_width = int(sw * 1.45)

            # 維持帽子圖片原來的長寬比例
            hat_height = int(
                hat.shape[0]
                * hat_width
                / hat.shape[1]
            )

            resized_hat = cv2.resize(
                hat,
                (hat_width, hat_height),
                interpolation=cv2.INTER_AREA
            )

            # 帽子水平方向對準人臉中心
            hat_x = (
                sx
                + sw // 2
                - hat_width // 2
            )

            # 帽子底部靠近額頭
            hat_y = (
                sy
                - int(hat_height * 0.72)
            )

            overlay_png(
                frame,
                resized_hat,
                hat_x,
                hat_y
            )

            # 測試時可保留人臉框
            cv2.rectangle(
                frame,
                (sx, sy),
                (sx + sw, sy + sh),
                (0, 255, 0),
                2
            )

        cv2.imshow(
            "Virtual Hat",
            frame
        )

        # ESC 離開
        if cv2.waitKey(1) == 27:
            break

finally:
    cap.release()
    cv2.destroyAllWindows()