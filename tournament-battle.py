#!/usr/bin/env python3
import argparse
import serial
import time
from time import sleep
import datetime
import random

parser = argparse.ArgumentParser()
parser.add_argument('port')
parser.add_argument('--delay', type=int, default=10)
parser.add_argument('--fight-time', type=int, default=150)
parser.add_argument('--no-use-x-spatk', action='store_false')
parser.add_argument('--no-dynamax', action='store_false')
args = parser.parse_args()

# ダイマックスによる遅延を追加
fight_time = args.fight_time + (20 if args.no_dynamax == True else 0)

dt = datetime.datetime

def send(msg, duration=0):
    now = dt.now()
    print(f'[{now}] {msg}')
    ser.write(f'{msg}\r\n'.encode('utf-8'))
    sleep(duration)
    ser.write(b'RELEASE\r\n')

ser = serial.Serial(args.port, 9600)

# 遅延を入れる
print(f'{args.delay}秒の遅延を入れています…（--delayで指定可能）')
sleep(args.delay)
send('Button B', 0.1)

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
            print(f'第{i + 1}試合を開始')

            send('Button A', 0.1) # 勝負を　しかけてきた！
            sleep(22)

            # スペシャルアップを使う
            if not no_use_x_spatk:
                print('スペシャルアップを使用します')

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
                sleep(0.5)

            # ダイマックスする
            if not args.no_dynamax:
                print('ダイマックスします')

                send('Button A', 0.1)
                sleep(0.5)

                send('LX MIN', 0.1)
                sleep(0.1)

                send('Button A', 0.1)
                sleep(0.2)

                # ダイマックスわざ
                send('Button A', 0.1)
                sleep(0.1)

            fight_start_time = time.time()

            while True:
                if (time.time() - fight_start_time) > fight_time:
                    break

                send('Button A', 0.1)
                sleep(0.1)

                # 残り秒数
                if random.randrange(0, 5) == 0:
                    time_left = round(fight_time - (time.time() - fight_start_time), 2)
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
