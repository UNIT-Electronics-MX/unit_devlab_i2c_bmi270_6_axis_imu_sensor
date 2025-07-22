#!/usr/bin/env python3
"""
BMI270 MicroPython - Ejemplo Principal
Uso de la biblioteca micropython_bmi270 oficial

Conexiones típicas:
- VCC: 3.3V
- GND: GND
- SCL: Pin 22 (configurable)
- SDA: Pin 21 (configurable)  
- SDO: GND para dirección 0x68, VCC para 0x69
"""

import time
from machine import I2C, Pin

# Importar la biblioteca micropython_bmi270
try:
    from micropython_bmi270.bmi270 import (
        BMI270, 
        ACCELERATOR_ENABLED, ACCELERATOR_DISABLED,
        ACCEL_RANGE_2G, ACCEL_RANGE_4G, ACCEL_RANGE_8G, ACCEL_RANGE_16G,
        GYRO_RANGE_125, GYRO_RANGE_250, GYRO_RANGE_500, GYRO_RANGE_1000, GYRO_RANGE_2000
    )
    print("✅ Biblioteca micropython_bmi270 cargada correctamente")
except ImportError as e:
    print(f"❌ Error importando micropython_bmi270: {e}")
    print("📋 Soluciones:")
    print("   1. Asegúrate de que la biblioteca esté en /lib/micropython_bmi270/")
    print("   2. Usa los scripts de upload para instalar la biblioteca")
    print("   3. Verifica que todos los archivos estén presentes")
    exit()

def main():
    """Función principal del ejemplo usando micropython_bmi270"""
    
    # Configuración de pines I2C
    SCL_PIN = 22
    SDA_PIN = 21
    I2C_FREQ = 400000  # 400kHz (puedes reducir a 100000 si hay problemas)
    
    print("🚀 BMI270 MicroPython - Biblioteca Oficial")
    print("=" * 45)
    print(f"📍 Configuración:")
    print(f"   SCL Pin: {SCL_PIN}")
    print(f"   SDA Pin: {SDA_PIN}")
    print(f"   I2C Freq: {I2C_FREQ} Hz")
    print()
    
    try:
        # Crear objeto I2C
        i2c = I2C(0, scl=Pin(SCL_PIN), sda=Pin(SDA_PIN), freq=I2C_FREQ)
        
        # Escanear dispositivos I2C
        print("🔍 Escaneando bus I2C...")
        devices = i2c.scan()
        print(f"   Dispositivos encontrados: {[hex(addr) for addr in devices]}")
        
        # Determinar dirección del BMI270
        bmi270_addr = None
        if 0x69 in devices:
            bmi270_addr = 0x69
            print(f"   📍 BMI270 encontrado en 0x69 (SDO = VCC)")
        elif 0x68 in devices:
            bmi270_addr = 0x68
            print(f"   📍 BMI270 encontrado en 0x68 (SDO = GND)")
        else:
            print("   ❌ BMI270 no detectado")
            print("   💡 Verifica las conexiones:")
            print("      - VCC a 3.3V")
            print("      - GND a GND")
            print("      - SCL a Pin 22")
            print("      - SDA a Pin 21")
            return
        
        # Crear instancia del sensor
        print(f"\n🔧 Inicializando BMI270 en 0x{bmi270_addr:02X}...")
        bmi = BMI270(i2c, bmi270_addr)
        
        # Configurar el sensor
        print("⚙️  Configurando sensor...")
        
        # Habilitar acelerómetro
        bmi.acceleration_operation_mode = ACCELERATOR_ENABLED
        
        # Configurar rangos
        bmi.acceleration_range = ACCEL_RANGE_2G      # ±2g
        bmi.gyro_range = GYRO_RANGE_1000             # ±1000 dps
        
        print(f"   📊 Configuración aplicada:")
        print(f"      Acelerómetro: {bmi.acceleration_range}")
        print(f"      Giroscopio: {bmi.gyro_range}")
        print(f"      Modo ACC: {bmi.acceleration_operation_mode}")
        
        # Pequeña pausa para estabilización
        time.sleep(0.5)
        print("\n🎯 Sensor listo para lectura!")
        
        # Leer datos del sensor en bucle
        print("\n📡 Iniciando lectura de datos (Ctrl+C para parar)...")
        print("Formato: Acelerómetro (g) | Giroscopio (dps)")
        print("-" * 65)
        
        count = 0
        while True:
            try:
                # Leer acelerómetro (tupla de 3 valores en g)
                acc_x, acc_y, acc_z = bmi.acceleration
                
                # Leer giroscopio (tupla de 3 valores en dps) 
                gyr_x, gyr_y, gyr_z = bmi.gyro
                
                # Mostrar datos formateados
                print(f"#{count:04d} | "
                      f"ACC: X:{acc_x:6.3f} Y:{acc_y:6.3f} Z:{acc_z:6.3f} g | "
                      f"GYR: X:{gyr_x:7.1f} Y:{gyr_y:7.1f} Z:{gyr_z:7.1f} dps")
                
                count += 1
                time.sleep(0.1)  # Leer cada 100ms (10 Hz)
                
            except KeyboardInterrupt:
                print("\n🛑 Deteniendo lectura de datos...")
                break
            except Exception as e:
                print(f"\n❌ Error inesperado: {e}")
                print("💡 Intentando continuar...")
                time.sleep(1)
        
        print("✅ Ejemplo finalizado correctamente.")
        
    except Exception as e:
        print(f"💥 Error crítico: {e}")
        print("\n🔧 Soluciones posibles:")
        print("   1. Verifica las conexiones físicas")
        print("   2. Reduce la frecuencia I2C a 100000 Hz")
        print("   3. Verifica que el BMI270 esté alimentado a 3.3V")
        print("   4. Asegúrate de que la biblioteca esté instalada correctamente")

