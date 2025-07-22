#!/usr/bin/env python3
"""
BMI270 MicroPython - Ejemplo Simple
Test básico para verificar que la biblioteca funciona
"""

import time
from machine import I2C, Pin

def test_bmi270_simple():
    """Test simple del BMI270"""
    
    print("🧪 BMI270 Test Simple")
    print("=" * 22)
    
    try:
        # Importar biblioteca
        from micropython_bmi270.bmi270 import BMI270, ACCELERATOR_ENABLED, ACCEL_RANGE_2G, GYRO_RANGE_1000
        print("✅ Biblioteca importada correctamente")
        
        # Configurar I2C
        i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)
        print("✅ I2C configurado")
        
        # Escanear dispositivos
        devices = i2c.scan()
        print(f"📍 Dispositivos I2C: {[hex(addr) for addr in devices]}")
        
        # Buscar BMI270
        addr = None
        if 0x69 in devices:
            addr = 0x69
        elif 0x68 in devices:
            addr = 0x68
        
        if addr is None:
            print("❌ BMI270 no encontrado")
            print("💡 Verifica las conexiones:")
            print("   VCC → 3.3V")
            print("   GND → GND") 
            print("   SCL → Pin 22")
            print("   SDA → Pin 21")
            return False
        
        print(f"✅ BMI270 encontrado en 0x{addr:02X}")
        
        # Crear instancia
        bmi = BMI270(i2c, addr)
        print("✅ Sensor inicializado")
        
        # Configurar
        bmi.acceleration_operation_mode = ACCELERATOR_ENABLED
        bmi.acceleration_range = ACCEL_RANGE_2G
        bmi.gyro_range = GYRO_RANGE_1000
        print("✅ Configuración aplicada")
        
        # Esperar estabilización
        time.sleep(0.5)
        
        # Realizar 5 lecturas de prueba
        print("\n📊 Realizando 5 lecturas de prueba:")
        for i in range(5):
            acc_x, acc_y, acc_z = bmi.acceleration
            gyr_x, gyr_y, gyr_z = bmi.gyro
            
            print(f"  {i+1}. ACC: [{acc_x:6.3f}, {acc_y:6.3f}, {acc_z:6.3f}] g")
            print(f"     GYR: [{gyr_x:7.1f}, {gyr_y:7.1f}, {gyr_z:7.1f}] dps")
            
            time.sleep(0.5)
        
        print("\n🎉 ¡BMI270 funcionando correctamente!")
        return True
        
    except ImportError as e:
        print(f"❌ Error de importación: {e}")
        print("💡 Asegúrate de que micropython_bmi270 esté en /lib/")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_bmi270_simple()
