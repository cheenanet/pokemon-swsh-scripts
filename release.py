#!/usr/bin/env python3
import argparse
import serial
import time
from time import sleep
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('port')
args = parser.parse_args()

datetime = datetime.datetime

def send(msg, duration=0):
    now = datetime.now()
    print(f'[{now}] {msg}')
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')

ser = serial.Serial(args.port, 9600)

rows = 5 # max 5
cols = 6 # max 6 

try:
    for row in range(0, rows):
        for col in range(0, cols):
            send('Button A', 0.1)
            sleep(0.3)

            send('LY MIN', 0.1)
            sleep(0.2)

            send('LY MIN', 0.1)
            sleep(0.1)

            send('Button A', 0.1)
            sleep(1)

            send('LY MIN', 0.1)
            sleep(0.1)

            send('Button A', 0.1)
            sleep(1.3)

            send('Button A', 0.1)
            sleep(0.1)

            send('LX MAX', 0.1)
            sleep(0.3)

        send('LX MAX', 0.1)
        sleep(0.1)

        send('LY MAX', 0.1)
        sleep(0.1)

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()