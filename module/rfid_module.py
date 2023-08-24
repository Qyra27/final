#!/usr/bin/env python

from mfrc522 import SimpleMFRC522
import time

reader = SimpleMFRC522()

def read_rfid():
        '''
        Fungsi ini berguna untuk membaca RFID,
        tag RFID yang terbaca akan dikembalikan / return
        '''
        id = reader.read()
        print(id)
        return id

def write_rfid(name):
         print("Now place your tag to write")
         reader.write(name)
         print(f"{name} Written")

# testing
#contoh penggunaan code
# write_rfid(name='Farid') #ini tu mau nulis Ilham
# #delay 3 detik
# time.sleep(3)

# try:
#         print(read_rfid())
# finally:
#         GPIO.cleanup()