def quick_test():
    """Test rápido para verificar funcionamiento"""
    
    print("⚡ BMI270 Quick Test")
    print("=" * 20)
    
    try:
        # Configuración básica
        i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=100000)  # Frecuencia más baja
        
        # Escanear
        devices = i2c.scan()
        print(f"Dispositivos I2C: {[hex(addr) for addr in devices]}")
        
        # Buscar BMI270
        addr = 0x69 if 0x69 in devices else (0x68 if 0x68 in devices else None)
        
        if addr is None:
            print("❌ BMI270 no encontrado")
            return False
        
        print(f"✅ BMI270 encontrado en 0x{addr:02X}")
        
        # Crear sensor
        bmi = BMI270(i2c, addr)
        
        # Configurar
        bmi.acceleration_operation_mode = ACCELERATOR_ENABLED
        bmi.acceleration_range = ACCEL_RANGE_2G
        bmi.gyro_range = GYRO_RANGE_1000
        
        # Una lectura de prueba
        acc = bmi.acceleration
        gyr = bmi.gyro
        
        print(f"📊 Datos de prueba:")
        print(f"   ACC: X:{acc[0]:6.3f} Y:{acc[1]:6.3f} Z:{acc[2]:6.3f} g")
        print(f"   GYR: X:{gyr[0]:7.1f} Y:{gyr[1]:7.1f} Z:{gyr[2]:7.1f} dps")
        print("🎉 BMI270 funcionando correctamente!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def streaming_example():
    """Ejemplo de streaming de datos en formato CSV"""
    
    print("📡 BMI270 Streaming de Datos CSV")
    print("=" * 35)
    
    try:
        # Configurar
        i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
        devices = i2c.scan()
        addr = 0x69 if 0x69 in devices else (0x68 if 0x68 in devices else None)
        
        if addr is None:
            print("❌ BMI270 no encontrado")
            return
        
        bmi = BMI270(i2c, addr)
        bmi.acceleration_operation_mode = ACCELERATOR_ENABLED
        bmi.acceleration_range = ACCEL_RANGE_4G  # ±4g para mayor rango
        bmi.gyro_range = GYRO_RANGE_1000
        
        print("⚙️  Configuración: ±4g, ±1000dps")
        print("📊 Formato CSV: acc_x,acc_y,acc_z,gyr_x,gyr_y,gyr_z")
        print("🔄 Frecuencia: 20 Hz")
        print("🛑 Presiona Ctrl+C para detener\n")
        
        # Header CSV
        print("acc_x,acc_y,acc_z,gyr_x,gyr_y,gyr_z")
        
        while True:
            acc_x, acc_y, acc_z = bmi.acceleration
            gyr_x, gyr_y, gyr_z = bmi.gyro
            
            print(f"{acc_x:.3f},{acc_y:.3f},{acc_z:.3f},"
                  f"{gyr_x:.1f},{gyr_y:.1f},{gyr_z:.1f}")
            
            time.sleep(0.05)  # 20 Hz
    
    except KeyboardInterrupt:
        print("\n🛑 Streaming detenido")
    except Exception as e:
        print(f"❌ Error: {e}")

def configuration_example():
    """Ejemplo de diferentes configuraciones del sensor"""
    
    print("🎛️  BMI270 - Configuraciones Diferentes")
    print("=" * 40)
    
    try:
        # Setup básico
        i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
        devices = i2c.scan()
        addr = 0x69 if 0x69 in devices else (0x68 if 0x68 in devices else None)
        
        if addr is None:
            print("❌ BMI270 no encontrado")
            return
        
        bmi = BMI270(i2c, addr)
        bmi.acceleration_operation_mode = ACCELERATOR_ENABLED
        
        # Configuraciones a probar
        configs = [
            {"acc_range": ACCEL_RANGE_2G, "gyr_range": GYRO_RANGE_250, "name": "±2g, ±250dps (Precisión)"},
            {"acc_range": ACCEL_RANGE_4G, "gyr_range": GYRO_RANGE_500, "name": "±4g, ±500dps (Balanceado)"},
            {"acc_range": ACCEL_RANGE_8G, "gyr_range": GYRO_RANGE_1000, "name": "±8g, ±1000dps (Deportivo)"},
            {"acc_range": ACCEL_RANGE_16G, "gyr_range": GYRO_RANGE_2000, "name": "±16g, ±2000dps (Extremo)"}
        ]
        
        for i, config in enumerate(configs):
            print(f"\n🔧 Configuración {i+1}: {config['name']}")
            
            # Aplicar configuración
            bmi.acceleration_range = config['acc_range']
            bmi.gyro_range = config['gyr_range']
            
            time.sleep(0.2)  # Tiempo para aplicar configuración
            
            # Tomar 3 muestras
            for sample in range(3):
                acc = bmi.acceleration
                gyr = bmi.gyro
                print(f"   Muestra {sample+1}: ACC[{acc[0]:6.3f}, {acc[1]:6.3f}, {acc[2]:6.3f}] "
                      f"GYR[{gyr[0]:7.1f}, {gyr[1]:7.1f}, {gyr[2]:7.1f}]")
                time.sleep(0.2)
        
        print("\n✅ Prueba de configuraciones completada")
        
    except Exception as e:
        print(f"❌ Error: {e}")

# Menú de opciones
def show_menu():
    """Mostrar menú de opciones"""
    print("\n📋 BMI270 MicroPython - Menú de Ejemplos")
    print("=" * 40)
    print("1. 🚀 Ejemplo principal (lectura continua)")
    print("2. ⚡ Test rápido")
    print("3. 📡 Streaming CSV")
    print("4. 🎛️  Prueba de configuraciones")
    print("0. 🚪 Salir")
    print()

if __name__ == "__main__":
    # Si se ejecuta desde la línea de comandos
    import sys
    
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg == "quick":
            quick_test()
        elif arg == "stream":
            streaming_example()
        elif arg == "config":
            configuration_example()
        elif arg == "menu":
            while True:
                show_menu()
                try:
                    choice = input("Selecciona opción: ")
                    if choice == "1":
                        main()
                    elif choice == "2":
                        quick_test()
                    elif choice == "3":
                        streaming_example()
                    elif choice == "4":
                        configuration_example()
                    elif choice == "0":
                        print("👋 ¡Hasta luego!")
                        break
                    else:
                        print("❌ Opción inválida")
                except KeyboardInterrupt:
                    print("\n👋 ¡Hasta luego!")
                    break
        else:
            print("Opciones disponibles:")
            print("  python ejemplo_bmi270.py        - Ejemplo principal")
            print("  python ejemplo_bmi270.py quick  - Test rápido")
            print("  python ejemplo_bmi270.py stream - Streaming CSV")
            print("  python ejemplo_bmi270.py config - Prueba configuraciones")
            print("  python ejemplo_bmi270.py menu   - Menú interactivo")
    else:
        # Ejecutar ejemplo principal por defecto
        main()
