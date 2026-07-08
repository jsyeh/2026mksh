# day03_2_processing_python_def_mousePressed_if_mouseButton_bonus
# 修改自 day03_1_processing_python_textSize_text
a = [0, 1, 2, 3, 4]

def mousePressed():  # mouse按下去,對應的函式
    i = mouseX // 100
    if mouseButton==LEFT: a[i] += 1
    else: a[i] -= 1

def setup():  # 設定的函式
    size(500, 100)  # 視窗大小 500x100
    
def draw():  # 畫圖的函式
    for i in range(5):  # 迴圈跑5次
        fill(255, 255, 242)  # 淡黃色、米色
        rect(i*100, 0, 100, 100)  # 畫格子
        
        fill(255, 0, 0)  # 紅色的字
        textSize(80)
        text( a[i], i*100, 80)  # 畫出 a[i]
    textSize(30)
    text(mouseX, mouseX, mouseY)
