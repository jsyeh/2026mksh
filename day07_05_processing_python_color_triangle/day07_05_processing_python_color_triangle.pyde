# day07_05_processing_python_color_triangle
def setup():
    size(500, 500, P3D)
    background(0)

    beginShape()

    fill(255, 0, 0)
    vertex(250, 50)

    fill(0, 255, 0)
    vertex(400, 400)

    fill(0, 0, 255)
    vertex(100, 400)

    endShape()
