
import time
import threading

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(14,GPIO.OUT)

from module import rfid_module 
from module import web

'''
    membaca rfid, jika terbaca RFID lampu hijau menyala 0.5 detik
    lalu akan update dta di web, berupa waktu saat tap, jika pagi, dianggap masuk
    jika sore dianggap pulang.

    loop:
        - baca rfid
        - jika terdetksi rfid, lampu menyala dan mengetahui itu rfid siapa
        - update data di web
'''

def loop_baca_rfid(_):
    while(1):
        id, nama = rfid_module.read_rfid()
        print(id, nama)
        web.time_writer(id)

        # menyalakan led selama 0.5 detik
        GPIO.output(14,GPIO.HIGH)
        time.sleep(0.5)
        #mematikan led
        GPIO.output(14,GPIO.LOW)

# bikin thread untuk membaca RFID agar bisa loop terus
rfid_thread = threading.Thread(target=loop_baca_rfid, args=(1,))
rfid_thread.start()
print("rfid start")

if __name__ == "__main__":
    web.app.run()
