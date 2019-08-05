# 知話輪サーバーと手元のBOTを繋げるngrok使用方法

## はじめに
ローカルマシンと知話輪サーバーを接続するための準備を行います。

<img width="400" src="https://user-images.githubusercontent.com/23329399/44826140-a1faef80-ac48-11e8-8abd-3a600be7265a.png">

- ngrokを使うとローカルマシンのポートと繋いでくれる
- webhookをローカルマシンで受けられる

## ngrokを実行する環境用意

#### 以下のURLより「ngrok」のファイルをダウンロード

https://ngrok.com/

#### この画面が出てきたなら自分のgithubやGoogleアカウントを使ってログイン

<img width="400" alt="2018-08-30 11 21 13" src="https://user-images.githubusercontent.com/23329399/44825753-03ba5a00-ac47-11e8-9e42-afd8f7b9c1d1.png">

#### ①Dwnload for 〇〇からngrokをダウンロード

<img width="400" alt="2018-08-30 11 23 59" src="https://user-images.githubusercontent.com/23329399/44825933-c99d8800-ac47-11e8-8dbf-c863045f3c04.png">


#### ダウンロードしたzipファイルを解凍し、ngrokを起動する

```
$ cd [ngrokをダウンロードしたディレクトリ]
$ unzip ngrok-stable-[OS情報].zip
$ ./ngrok http 5555
```

## 以下のような画面が出てきたならOK

<img width="400" alt="2018-08-29 15 30 52" src="https://user-images.githubusercontent.com/23329399/44769749-9227d080-aba0-11e8-8747-b681f76092d8.png">

- webhookの受け取り口を用意することができました。
