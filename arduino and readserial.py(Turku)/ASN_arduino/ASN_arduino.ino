// Example testing sketch for various DHT humidity/temperature sensors


#include "DHT.h"

#define DHTPIN 2     // what pin we're connected to

#define DHTTYPE DHT22   // DHT 22  (AM2302)

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600); 
  Serial.println("DHT22 test!");
 
  dht.begin();
}

int16_t h = dht.readHumidity()*10;
  int16_t t = dht.readTemperature()*10;
  if (isnan(t) || isnan(h)) {
    Serial.println("Failed to read from DHT");
  } else {
    Serial.write(0x00);
    Serial.write(highByte(h));
    Serial.write(lowByte(h));
    Serial.write(highByte(t));
    Serial.write(lowByte(t));
    delay(2000);
  }
}

