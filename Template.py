import RPi.GPIO as GPIO
import time

# Definición de pines GPIO
pulso = 23
intervalo = 24

# Configuración de pines
GPIO.setmode(GPIO.BCM)
GPIO.setup(pulso, GPIO.OUT)
GPIO.setup(intervalo, GPIO.OUT)

# Función para generar un pulso
def generar_pulso(duracion):
    GPIO.output(pulso, GPIO.HIGH)
    time.sleep(duracion / 1000)
    GPIO.output(pulso, GPIO.LOW)

# Función para generar un intervalo
def generar_intervalo():
    GPIO.output(intervalo, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(intervalo, GPIO.LOW)

# Diccionario con las duraciones de pulso
duraciones = {
    "25ms": 25,
    "45ms": 45,
    "65ms": 65,
    "100ms": 100
}

# Bucle principal
while True:
    # Ingreso del número
    numero = input("Ingrese un número (1-4): ")

    # Validación del número
    if not numero.isdigit() or int(numero) < 1 or int(numero) > 4:
        print("Número no válido. Ingrese un número entre 1 y 4.")
        continue

    # Generación de pulsos y intervalos
    for i in range(4):
        generar_pulso(duraciones[f"{numero}ms"])
        generar_intervalo()

# Limpieza de pines
GPIO.cleanup()
