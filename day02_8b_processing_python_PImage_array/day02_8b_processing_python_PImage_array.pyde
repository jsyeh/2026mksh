# day02_8b_processing_python_PImage_array
# 把 day02_8a_processing_python_PImage_array 放到 AI 裡翻譯成 Python 版本
img = None
img2 = None

# 二維陣列
a = [
    [0, 1, 1, 1, 1],
    [1, 2, 1, 1, 1],
    [1, 1, 1, 1, 1]
]

def setup():
    global img, img2

    size(500, 300)

    img = loadImage("cat.png")
    img2 = loadImage("cat2.png")


def draw():
    background(255)

    for i in range(3):      # 列 (y)
        for j in range(5):  # 行 (x)

            if a[i][j] == 1:
                image(img, j * 100, i * 100, 100, 100)

            if a[i][j] == 2:
                image(img2, j * 100, i * 100, 100, 100)


def mousePressed():
    i = mouseY // 100
    j = mouseX // 100

    a[i][j] = (a[i][j] + 1) % 3
