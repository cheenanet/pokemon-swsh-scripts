#!/usr/bin/env python3
import argparse
import serial
import time
from time import sleep
import datetime
import random

parser = argparse.ArgumentParser()
parser.add_argument('port')
parser.add_argument('--fight_time', type=int, default=150)
args = parser.parse_args()

dt = datetime.datetime

def send(msg, duration=0):
    now = dt.now()
    print(f'[{now}] {msg}')
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')

ser = serial.Serial(args.port, 9600)

try:
    start_time = time.time()

    # トーナメント自動化

    for lap in range(0, 999):
        send('Button A', 0.2) # 話しかける
        sleep(1)

        send('Button A', 0.1) 
        sleep(0.5)

        send('Button A', 0.1) # はい
        sleep(1)

        send('Button A', 0.1) 
        sleep(0.5)

        send('Button A', 0.1) # いる
        sleep(0.5)

        send('Button A', 0.1)
        sleep(0.5)

        send('LY MAX', 0.1)
        sleep(0.1)

        send('LY MAX', 0.1) # ホップ
        sleep(0.1)

        for i in range(0, 13):
            send('Button A', 0.1)
            sleep(0.4)

        # 入場

        for i in range(0, 3):
            send('LY MIN', 3) # 入場する
            sleep(5)

            send('Button A', 0.1) # セリフ1
            sleep(1)

            send('Button A', 0.1) # セリフ2
            sleep(1)

            send('Button A', 0.1) # セリフ3
            sleep(15)

            # 勝負

            send('Button A', 0.1) # 勝負を　しかけてきた！
            sleep(22)

            # スペシャルアップを使う
            send('LY MAX', 0.1)
            sleep(0.1)

            send('LY MAX', 0.1)
            sleep(0.1)

            send('Button A', 0.1)
            sleep(1.5)

            send('LX MAX', 0.1)
            sleep(0.1)

            send('LX MAX', 0.1)
            sleep(0.1)

            send('LY MAX', 0.1)
            sleep(0.1)

            send('LY MAX', 0.1)
            sleep(0.1)

            send('Button A', 0.1)
            sleep(0.2)

            send('Button A', 0.1)
            sleep(12)

            send('LY MIN', 0.1)
            sleep(0.1)

            send('LY MIN', 0.1)
            sleep(0.1)

            fight_start_time = time.time()

            while True:
                if (time.time() - fight_start_time) > args.fight_time:
                    break

                send('Button A', 0.1)
                sleep(0.1)

                if random.randrange(2):
                    time_left = round(args.fight_time - (time.time() - fight_start_time), 2)
                    print(f'[{dt.now()}] 残り{time_left}秒')

            print('勝利')

        # 優勝
        print('優勝')

        # ボールガイ
        for i in range(0, 20):
            send('Button A', 0.1)
            sleep(1)

        send('LY MIN', 1) # 受付に突っ込む

        print(f'[{dt.now()}] {round(time.time() - start_time, 2)}秒経過（{lap}回目）')

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()
