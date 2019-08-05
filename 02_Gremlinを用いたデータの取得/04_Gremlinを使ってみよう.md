# Gremlinを使ってみよう

## 前準備
### Gremlin Consoleの導入
まだの方は、以下のページを参考に、Gremlin Consoleを導入してください。  
[Gremlin Console導入](./02_Gremlin_Console導入.md)

### データベース接続情報のダウンロード
各データベースにアクセスするための情報が必要です。  
db_infoにあるymlファイル群をダウンロードしてください。

※ここでは、`~Downloads`以下にダウンロードされたものとします。

## 知話輪のデータベースへの接続
Gremlin Consoleを起動します。

```bash
$ cd ~/Downloads/apache-tinkerpop-gremlin-console-3.4.2
$ bin/gremlin.sh
         \,,,/
         (o o)
-----oOOo-(3)-oOOo-----
plugin activated: tinkerpop.server
plugin activated: tinkerpop.utilities
plugin activated: tinkerpop.tinkergraph
gremlin>
```

知話輪のデータが入っているデータベースに接続。
ymlファイルへのパスは適宜変更してください。
docker-composeを利用した場合は、`/gremlin/chiwawa.yml`となります。

```bash
gremlin> :remote connect tinkerpop.server ../gremlin/chiwawa.yml
==>Configured summer-intern-2019.gremlin.cosmos.azure.com/40.115.241.37:443
gremlin>
```

Gremlinクエリの待ち受け状態にします。

```bash
gremlin> :remote console
==>All scripts will now be sent to Gremlin Server - [summer-intern-2019.gremlin.cosmos.azure.com/40.115.241.37:443] - type ':remote console' to return to local mode
gremlin>
```

この状態でクエリを投げると、結果が返ってきます。

## クエリを投げてみよう
例えば、すべての`user`の頂点から1点取得し、その点の`name`プロパティを表示するには、

```bash
gremlin> g.V().hasLabel('user').limit(1).values('name')
==>user1
```

このユーザが投稿した(`posts`の辺の先)メッセージの中の1点を取得。  
そのメッセージの頂点の本文`text`を表示するには、

```bash
gremlin> g.V().hasLabel('user').limit(1).out('posts').limit(1).values('text')
==>@USERAAADGBEDDUSERAABGDAAAE: @USERAAADHCFAFUSERAAADIEABE: @USERACIEGCEFEUSERADBACFDDE: @USERAEEJHECCFUSERACHEGCABF:
会議術の第5回を作成しました。
チェックとイラストをお願いします。
```

メッセージを3件取得してみます。

```bash
gremlin> g.V().hasLabel('user').limit(1).out('posts').range(0, 3).values('text')
==>@USERAAADGBEDDUSERAABGDAAAE: @USERAAADHCFAFUSERAAADIEABE: @USERACIEGCEFEUSERADBACFDDE: @USERAEEJHECCFUSERACHEGCABF:
会議術の第5回を作成しました。
チェックとイラストをお願いします。
==>https://xxxx
==>@USERAEEJHECCFUSERACHEGCABF:
全部で12回あります。
その頃には我々は有名人ですな。ハハハ
```

Console上では`==>`が表示されますが、実際のレスポンスはjson形式のリストになっています。
```json
[
  "@USERAAADGBEDDUSERAABGDAAAE: @USERAAADHCFAFUSERAAADIEABE: @USERACIEGCEFEUSERADBACFDDE: @USERAEEJHECCFUSERACHEGCABF: \n会議術の第5回を作成しました。\nチェックとイラストをお願いします。",
  "https://xxx",
  "@USERAEEJHECCFUSERACHEGCABF: \n全部で12回あります。\nその頃には我々は有名人ですな。ハハハ"
]
```

## Gremlin Consoleを終了
以下のコマンドで、Gremlin Consoleが終了します。
```bash
gremlin> :quit
```
