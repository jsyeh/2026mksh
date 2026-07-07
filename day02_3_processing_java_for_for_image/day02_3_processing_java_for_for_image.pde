// day02_3_processing_java_for_for_image
// 練習用 for 迴圈
PImage img;
void setup() {
  size(500, 300);
  img = loadImage("cat.png");
} // 要記得,把 cat.png 圖檔,拉入程式裡

void draw() {
  background(255);
  for (int i=0; i<3; i++) { // 左手i 對應y
    for (int j=0; j<5; j++) { // 右手j 對應x
      image(img, j*100, i*100, 100, 100);
    }         // x座標, y座標
  }
}
