# pokemon-swsh-autoplay
ポケットモンスター ソード・シールドにおけるキー入力の自動化を行うPythonスクリプト

## 必要条件
- USB搭載のマイクロコンピュータ（CPUに atmega16u2 or atmega32u4 を搭載したもの）
- USBシリアル変換アダプタ
- microUSBケーブル
- [ebith/Switch-Fightstick](https://github.com/ebith/Switch-Fightstick)

## 掲載内容
`/dev/ttyUSB0` は環境に応じて変更すること。Linuxでは `/dev/ttyUSB0` など。Windows Subsystem for Linux (WSL)の場合は `/dev/ttyS1` など（COMポートの番号に合わせる）。

- tournament-battle.py  
シュートスタジアムのトーナメント戦の自動化。[85-117行](https://github.com/cheenanet/pokemon-swsh-scripts/blob/e943c47136710ab6023f60bf92a971a5bb915431/tournament-battle.py#L85-L117)においてスペシャルアップ（シンボラー用、資料参照）を使用しているため、不要な場合は削除する。  
`python3 tournament-battle.py --fight_time 150 /dev/ttyUSB0`
    - `--fight_time`: 一試合の時間（秒）。長くかかる場合は増やす（デフォルト: 150）。
- egg-hatching.py  
タマゴ孵化の自動化。タマゴ5個の孵化を6回行います。ボックスを空にして閉じ、特性がほのおのからだのポケモンを手持ちに入れ、預け屋でタマゴができている状態で、Xボタンでメニューを表示し「マップ」にカーソルを合わせた上で実行する。  
`python3 egg-hatching.py --laps 20 /dev/ttyUSB0`
    - `--laps`: 自転車で周回する数。デフォルト: 20  
    孵化対象のポケモンのタマゴ歩数によってこの値を変更する（https://yakkun.com/swsh/zukan/ を参照）。40サイクルのポケモンはおよそ60周で誕生する。効率化のためこのスクリプトでは1/3の歩数を歩くと次のタマゴを受け取りにいき、タマゴ5匹を持つと残りの2/3を歩くようになっているため、60周では20周が適している。タマゴが見つかるまでの歩数を考慮し、少なくとも15周にするとよい。
- release.py  
ポケモン逃がしの自動化。ボックス内のポケモンをすべて逃がす。1列目から順番に逃がしているため、並びに空きがないようにすること。  
`python3 release.py --count 12 /dev/ttyUSB0`
    - `--count`: 逃がすポケモンの数。

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
