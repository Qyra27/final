# menyalakan dan menghidupkan LED
# dikerjain sendiri
import RPi.GPIO as GPIO
import time
# GPIO.setmode(GPIO.BCM) # sudah di set di rfid
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)

# bikin fungsi untuk menyalakan dan mematikan lampu

def lampu(state) :
        '''
        jika state == 1 maka lampu nyala\n
        jika state == 0 maka lampu mati
        '''
        
        if state == 1 :
                GPIO.output(14,GPIO.HIGH)
        else :
                GPIO.output(14,GPIO.LOW)

# Testing --> Testing itu seolah-olah jalan di main
# lampu(1) #lampu nyala
# time.delay(1) # delay 1 detik
# lampu(0) # lampu mati
