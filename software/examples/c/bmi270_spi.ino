#include <SPI.h>
#include "BMI270.h"

#define PIN_SCLK  18   // scl
#define PIN_MISO  19   // sdo
#define PIN_MOSI  23   // sda
#define PIN_CS     5   // cs

static BMI270 imu(PIN_CS);

// Escalas típicas (ajustables)
constexpr float ACCEL_SCALE = 1.0f / 2048.0f;  // LSB/g
constexpr float GYRO_SCALE  = 1.0f / 16.4f;    // LSB/°/s

void setup() {
    Serial.begin(115200);
    SPI.begin(PIN_SCLK, PIN_MISO, PIN_MOSI, PIN_CS);
    imu.begin();
    Serial.println(F("{\"status\": \"BMI270 initialized\"}"));
}

void loop() {
    imu.readSensor();

    // Valores crudos
    int16_t ax_raw = imu.getRawAccelX();
    int16_t ay_raw = imu.getRawAccelY();
    int16_t az_raw = imu.getRawAccelZ();
    int16_t gx_raw = imu.getRawGyroX();
    int16_t gy_raw = imu.getRawGyroY();
    int16_t gz_raw = imu.getRawGyroZ();

    // Conversión
    float ax_g = ax_raw * ACCEL_SCALE;
    float ay_g = ay_raw * ACCEL_SCALE;
    float az_g = az_raw * ACCEL_SCALE;
    float gx_dps = gx_raw * GYRO_SCALE;
    float gy_dps = gy_raw * GYRO_SCALE;
    float gz_dps = gz_raw * GYRO_SCALE;

    // Imprimir en formato JSON
    Serial.print(F("{\"accel\":{"));
    Serial.printf("\"x\":%.3f,\"y\":%.3f,\"z\":%.3f},", ax_g, ay_g, az_g);
    Serial.print(F("\"gyro\":{"));
    Serial.printf("\"x\":%.2f,\"y\":%.2f,\"z\":%.2f}", gx_dps, gy_dps, gz_dps);
    Serial.println("}");

    delay(200);
}
