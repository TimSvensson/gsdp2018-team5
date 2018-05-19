work flow:
======
First, connect the wires each component, connect HC-05 Bluetooth to the server by using UART, configure on the computer (because sever is not finished by other team members, so we test in local), remember to check the COM port consistent with the COM port of python file, and run the python file, the server can receive the values of sensor.
![](http://ww1.sinaimg.cn/large/61446e99gy1frg5zn4s1hj20o10b4q4h.jpg)

Then we can see the value of humidity and temperature on the terminal, and note that JSON file is success created.
![](http://ww1.sinaimg.cn/large/61446e99gy1frg61iv8joj20o10f6n0y.jpg)
After using my mouth to blow hot air on the sensor, the temperature and humidity have changed obviously.
![](http://ww1.sinaimg.cn/large/61446e99gy1frg62bimbyj20o10gxgq0.jpg)
And you can see test.json in the folder.
![](http://ww1.sinaimg.cn/large/61446e99gy1frg63nb9owj20o003p74r.jpg)
open the test.json, you can see the current value of humidity and temperature.
![](http://ww1.sinaimg.cn/mw690/61446e99gy1frg64qo778j20ig08et9m.jpg)

Note:
======
![](http://ww1.sinaimg.cn/large/61446e99gy1frg66s505pj20hx0580v8.jpg)

We totally send 5 bytes data from Arduino write to the serial, 0x00 is the start byte, second and third bytes are the value of humidity, while fourth and fifth bytes are the value of temperature.
![](http://ww1.sinaimg.cn/large/61446e99gy1frg67kfl8vj20o1093788.jpg)
In python file, read from corresponding bytes for humidity and temperature, convert these values to integer, then transform to json format.
