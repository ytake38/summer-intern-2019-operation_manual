# gremlinコマンドのサンプル集

gremlinでグラフDBから必要な情報を取得するときの基本的な使い方を紹介します。  
より詳しい操作方法を知りたい場合は、[公式ドキュメント](http://tinkerpop.apache.org/docs/current/reference/#traversal)を参照してください。  
## 基本概要
グラフにはそれぞれの要素が頂点(Vertical)として表現され、要素間の関係性は辺(Edge)で表現されます。  
それぞれの頂点にはプロパティ(Property)と呼ばれる付加情報が付いている場合があります。  
辺は始点と終点を持ち、図面上では矢印で表現されます。

## 全ての頂点(ノード)を取得する
データベース上に存在する全ての頂点を絞り込みなしで取得します。  
大量の頂点が登録されている場合、時間も負荷もかかるので絞り込みなしでの取得は避けるべきです。
```
g.V()
```
## 取得できるデータ形式
gremlinで取得するデータ形式はJSONで表現されます。  
頂点を取得する場合、次のようなJSONオブジェクトのリストで表現されます。  
```
[
  {
    "id": "be62496ae2619e974f2e759392f5928b539442bc",
    "label": "user",
    "type": "vertex",
    "properties": {
      "name": [
        {
          "id": "d7824a6e-c85f-4942-8162-b8b0842cb2a6",
          "value": "user1"
        }
      ],
      "fullName": [
        {
          "id": "a5b867cd-dbe4-4d63-840a-d278dd8ecc93",
          "value": "山田太郎"
        }
      ]
    }
  },
  ...
]
```
取得する頂点が１つのみであってもリストに格納されて渡されるので要注意です。  
```
[
  {
      頂点A
  }
]
```

## 特定のラベルで絞り込んで頂点を取得する。
頂点の種類がユーザの場合をuserラベルを使って表現しています。  
```
g.V().hasLabel('user')
```

## 特定の頂点をnameプロパティで絞り込んで取得する。
nameプロパティはユニークなので必ず１つの頂点に絞り込めます
```
g.V().has('name', 'user1')
```

## 特定の頂点を始点とする全ての辺を取得する。
```
g.V().has('name', 'user1').outE()
```
辺を取得する場合のJSONはこんな感じになります。  
```
[
  {
    "id": "fd2dddf4-d152-4c32-8e6d-994ff93c4c58",
    "label": "follow",
    "type": "edge",
    "inVLabel": "user",
    "outVLabel": "user",
    "inV": "6fcf1828bd912960123e79f48b5d3eead5a34335",
    "outV": "f9c0b33e9a8e85c1c6386e371e92ea99903e0eba"
  },
  ...
]
```
## 特定の頂点を終点とする全ての辺を取得する。
```
g.V().has('name', 'user1').inE()
```
## 特定の頂点を始点または終点とする全ての辺を取得する。
```
g.V().has('name', 'user1').bothE()
```
## 特定の種類の辺で絞り込む
```
g.V().has('name', 'user1').outE('follow')
```
## 特定の頂点を始点とした辺を終点に持つ頂点を取得する。
この場合取得するJSONは辺のリストでなく頂点のリストになります。
```
g.V().has('name', 'user1').out()
```
## 特定の頂点を終点とした辺を始点に持つ頂点を取得する。
```
g.V().has('name', 'user1').in()
```
## 特定の種類の辺で絞り込む
```
g.V().has('name', 'user1').out()
```
## 特定の辺を持つ頂点を取得する
(user1) -follow-> (取得したい頂点)
```
g.V().has('name', 'user1').out('follow')
```
(user1) <-follow- (取得したい頂点)
```
g.V().has('name', 'user1').in('follow')
```
## 頂点の数を取得する
userラベルを持つ頂点の数
```
g.V().hasLabel('user').count()
```
countで取得できるJSONの構造は以下のようにリストの中に単一の数値が入ります。
```
[400]
```
user1のフォロー数(outEでも可)
```
g.V().has('name', 'user1').out('follow').count()
```
user1のフォロワー数(inEでも可)
```
g.V().has('name', 'user1').in('follow').count()
```
## 特定のプロパティを指定して取得する
user1のフォロワーのユーザ名一覧を取得したい場合
```
g.V().has('name', 'user1').out('follow').values('name')
```
取得できるJSONは以下のようになります
```
[
  "user2",
  "user55",
  "user128",
  ...
]
```
