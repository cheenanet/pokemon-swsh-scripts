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

# サイクル20 = 30
# サイクル40 = 60
laps = 30

try:
    for i in range(0, 6): # 5匹孵化×6回
        start_time = time.time()

        for j in range(0, 5): # 1匹孵化×5
            lap_start_time = time.time()

            send('Button X', 0.1)
            sleep(1)

            send('Button A', 0.1)
            sleep(2.5)

            send('Button A', 0.1)
            sleep(0.5)

            send('Button A', 0.1)
            sleep(5)

            # タマゴもらう
            send('LY MAX', 0.7)
            send('LX MAX', 0.2)
            sleep(0.5)

            send('Button A', 0.1) # キミのポケモンが…
            sleep(0.5)

            send('Button A', 0.1) # 欲しいですよね
            sleep(0.5)

            send('Button A', 0.1) # はい
            sleep(3)

            send('Button A', 0.1) # 預け屋さんからタマゴをもらった
            sleep(3)

            send('Button A', 0.1) # 手持ちに加えました
            sleep(2)

            send('Button A', 0.1) # 大事に育ててね
            sleep(0.1)

            send('LY MIN', 3)
            sleep(0.1)

            send('LX MAX', 2)
            sleep(0.1)

            for lap in range(0, laps):
                print(f'{lap + 1}周目')

                send('LY MIN', 0.5)
                send('LX MIN', 0.5)
                send('LY MAX', 0.5)
                send('LX MAX', 0.5)

                send('Button B', 0.3)

            # ボタン押せるようになるまで待機
            for wait in range(0, 8):
                send('Button B', 0.1)
                sleep(1)

            print(f'{j + 1}匹孵化完了？：{round(time.time() - lap_start_time, 2)}秒経過（合計：{round(time.time() - start_time, 2)}秒）')

        for lap in range(0, laps):
            print(f'{lap + 1}周目')

            send('LY MIN', 0.5)
            send('LX MIN', 0.5)
            send('LY MAX', 0.5)
            send('LX MAX', 0.5)

            send('Button B', 0.3)

        # ボタン押せるようになるまで待機
        for wait in range(0, 8):
            send('Button B', 0.1)
            sleep(1)

        print(f'5匹孵化完了：{round(time.time() - start_time, 2)}秒経過')

        send('Button X', 0.1)
        sleep(1)

        send('LX MAX', 0.1)
        sleep(0.1)

        send('LY MIN', 0.1)
        sleep(0.1)

        send('Button A', 0.1) # ポケモン
        sleep(2)

        send('Button R', 0.1) # ボックスを開く
        sleep(2)

        send('LX MIN', 0.1)
        sleep(0.1)

        send('LY MAX', 0.1) # タマゴにカーソル
        sleep(0.1)

        send('Button Y', 0.1)
        sleep(0.1)

        send('Button Y', 0.1) # はんいモード
        sleep(0.1)

        send('Button A', 0.1)
        sleep(0.1)

        send('LY MAX', 0.1)
        sleep(0.1)

        send('LY MAX', 0.1)
        sleep(0.1)

        send('LY MAX', 0.1)
        sleep(0.1)

        send('LY MAX', 0.1)
        sleep(0.1)

        send('Button A', 0.1) # タマゴ全選択
        sleep(0.1)

        send('LX MAX', 0.1)
        sleep(0.1)

        send('LY MAX', 0.1)
        sleep(0.1)

        send('LY MAX', 0.1)
        sleep(0.1)

        send('LY MAX', 0.1)
        sleep(0.1)

        send('LY MAX', 0.1)
        sleep(0.1)

        send('Button A', 0.1) # いちらん
        sleep(0.5)

        send('Button A', 0.1) # ボックスに置く
        sleep(0.5)

        send('Button B', 0.1) # もどる
        sleep(0.1)

        send('Button B', 0.1) # もどる
        sleep(2)

        send('Button B', 0.1) # もどる
        sleep(1.5)

        send('LY MAX', 0.1)
        sleep(0.1)

        send('LX MIN', 0.1)
        sleep(0.1)

        send('Button B', 0.1) # もどる
        sleep(1.5)

except KeyboardInterrupt:
    send('RELEASE')
    ser.close()

