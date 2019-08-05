# 知話輪エコーBotを作ってみよう

## 事前準備
[Python環境の準備](../00_Python環境の準備)が完了している前提で話を進めます。

まず、任意の場所に作業用のディレクトリを作成してください。

```bash
$ mkdir chiwawa_echo_bot
$ cd chiwawa_echo_bot
```

### pipenvの仮想環境を準備
各種ライブラリをインストールします。  
(3系の違うバージョン利用する場合、実際のpythonバージョンに合わせてコマンドを修正してください)

```bash
$ pipenv install flask gunicorn python-dotenv requests --python=3.6
```

仮想環境を有効化します。

```bash
$ pipenv shell
```

仮想環境を終了する場合は以下のコマンドを実行します。

```bash
$ exit
```

`app.py`ファイルを作成し、Botプログラムを記述していきます。  
任意のエディターを用いてください。

```bash
$ vim app.py
```

## FlaskでHello, Worldサーバーを作成
`app.py`に以下のコードを記述します。

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

動かしてみましょう。

```bash
$ flask run
```

ブラウザで、http://127.0.0.1:5000/ にアクセスすると「Hello, World!」が表示されます。

本番環境ではgunicornで動かしたいので、gunicornでスクリプトを起動して確認する。

```bash
$ gunicorn -b :5555 app:app
```

同様に、http://127.0.0.1:5555/ にアクセスすると「Hello, World!」が表示されます。

## Botプログラムの作成

### .envの準備
環境設定ファイル「.env」を作成します。  
知話輪管理画面で発行した「APIトークン」「Webhook検証トークン」を記述してください。

```env
CHIWAWA_API_TOKEN=APIトークン
CHIWAWA_VALIDATION_TOKEN=Webhook検証トークン
```

### app.pyの拡張
Botに必要な情報を「app.py」に記述していきます。  

```python
import os
import json

from flask import Flask, request
from dotenv import load_dotenv
import requests

app = Flask(__name__)
load_dotenv('.env')
env = os.environ

# 先ほど作成した、Hello, world!
@app.route('/')
def hello_world():
    return 'Hello, World!'


# 知話輪サーバーからのWebhookを受け取るエンドポイント
@app.route('/message', methods=['POST'])
def messages():
    if is_request_valid(request):
        body = request.get_json(silent=True)
        companyId = body['companyId']
        msgObj = body['message']
        groupId = msgObj['groupId']
        messageText = msgObj['text']
        userName = msgObj['createdUserName']
        send_message(companyId, groupId, userName + 'さん、' + messageText)
        return "OK"
    else:
        return "request is not valid."

# 検証トークンを用いて、リクエスト送信元が正しいか検証する
def is_request_valid(request):
    validationToken = env['CHIWAWA_VALIDATION_TOKEN']
    requestToken = request.headers['X-Chiwawa-Webhook-Token']
    return validationToken == requestToken

# 知話輪APIを用いて、サーバにメッセージを送信する
def send_message(companyId, groupId, message):
    url = 'https://{0}.chiwawa.one/api/public/v1/groups/{1}/messages'.format(companyId, groupId)
    headers = {
        'Content-Type': 'application/json',
        'X-Chiwawa-API-Token': env['CHIWAWA_API_TOKEN']
    }
    content = {
        'text': message
    }
    requests.post(url, headers=headers, data=json.dumps(content))
```

### webhookを受け取るためngrokを使用

別のターミナル(コマンドプロンプト)でngrokを起動します。

```bash
$ cd path/to/ngrok
$ ./ngrok http 5555
ngrok by @inconshreveable                                                                                                                        (Ctrl+C to quit)

Session Status                online
Account                        (Plan: Free)
Update                        update available (version 2.3.34, Ctrl-U to update)
Version                       2.3.29
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://example.ngrok.io -> http://localhost:5555
Forwarding                    https://example.ngrok.io -> http://localhost:5555

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```

表示されたForwarding URLを控えておきましょう。  
上記出力の`https://example.ngrok.io`に該当します。

知話輪管理画面を開き、ログインします。  
先程登録したBotの「Webhook URL」の欄に「{ngrokのURL}/message}」
と入力して「変更する」をクリックしてください。

例：`https://example.ngrok.io/message`  
`/message`がWebhookを受け付けるパスなので、忘れずにつけましょう。

**注意：ngrok毎回起動する時URLが変わるため、知話輪管理画面でのURL修正が都度必要になります**

### gunicornを起動

```bash
$ gunicorn -b :5555 app:app
```

起動中の場合Ctl+Cで一回停止してから再起動します。

エコーボットの実装は以上で完了となります。

## 知話輪アプリから作成したBotにメッセージを投げてみる

Botと会話するためのグループを作成します。

1. 「知話輪」を開いて左メニュー「個人」の横にある「検索」をクリック
1. 検索方法「Bot名から検索」をクリック
1. ユーザーから作ったBOTを選択して個人用グループを作成

テキスト入力欄になにかメッセージを入力して投稿してみましょう！

1. 適当に話しかけてみる
1. Botが返事をしてくれれば成功です！
