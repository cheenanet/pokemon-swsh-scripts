# pokemon-swsh-autoplay
ポケットモンスター ソード・シールドにおけるキー入力の自動化を行うPythonスクリプト

## 必要条件
- USB搭載のマイクロコンピュータ（CPUに atmega16u2 or atmega32u4 を搭載したもの）
- USBシリアル変換アダプタ
- microUSBケーブル
- [ebith/Switch-Fightstick](https://github.com/ebith/Switch-Fightstick)

## 掲載内容
- tournament-battle.py  
シュートスタジアムのトーナメント戦の自動化。[85-117行](https://github.com/cheenanet/pokemon-swsh-scripts/blob/e943c47136710ab6023f60bf92a971a5bb915431/tournament-battle.py#L85-L117)においてスペシャルアップ（シンボラー用、資料参照）を使用しているため、不要な場合は削除してください。
- egg-hatching.py  
タマゴ孵化の自動化。タマゴ5個の孵化を6回行います。ボックスを空にして閉じ、特性がほのおのからだのポケモンを手持ちに入れ、預け屋でタマゴができている状態で、Xボタンでメニューを表示し「マップ」にカーソルを合わせた上で実行してください。
- release.py  
ポケモン逃がしの自動化。 ボックス内のポケモンをすべて逃がします。 `rows` は列 `cols` は行です。デフォルトでそれぞれ5、6（＝30匹）となっているので適時変更してください。

## 資料
「ポケットモンスター ソード・シールド」におけるポケモンのタマゴ孵化や「かえんだま」入手作業を自動化する – 無能ブログ  
https://blog.cheena.net/2533

NintendoSwitchをPCから操作する - おいら屋ファクトリー  
https://blog.feelmy.net/control-nintendo-switch-from-computer/
