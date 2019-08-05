# gremlinのクエリをpythonから呼び出す

## pythonからcosmosDBにgremlinのクエリを発行する

```chiwawa_client.py
from gremlin_python.driver import client, serializer

__query = "g.V().has('name', 'user1').out('follow').values('name')"

ENDPOINT = 'intern-2018'
DB_NAME = 'cww-database'
GRAPH_NAME = 'cww-graph'
PRIMARY_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'

# クライアントを生成
c = client.Client('wss://{}.gremlin.cosmosdb.azure.com:443/'.format(ENDPOINT), 'g',
                      username="/dbs/{0}/colls/{1}".format(DB_NAME, GRAPH_NAME),
                      password="{}".format(PRIMARY_KEY),
                      message_serializer=serializer.GraphSONSerializersV2d0()
                      )

# クエリを発行してcallbackを取得
callback = c.submitAsync(__query)

# コールバックが複数回に分かれて返ってくるので一つのリストにする
res = [i for it in callback.result() for i in it]

# あとはresの中身を文字列や画像に処理して知話輪に投稿する（以下参照）
```

## interactive shell with python
```python
from gremlin_python.driver import client, serializer
import pprint

#__query = "g.V().has('name', 'user1').out('follow').values('name')"
__query = 'g.V().hasLabel("user")'

ENDPOINT = 'intern-2018-fjmt'
DB_NAME = 'sample-database'
GRAPH_NAME = 'sample-graph'
PRIMARY_KEY = 'k0oZuYmygP4nr9XpgahGnBJiSxmICEIGNPoGO0nAiVJ3wSdb6bQcGuN29Ff43ix1xkiV1tPgFGaWXYiqvxbaOQ=='

# クライアントを生成
c = client.Client('wss://{}.gremlin.cosmosdb.azure.com:443/'.format(ENDPOINT), 'g',
                      username="/dbs/{0}/colls/{1}".format(DB_NAME, GRAPH_NAME),
                      password="{}".format(PRIMARY_KEY),
                      message_serializer=serializer.GraphSONSerializersV2d0()
                      )

while True:
    # クエリを発行してcallbackを取得
    callback = c.submitAsync(input())
        # コールバックが複数回に分かれて返ってくるので一つのリストにする
    res = [i for it in callback.result() for i in it]
    pprint.pprint(res)  # print prettify
```

## 参考
知話輪のAPIを叩くクライアントクラスの実装例

