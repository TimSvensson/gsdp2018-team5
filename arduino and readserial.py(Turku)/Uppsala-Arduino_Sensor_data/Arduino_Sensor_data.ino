/**
   Example for reading temperature and humidity
   using the DHT22 and ESP8266

   Copyright (c) 2016 Losant IoT. All rights reserved.
   https://www.losant.com
*/

#include "DHT.h"
#include <Wire.h>
#include "Adafruit_SI1145.h"

#define DHTPIN 7     // what digital pin the DHT22 is conected to
#define DHTTYPE DHT22   // there are multiple kinds of DHT sensors



DHT dht(DHTPIN, DHTTYPE);

Adafruit_SI1145 uv = Adafruit_SI1145();

bool uvSensor;


void setup() {
  Serial1.begin(9600);
  Serial1.setTimeout(2000);

  // Wait for serial to initialize.
  while (!Serial1) { }

  Serial1.println("Device Started");
  Serial1.println("-------------------------------------");
  Serial1.println("Running DHT!");
  Serial1.println("-------------------------------------");



  // check if uv Sensor is connected, skip if not connected.
  if (! uv.begin()) {
    uvSensor = false;
    Serial1.println("Didn't find UV Sensor Si1145, will continue without");
  } else {
    uvSensor = true;
  }

}

int timeSinceLastRead = 0;
void loop() {
  // update values every 2 second.
  if (timeSinceLastRead > 2000) {

    // check if uv Sensor is connected. Run measurement if connected.
    if (uvSensor) {
      Serial1.println("===================");
      Serial1.print("Vis: "); Serial1.println(uv.readVisible());
      Serial1.print("IR: "); Serial1.println(uv.readIR());

      float UVindex = uv.readUV();
      // the index is multiplied by 100 so to get the
      // integer index, divide by 100!
      UVindex /= 100.0;
      Serial1.print("UV: ");  Serial1.println(UVindex);
    }

    // Reading temperature or humidity takes about 250 milliseconds!
    // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
    float h = dht.readHumidity();
    // Read temperature as Celsius (the default)
    float t = dht.readTemperature();
    // Read temperature as Fahrenheit (isFahrenheit = true)
    float f = dht.readTemperature(true);

    // Check if any reads failed and exit early (to try again).
    if (isnan(h) || isnan(t) || isnan(f)) {
      Serial1.println("Failed to read from DHT sensor!");
      timeSinceLastRead = 0;
      return;
    }

    // Compute heat index in Fahrenheit (the default)
    float hif = dht.computeHeatIndex(f, h);
    // Compute heat index in Celsius (isFahreheit = false)
    float hic = dht.computeHeatIndex(t, h, false);
    Serial1.println("===================");
    Serial1.print("Humidity: "); Serial1.print(h); Serial1.println(" %\t");
    Serial1.print("Temperature: "); Serial1.print(t); Serial1.print(" *C / "); Serial1.print(f); Serial1.println(" *F\t");
    Serial1.print("Heat index: "); Serial1.print(hic); Serial1.print(" *C / "); Serial1.print(hif); Serial1.println(" *F");

    timeSinceLastRead = 0;
  }
  delay(100);
  timeSinceLastRead += 100;


}
