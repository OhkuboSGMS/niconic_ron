## niconico cron
エコノミー制限を回避して，ダウンロード

## 環境
RasberryPi3 のcrontabでの動作を想定

| name         | version |
|--------------|--------|
| python       | 3.6    |
| yt-dlp       | 2022.6.29 |
| pyinstaller  | 5.1    |
---------------------------

## Install
raspiにconda環境を準備
```shell
wget https://github.com/jjhelmus/berryconda/releases/download/v2.0.0/Berryconda3-2.0.0-Linux-armv7l.sh
bash Berryconda3-2.0.0-Linux-armv7l.sh
source 
```
## Build
`shell/build_raspi3.sh`

## 定期実行
 `crontab`に以下の命令を追記

```
01 2 * * * ~/bin/niconicron/main --flie_list  ~/list.txt
```
毎日02:01に ~/list.txtのファイルをダウンロード


#### Windows Build
`shell/build_win.bat`