```python
import json
import os

import requests


# 基底例外クラス
class ChiwawaBaseException(Exception):
    pass


# Chiwawaサーバーから返ってきたエラーレスポンスをハンドリングする例外クラス
class ChiwawaResposeError(ChiwawaBaseException):
    def __init__(self, status_code, err_resp):
        super().__init__()
        self.status_code = status_code
        self.err_resp = err_resp

    def __str__(self):
        return json.dumps(self.err_resp)


# 知話輪クライアントクラス
class ChiwawaClient(object):
    def __init__(self, commpany_id, api_token, api_version='v1'):

        self.api_version = api_version
        self.commpany_id = commpany_id
        self.api_token = api_token
        self.base_url = \
            'http://{0}.chiwawa.one/api/public/{1}'.format(self.commpany_id,
                                                           self.api_version)

　　　　　　　　# レスポンスステータスコードをチェックして200OK以外は例外を送出する
    @staticmethod
    def _check_status_code(status_code, text):
        if status_code != 200:
            raise ChiwawaResposeError(status_code, json.loads(text))

    # メッセージ投稿
    def post_message(self, group_id, text, *,
                     to=None, from_=None, to_all=False, attachments=None):
        # The 'from' is a reserved word for python, so specify it with 'from_'.

        data = {
            'text': text
        }

        if to is not None:
            data['to'] = to

        if from_ is not None:
            data['from'] = from_

        if to_all is not False:
            data['toAll'] = str(to_all).lower()

        if attachments is not None:
            data['attachments'] = attachments

        url = '{0}/groups/{1}/messages'.format(self.base_url, group_id)
        headers = {
            'Content-Type': 'application/json',
            'X-Chiwawa-API-Token': self.api_token
        }
        resp = requests.post(url, headers=headers, data=json.dumps(data))
        self._check_status_code(resp.status_code, resp.text)

        return resp.json()

    # メッセージ一覧取得
    def get_message_list(self, group_id, *,
                         created_at_from=0, created_at_to=None,
                         max_results=20):

        params = {
            'createdAtFrom': created_at_from,
            'maxResults': max_results,
        }

        if created_at_from is not None:
            params['createdAtTo'] = created_at_to

        url = '{0}/groups/{1}/messages'.format(self.base_url, group_id)
        headers = {
            'Content-Type': 'application/json',
            'X-Chiwawa-API-Token': self.api_token
        }
        resp = requests.get(url, headers=headers, params=params)
        self._check_status_code(resp.status_code, resp.text)

        return resp.json()

    # メッセージ情報取得
    def get_message_info(self, group_id, message_id):

        url = '{0}/groups/{1}/messages/{2}'.format(self.base_url, group_id,
                                                   message_id)
        headers = {
            'Content-Type': 'application/json',
            'X-Chiwawa-API-Token': self.api_token
        }
        resp = requests.get(url, headers=headers)
        self._check_status_code(resp.status_code, resp.text)

        return resp.json()

    # メッセージ削除（できれば使わないで）
    def delete_message(self, group_id, message_id):

        url = '{0}/groups/{1}/messages/{2}'.format(self.base_url, group_id,
                                                   message_id)
        headers = {
            'Content-Type': 'application/json',
            'X-Chiwawa-API-Token': self.api_token
        }
        resp = requests.delete(url, headers=headers)
        self._check_status_code(resp.status_code, resp.text)

        return True

    # メッセージ付加情報変更
    def update_message_attachments(self, group_id, message_id, attachments):

        url = '{0}/groups/{1}/messages/{2}/attachments'.format(self.base_url,
                                                               group_id,
                                                               message_id)
        data = {'attachments': attachments}
        headers = {
            'Content-Type': 'application/json',
            'X-Chiwawa-API-Token': self.api_token
        }
        resp = requests.put(url, headers=headers, data=json.dumps(data))
        self._check_status_code(resp.status_code, resp.text)

        return resp.json()

    # ファイル情報取得
    # レスポンスに含まれるダウンロードURL(downloadUrl)は60秒間のみ有効
    def get_file_info(self, group_id, message_id):

        url = '{0}/groups/{1}/files/{2}'.format(self.base_url, group_id,
                                                message_id)
        headers = {
            'Content-Type': 'application/json',
            'X-Chiwawa-API-Token': self.api_token
        }
        resp = requests.get(url, headers=headers)
        self._check_status_code(resp.status_code, resp.text)

        return resp.json()

    # ファイル投稿
    def post_file(self, group_id, file_type, file_path, *, file_name=None):

        if file_name is None:
            file_name = os.path.basename(file_path)

        files = {'file': (file_name, open(file_path, 'rb'), file_type)}
        data = {'fileName': file_name}

        url = '{0}/groups/{1}/files'.format(self.base_url, group_id)
        headers = {
            'X-Chiwawa-API-Token': self.api_token
        }
        resp = requests.post(url, headers=headers, files=files, data=data)
        self._check_status_code(resp.status_code, resp.text)

        return resp.json()

    # グループ所属ユーザ一覧取得
    def get_group_user_list(self, group_id):

        url = '{0}/groups/{1}/users'.format(self.base_url, group_id)
        headers = {
            'Content-Type': 'application/json',
            'X-Chiwawa-API-Token': self.api_token
        }
        resp = requests.get(url, headers=headers)
        self._check_status_code(resp.status_code, resp.text)

        return resp.json()
```

このクラスを`import`して呼び出す
```python
# from .ファイル名（.pyを除く）でimportする
# .が頭に付いているのは明示的にカレントディレクトリのモジュールを指定する意味
# 同じファイル内からクラスを呼び出す際はもちろんimportは必要ない
from .chiwawa_client import ChiwawaClient

cc = ChiwawaClient(commpany_id, api_token)
gi = 'ZZZZZZZZZZZZZZZZZZZZ'

o = cc.post_message(group_id=gi, text='fuga', to_all=True)
print(o)

o = cc.post_file(group_id=gi, file_path='/path/to/file', file_type='image/jpg')
print(o)

msg_id = o['messageId']

o = cc.get_file_info(group_id=gi, message_id=msg_id)
print(o)

o = cc.get_message_info(group_id=gi, message_id=msg_id)
print(o)

o = cc.get_group_user_list(group_id=gi)
print(o)

o = cc.get_message_list(group_id=gi)
print(o)
```
