#!/usr/bin/env python3
import argparse
import serial
import time
from time import sleep
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('port')
parser.add_argument('--count', type=int)
args = parser.parse_args()

def send(msg, duration=0):
    now = datetime.datetime.now()
    print(f'[{now}] {msg}')
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')

ser = serial.Serial(args.port, 9600)

try:
    for i in range(1, args.count):
        print(f'{i}匹目')

        send('Button A', 0.1)
        sleep(0.2)

        send('LY MIN', 0.1)
        sleep(0.1)

        send('LY MIN', 0.1)
        sleep(0.1)

        send('Button A', 0.1) # にがす
        sleep(1)

        send('LY MIN', 0.1)
        sleep(0.1)

        send('Button A', 0.1)
        sleep(1.4)

        send('Button A', 0.1)
        sleep(0.2)

        send('LX MAX', 0.1) # 次へ
        sleep(0.2)

        if i % 6 == 0:
            send('LX MAX', 0.1) # てもちへ
            sleep(0.1)

            send('LY MAX', 0.1) # 下の行へ
            sleep(0.1)

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
