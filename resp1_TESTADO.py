#Definindo a utilização da biblioteca GPIO
import RPi.GPIO as GPIO
#Importação da biblioteca time para utilizar temporizadores
import time
from datetime import datetime
#Aqui definimos que vamos usar o numero de ordem do pino, e não o numero que refere a porta
#Para usar o numero da porta, é preciso trocar a definição "GPIO.BOARD (ex. Pino 12)" para "GPIO.BCM (ex.GPIO 18)" 
#Definindo a pinagem real
GPIO.setmode(GPIO.BOARD)
#Definindo o pino a ser utilizado
pin_to_circuit = 12
try:
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    while(1):
        GPIO.output(pin_to_circuit,1)
        print("***LIGADO***")
        a=datetime.now().second
        print(str(a)) 
        time.sleep(0.250)
        GPIO.output(pin_to_circuit,0)
        print("---DESLIGADO---")
        time.sleep(0.250)
except KeyboardInterrupt:
    print ("Fim")
    pass
finally:
    GPIO.cleanup()
#Fonte: Raspberry pi Fundation
