# Gremlin Python
PythonのプログラムからCosmosDBに接続し、Gremlinのクエリを発行します。

## サンプル
[gremlin_python](./gremlin_python)以下に、サンプルプログラムを置いています。

オプション  
- -d, --database : データベース名を指定
- -g, --graph : グラフ名を指定
- -k, --key : パスワードを指定

database, graphのデフォルト値は知話輪チャットデータになっています。

```bash
$ cd ./gremlin_python
$ pipenv install
$ pipenv shell
$ python gremlin_shell.py -d intern-data -g chiwawa -k primary_key_here
gremlin>
```

| データベース       | -d, --database       | -g, --graph |
| --------------- | -------------- | ---------- |
| 知話輪チャットデータ | intern-data    | chiwawa |
| ウィークリーレポート | Intern-data-wr | wr |
| 営業レポート    | intern-data-sales | sales |
| お問い合わせ    | intern-data-support | support |

パスワード(-k, --key)は、[gremlin_console](./gremlin_console)フォルダのymlファイルを参照してください。
