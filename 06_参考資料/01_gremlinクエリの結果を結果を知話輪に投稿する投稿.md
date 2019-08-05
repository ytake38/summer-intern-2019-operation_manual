# gremlinクエリの結果を知話輪に投稿する

```python
import os
import json

import requests
from flask import Flask, request
from gremlin_python.driver import client, serializer
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv('.env')
env = os.environ

# グループに所属するユーザー一覧を取得するクエリ
__query = "g.V().has('label', 'group').count()"


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/message', methods=['POST'])
def messages():
    if is_request_valid():
        body = request.get_json(silent=True)
        company_id = body['companyId']
        msg_obj = body['message']
        group_id = msg_obj['groupId']
        message_text = msg_obj['text']
        user_name = msg_obj['createdUserName']
        if message_text.find('hoge') >= 0:
            msg_to_return = access_to_graph_db()
            send_message(company_id, group_id, user_name + msg_to_return)
            return "OK"
        else:
            send_message(company_id, group_id, user_name + message_text)
            return "hoge does not exist"
    else:
        return "Request is not valid."


# Check if token is valid.
def is_request_valid():
    validation_token = env['CHIWAWA_VALIDATION_TOKEN']
    request_token = request.headers['X-Chiwawa-Webhook-Token']
    return validation_token == request_token


# Send message to Chiwawa server
def send_message(company_id, group_id, message):
    url = 'https://{0}.chiwawa.one/api/public/v1/groups/{1}/messages'.format(company_id, group_id)
    headers = {
        'Content-Type': 'application/json',
        'X-Chiwawa-API-Token': env['CHIWAWA_API_TOKEN']
    }
    content = {
        'text': message
    }
    requests.post(url, headers=headers, data=json.dumps(content))


def access_to_graph_db():
    c = client.Client('wss://{}.gremlin.cosmosdb.azure.com:443/'.format(env['ENDPOINT']), 'g',
                      username="/dbs/{0}/colls/{1}".format(env['DB_NAME'], env['GRAPH_NAME']),
                      password="{}".format(env['PRIMARY_KEY']),
                      message_serializer=serializer.GraphSONSerializersV2d0()
                      )

    callback = c.submitAsync(__query)
    x = []
    for it in callback.result():
        for i in it:
            x.append(i)

    return str(x)
```
