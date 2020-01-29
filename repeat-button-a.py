#!/usr/bin/env python3
import argparse
import serial
import time
from time import sleep
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('port')
#parser.add_argument('--delay', type=int, default=10)
args = parser.parse_args()

def send(msg, duration=0):
    now = datetime.datetime.now()
    print(f'[{now}] {msg}')
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')

ser = serial.Serial(args.port, 9600)

try:
    while True:
        send('Button A', 0.1)
        sleep(0.2)

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
