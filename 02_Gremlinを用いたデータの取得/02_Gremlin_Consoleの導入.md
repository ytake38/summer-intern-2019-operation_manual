# Gremlin Consoleの導入
Graph DBからデータを取得するための言語Gremlin。  
Gremlinを実行するためのConsoleを導入していきます。  

分かる方はDockerを利用すると簡単です。[Dockerを利用する場合](#dockerを利用する場合)

## Java8
Gremlin Consoleを動作させるには、Java8が必要です。
Java8以上の環境が整っている場合、この手順は必要ありません。

### macOSの場合
```bash
$ brew tap AdoptOpenJDK/openjdk
$ brew cask install adoptopenjdk8
```

`.bash_profile`に下記の2行を追記します。
```
export JAVA_HOME=`/usr/libexec/java_home -v "1.8"`
PATH=${JAVA_HOME}/bin:${PATH}
```

設定を反映させます。

```bash
$ source ~/.bash_profile
```

### Windowsの場合
[WindowsへのJDKインストール方法](https://qiita.com/ko2a/items/69fa8a5366d7449500ca)を参考にインストールを進めてください。

## Gremlin Console
[こちらのページ](http://tinkerpop.apache.org/downloads.html)
よりGremlin Consoleをダウンロードします。  

以下のコマンドは、Downloadsフォルダに保存した場合を想定しています。

```bash
$ cd ~/Downloads
$ unzip apache-tinkerpop-gremlin-console-3.4.2-bin.zip
$ cd apache-tinkerpop-gremlin-console-3.4.2-bin
$ bin/gremlin.sh
         \,,,/
         (o o)
-----oOOo-(3)-oOOo-----
plugin activated: tinkerpop.server
plugin activated: tinkerpop.utilities
plugin activated: tinkerpop.tinkergraph
gremlin>
```

このような出力が表示されれば、導入は完了です。

## Dockerを利用する場合

```bash
$ docker pull tinkerpop/gremlin-console
$ docker run --rm -it tinkerpop/gremlin-console
```

[gremlin_console](./gremlin_console/)フォルダにデータベース接続用の設定ファイルとComposeファイルを置いています。  
適当なディレクトリに配置し、以下コマンドを入力することで、設定ファイルをマウントしたコンテナが起動します。

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
