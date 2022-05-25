#include <Arduino.h>
#include <string.h>

// ESP32 Libs
#include <WiFi.h>
#include <WiFiUdp.h>

// BMP280 Libs
#include <Adafruit_BMP280.h>
#include <Adafruit_Sensor.h>

#define I2C_ADDRESS 0x76

// predeclaration Error function
String nan_Error(String);

const char* ssid = "2.4 GHz";
const char* wifiPwd = "KirscheBananeErdbeere1";

const char* udpAddress = "192.168.0.193";
const int udpPort = 1235;

// make objects from classes
Adafruit_BMP280 bmp;
WiFiUDP udp;


void setup() {
  Serial.begin(115200);

  // connect BMP280 over I2C
  if(!bmp.begin(I2C_ADDRESS)){ // or 0x77, check on raspberry pi via sudo apt install i2c-tools; i2cdetect -y 1
    Serial.println("Check your wiring!\n Can't connect bmp280!\n");
    Serial.println(bmp.sensorID());
  }
  else{
    Serial.println("bmp280 connected!");
  }

  // connect wifi
  WiFi.begin(ssid,wifiPwd);
  while(WiFi.status() != WL_CONNECTED){
    Serial.print("...\t");
    delay(500);
  }
  Serial.println("Connected");
  Serial.println(ssid);
  Serial.println(WiFi.localIP());
}

void loop() {
  String temperature = (String)bmp.readTemperature();
  temperature = nan_Error(temperature);
  udp.beginPacket(udpAddress,udpPort);
  udp.print(temperature);
  udp.endPacket();
  Serial.println(bmp.readTemperature(),2);
  delay(2500);
  }

String nan_Error(String check){
  if (check == "nan"){
    bmp.begin(I2C_ADDRESS);
    delay(500);
    check == (String)bmp.readTemperature();
  }
  return check;
}