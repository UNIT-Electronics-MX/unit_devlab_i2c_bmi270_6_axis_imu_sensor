# BMI270 Arduino Code Explanation

This document explains how the Arduino sketch communicates with the **BMI270 IMU sensor** via **I2C**, using the **SparkFun BMI270 Arduino Library**.

---

## Included Libraries and Object Initialization

```cpp
#include <Wire.h>
#include "SparkFun_BMI270_Arduino_Library.h"

BMI270 imu;
```

- `Wire.h`: Enables I2C communication.  
- `SparkFun_BMI270_Arduino_Library.h`: Provides functions specific to BMI270.  
- `BMI270 imu`: Declares the BMI270 sensor object.

---

## I2C Address Configuration

```cpp
uint8_t i2cAddress = BMI2_I2C_PRIM_ADDR+1; // 0x68
```

- The sensor's default I2C address is `0x68`. The `+1` ensures it is explicitly set.

---

## Setup Function

```cpp
void setup() {
    Serial.begin(115200);
    Serial.println("BMI270 Example 1 - Basic Readings I2C");

    Wire.begin();

    while (imu.beginI2C(i2cAddress) != BMI2_OK) {
        Serial.println("Error: BMI270 not connected, check wiring and I2C address!");
        delay(1000);
    }

    Serial.println("BMI270 connected!");
}
```

**What it does:**  
- Starts serial communication at **115200 baud**.  
- Initializes the I2C bus with `Wire.begin()`.  
- Tries to initialize the sensor until successful.  
- Prints an error message every second until the sensor is detected.

---

## Loop Function

```cpp
void loop() {
    imu.getSensorData();
```

- Fetches the latest sensor readings. Must be called before accessing data fields.

---

## 📈 Acceleration Data Reading

```cpp
    Serial.print("Acceleration in g's\t");
    Serial.print("X: "); Serial.print(imu.data.accelX, 3);
    Serial.print("\tY: "); Serial.print(imu.data.accelY, 3);
    Serial.print("\tZ: "); Serial.print(imu.data.accelZ, 3);
```

- Reads acceleration in X, Y, Z axes.  
- Values in **g (gravitational units)**.  
- Printed with **3 decimal digits**.

---

## 🔄 Gyroscope Data Reading

```cpp
    Serial.print("\tRotation in deg/sec\t");
    Serial.print("X: "); Serial.print(imu.data.gyroX, 3);
    Serial.print("\tY: "); Serial.print(imu.data.gyroY, 3);
    Serial.print("\tZ: "); Serial.println(imu.data.gyroZ, 3);
```

- Reads rotation data in **degrees per second (°/s)**.  
- Values printed on the same line after acceleration.

---

## Sampling Rate

```cpp
    delay(20); // 50 Hz loop rate
}
```

- Adds a **20 ms delay** to achieve a sampling frequency of **50 Hz**.

---
