// day04_06a_processing_java_progress_bar
int blood = 0; 
void setup() {
  size(300, 50);
}
void draw() {
  background(255);
  fill(255, 0, 0);
  rect(0, 0, blood, 50);
  blood += 1;
}
