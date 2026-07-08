# day03_6_processing_python_countdown
# 修改自 day03_5_processing_python_countdown
# 有時候變負數, 而且太快開始, 而且不能暫停!
# OK (1) 小鹿: 用 max() 找最大值 max(負數, 0) 
# 明天再弄(2) 鬧鐘要可以「修改」用 day03_3 的 mouseDragged 來滑動
# 明天再弄(3) 要可以暫停
target = 0  # 我們的目標時間
def setup():  # 設定的函式
    global target  # 要可以修改外面的 target 變數
    size(500, 200)  # 視窗大小
    mm = minute()  # 分鐘(現在的時間)
    ss = second()  # 秒鐘(現在的時間)
    target = (mm+0)*60 + ss +10 # 我們的 target 目標時間 

def draw():  # 畫圖的函式
    background(0)  # 背景黑色
    textSize(150)  # 字很大 150號字
    remain = max(target - minute()*60 - second(), 0)  # 剩下的秒數
    mm = remain // 60  # 分鐘
    ss = remain % 60  # 秒鐘
    text( nf(mm,2) + ":" + nf(ss,2), 80, 150)  # 接成數字
