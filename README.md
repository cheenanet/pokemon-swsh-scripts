# pokemon-swsh-autoplay
ポケットモンスター ソード・シールドにおけるキー入力の自動化を行うPythonスクリプト

## 必要条件
- USB搭載のマイクロコンピュータ（CPUに atmega16u2 or atmega32u4 を搭載したもの）
- USBシリアル変換アダプタ
- microUSB Type-Cケーブル（またはmicroUSB to Type-AケーブルとType-A to Type-Cアダプタ）
- [ebith/Switch-Fightstick](https://github.com/ebith/Switch-Fightstick)
- Python 3.6以上

## インストール
`/dev/ttyUSB0` は環境に応じて変更すること。Linuxでは `/dev/ttyUSB0` など。Windows Subsystem for Linux (WSL)の場合は `/dev/ttyS1` など（COMポートの番号に合わせる）。

```
# 必要なものをインストール
sudo apt install avrdude gcc-avr

# ebith/Switch-Fightstick をクローン
git clone --recursive https://github.com/ebith/Switch-Fightstick.git

# ディレクトリを移動
cd Switch-Fightstick

# ビルド
make

# バイナリを書き込むためにPro MicroをDFUモードにする必要がある。
# 基板のRSTとGNDをテストワイヤでつなげ、数秒以内に実行する。
# オプションの m32u4 はCPUが atmega32u4 の場合。atmega16u2 の場合は m16u2 にする。 
sudo avrdude -p m32u4 -c avr109 -D -P $(ls /dev/ttyUSB*) -b 57600 -U flash:w:Joystick.hex
```

インストール後は `Switch-Fightstick` ディレクトリを削除してもよい。

## 掲載内容
- tournament-battle.py  
シュートスタジアムのトーナメント戦の自動化。
使用方法:  
`python3 tournament-battle.py --fight_time 150 /dev/ttyUSB0`
    - `--fight-time [time]`: 一試合の時間（秒）。長くかかる場合は増やす（デフォルト: 150）。
    - `--use-x-spatk`: スペシャルアップを使う（デフォルト：使わない）。
    - `--use-dynamax`: 技リストの一番上をダイマックス技として使う（使うと試合時間が20秒プラスされる。デフォルト：使わない）。
- egg-hatching.py  
タマゴ孵化の自動化。タマゴ5個の孵化を6回行います。ボックスを空にして閉じ、特性がほのおのからだのポケモンを手持ちに入れ、預け屋でタマゴができている状態で、Xボタンでメニューを表示し「マップ」にカーソルを合わせた上で実行する。  
使用方法:  
`python3 egg-hatching.py --laps 20 /dev/ttyUSB0`
    - `--laps`: 自転車で周回する数。デフォルト: 20  
    孵化対象のポケモンのタマゴ歩数によってこの値を変更する（https://yakkun.com/swsh/zukan/ を参照）。40サイクルのポケモンはおよそ60周で誕生する。効率化のためこのスクリプトでは1/3の歩数を歩くと次のタマゴを受け取りにいき、タマゴ5匹を持つと残りの2/3を歩くようになっているため、60周では20周が適している。タマゴが見つかるまでの歩数を考慮し、少なくとも15周にするとよい。
- release.py  
ポケモン逃がしの自動化。ボックス内のポケモンをすべて逃がす。1列目から順番に逃がしているため、並びに空きがないようにすること。  
使用方法:  
`python3 release.py --count 12 /dev/ttyUSB0`
    - `--count [count]`: 逃がすポケモンの数。

## バグ報告等
- Issues（GitHubのアカウント必要）: https://github.com/cheenanet/pokemon-swsh-scripts/issues
- Twitter: [@cheenanet](https://twitter.com/cheenanet)
- Email: cheena@cheena.net

## 資料
「ポケットモンスター ソード・シールド」におけるポケモンのタマゴ孵化や「かえんだま」入手作業を自動化する – 無能ブログ  
https://blog.cheena.net/2533

NintendoSwitchをPCから操作する - おいら屋ファクトリー  
https://blog.feelmy.net/control-nintendo-switch-from-computer/

## ライセンス
[MITライセンス](https://github.com/cheenanet/pokemon-swsh-scripts/blob/master/LICENSE)
