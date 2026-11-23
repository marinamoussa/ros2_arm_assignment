#include <Servo.h>

Servo s1;
Servo s2;
Servo s3;
Servo s4;

String line = "";

void setup() {
  Serial.begin(115200);
  s1.attach(3);
  s2.attach(5);
  s3.attach(6);
  s4.attach(9);
  s1.write(90);
  s2.write(90);
  s3.write(90);
  s4.write(90);
}

void loop() {
  while (Serial.available() > 0) {
    char c = (char)Serial.read();
    if (c == '\n') {
      int a[4] = {90, 90, 90, 90};
      int idx = 0;
      int start = 0;
      for (int i = 0; i <= line.length() && idx < 4; i++) {
        if (i == line.length() || line.charAt(i) == ',') {
          int v = line.substring(start, i).toInt();
          a[idx++] = constrain(v, 0, 180);
          start = i + 1;
        }
      }
      s1.write(a[0]);
      s2.write(a[1]);
      s3.write(a[2]);
      s4.write(a[3]);
      line = "";
    } else if (c != '\r') {
      line += c;
    }
  }
}
