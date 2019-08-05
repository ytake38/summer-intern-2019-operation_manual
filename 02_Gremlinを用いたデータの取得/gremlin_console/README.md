# データベースへの接続情報とComposeファイル
## 接続情報
|データ|設定|
|---|---|
|知話輪チャットデータ|[chiwawa.yml](./chiwawa.yml)|
|お問い合わせ|[support.yml](support.yml)|
|従業員週報|[weekly_report.yml](weekly_report.yml)|
|営業レポート|[sales_report.yml](sales_report.yml)|

## Gremlin Console コンテナの起動
gremlin_console以下のファイルを適当なディレクトリに配置し、以下コマンドを入力することで、設定ファイルをマウントしたコンテナが起動します。

```bash
$ cd ~/Downloads/gremlin
$ docker-compose run gremlin
         \,,,/
         (o o)
-----oOOo-(3)-oOOo-----
plugin activated: tinkerpop.server
plugin activated: tinkerpop.utilities
plugin activated: tinkerpop.tinkergraph
gremlin>
```
