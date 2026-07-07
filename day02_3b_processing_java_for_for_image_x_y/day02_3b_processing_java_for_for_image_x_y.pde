// day02_3b_processing_java_for_for_image_x_y
// 練習用 for 迴圈
PImage img;
void setup() {
  size(500, 300);
  img = loadImage("cat.png");
} // 要記得,把 cat.png 圖檔,拉入程式裡

void draw() {
  background(255);
  for (int x=0; x<500; x+=100) { // x座標, 每次加100
    for (int y=0; y<300; y+=100) { // y座標, 每次加100
      image(img, x, y, 100, 100);
    }
  }
}
