import machine
import time
import sys

LED = machine.Pin(25, machine.Pin.OUT)
GN = machine.Pin(28, machine.Pin.OUT)  # VERDE
YE = machine.Pin(27, machine.Pin.OUT)  # AMARILLO
RD = machine.Pin(26, machine.Pin.OUT)  # ROJO
BUZ = machine.Pin(22, machine.Pin.OUT) # BUZZER

LED.value(1)

while True:
    command = sys.stdin.readline().strip()
    if command == 'A':
        # encender FPY "Verde"
        GN.value(1)
        YE.value(0)
        RD.value(0)
        BUZ.value(0)
    
    elif command == 'B':
        # encender FPY "Amarillo"
        GN.value(0)
        YE.value(1)
        RD.value(0)
        BUZ.value(0)
        
    elif command == 'C':
        # encender FPY "Rojo"
        GN.value(0)
        YE.value(0)
        RD.value(1)
        BUZ.value(0)

        
    elif command == 'D':
        # Soporte ingenieria
        GN.value(0)
        YE.value(0)
        RD.value(1)
        BUZ.value(1)
        
    elif command == 'E':
        # Soporte calidad
        GN.value(0)
        YE.value(1)
        RD.value(1)
        BUZ.value(1)
        
    elif command == 'F':
        # Soporte producción
        GN.value(1)
        YE.value(0)
        RD.value(1)
        BUZ.value(1)
        
    elif command == 'G':
        # Soporte todos
        GN.value(1)
        YE.value(1)
        RD.value(1)
        BUZ.value(1)

    elif command == 'H':
        # Apagar todo
        GN.value(0)
        YE.value(0)
        RD.value(0)
        BUZ.value(0)
        
 
        