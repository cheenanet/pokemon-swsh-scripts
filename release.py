#!/usr/bin/env python3
import argparse
import serial
import time
from time import sleep
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('port')
parser.add_argument('--rows', type=int)
parser.add_argument('--cols', type=int)
args = parser.parse_args()

ser = serial.Serial(args.port, 9600)

try:
    for row in range(0, args.rows):
        for col in range(0, args.cols):
            send('Button A', 0.1)
            sleep(0.3)

            send('LY MIN', 0.1)
            sleep(0.2)

            send('LY MIN', 0.1)
            sleep(0.1)

            send('Button A', 0.1) # にがす
            sleep(1)

            send('LY MIN', 0.1)
            sleep(0.1)

            send('Button A', 0.1)
            sleep(1.4)

            send('Button A', 0.1)
            sleep(0.1)

            send('LX MAX', 0.1) # 次へ
            sleep(0.3)

        send('LX MAX', 0.1) # てもちへ
        sleep(0.1)

        send('LY MAX', 0.1) # 下の行へ
        sleep(0.1)

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()

def send(msg, duration=0):
    now = datetime.datetime.now()
    print(f'[{now}] {msg}')
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')
