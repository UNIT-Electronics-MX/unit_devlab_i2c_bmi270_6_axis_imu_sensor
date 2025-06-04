---
title: "UNIT BMI270 Module"
version: "1.0"
modified: "2025-05-08"
output: "unit_bmi270_module.pdf"
subtitle: "6-axix Inertial Sensor Module with I2C/SPI Interface and Low Power Design"
---

<!--
# README_TEMPLATE.md
Este archivo sirve como entrada para generar un PDF técnico estilo datasheet.
Edita las secciones respetando el orden, sin eliminar los encabezados.
-->
 <!-- logo -->

# UNIT BMI270 Module

![product](images/top.png)

## Introduction

The UNIT BMI270 is a 6-axis inertial measurement module that integrates a 3-axis accelerometer and a 3-axis gyroscope. Designed for low power consumption and high performance, it provides motion and gesture detection capabilities for embedded systems. The module supports I2C and SPI interfaces and includes configurable interrupts for advanced motion detection applications.

## Functional Description

The BMI270 sensor module combines a 16-bit accelerometer and a 16-bit gyroscope to deliver precise measurements of linear acceleration and angular velocity. It is highly suitable for applications requiring accurate motion tracking. The module allows flexible communication with microcontrollers via selectable I2C or SPI interfaces. Auxiliary and interrupt pins are available for gesture, activity, or tap detection, enhancing its integration in wearables, robotics, and interactive systems.

## Electrical Characteristics & Signal Overview

- Operating voltage: 3.3V (typical)
- Communication interfaces: I2C (up to 1 MHz), SPI (up to 10 MHz)
- Accelerometer range: ±2g / ±4g / ±8g / ±16g
- Gyroscope range: ±125°/s to ±2000°/s
- Low current consumption: ~850 μA in full operation
- Interrupt output: Active-low, open-drain
- Logic level: 3.3V compatible

## Applications

- Activity monitoring and fitness tracking
- Gesture detection and wake-on-motion
- Game controller orientation sensing
- Package motion and shock detection
- Navigation support in mobile robotics
- Smart home device triggering via motion

## Features

- 6-axis motion sensing (accelerometer + gyroscope)
- Low power consumption suitable for battery-powered applications
- Selectable I2C or SPI digital communication
- 16-bit resolution for both sensors
- Configurable motion and gesture interrupts
- Auxiliary pins for extended functionality
- Compact form factor for space-limited designs

## Pin & Connector Layout

| PIN     | Description                   |
|---------|-------------------------------|
| VCC     | MCU logic voltage (3.3V)      |
| GND     | Ground                        |
| SDA     | I2C data line                 |
| SCL     | I2C clock line                |
| SDO     | SPI MISO / I2C address select |
| CS      | SPI chip select               |
| INT1    | Interrupt output 1            |
| INT2    | Interrupt output 2            |

## Settings

### Interface Overview

| Interface  | Signals / Pins        | Typical Use                             |
|------------|-----------------------|-----------------------------------------|
| I2C        | SDA, SCL, SDO         | Standard I2C communication              |
| SPI        | SCK, MOSI, MISO, CS   | High-speed SPI communication            |
| Interrupts | INT1, INT2            | Motion detection, tap, activity alerts  |

### Supports

| Symbol | I/O   | Description                          |
|--------|-------|--------------------------------------|
| SDA    | I/O   | I2C serial data                      |
| SCL    | I     | I2C serial clock                     |
| CS     | I     | SPI chip select (active low)         |
| SDO    | I/O   | SPI MISO / I2C address configuration |
| INT1   | O     | Interrupt output for motion events   |
| INT2   | O     | Additional interrupt output          |

## Block Diagram

![Function Diagram](./images/pinout.png)

## Dimensions

![Dimensions](./images/dimension.png)

## Usage

Works with:

- Arduino and ESP32 boards (via I2C/SPI)
- STM32, RP2040, and other ARM-based MCUs
- MicroPython and C/C++ SDKs
- Gesture recognition libraries
- Inertial navigation algorithms

## Downloads

- [Schematic PDF](../hardware/unit_sch_V_0_0_1_ue0068_bmi270.pdf)

## Purchase

- [Buy from UNIT Electronics](https://www.uelectronics.com)
