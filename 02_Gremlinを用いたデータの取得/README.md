# Gremlinを用いたデータの取得
私たちが用意したデータは、会社名や人名をマスク処理した後、
Azure Cosmos DBのグラフデータベースに格納されています。  


## ゴール
- CosmosDBからGremlinを用いてデータを取得できる
  - Gremlinクエリが使える
  - どんなデータが格納されているかを知る
- サンプルクエリを参考して、NLPのデータソースとして利用するデータの取得を試みる

## 今回取り組む部分
<img src="imgs/db_cast.png" width="500px" />

##  インデックス

### Step1: [データソースの説明](./01_データソースの説明.md)
今回、4種類のデータを用意しています。  
どういったテキストデータがDBに格納されているのか説明します。

### Step2: [Gremlin Consoleの導入](./02_Gremlin_Consoleの導入.md)
Gremlinを使うためのコンソールをインストールします。

### Step3: [Gremlinコマンドについて](./03_Gremlinコマンドについて.md)
Gremlinクエリの作法を学びます。

### Step4: [Gremlinを使ってみよう](./04_Gremlinを使ってみよう.md)
Gremlinクエリを使ってみましょう。

### Step5: [Gremlin Python](./05_Gremlin_Python.md)
GremlinをPythonから利用します。

## 各データベースの設計とGremlinサンプル集
- [知話輪チャットデータ](./DB設計とGremlinサンプル/知話輪.md)
- [お問い合わせ](./DB設計とGremlinサンプル/PD問い合わせ.md)
- [従業員週報](./DB設計とGremlinサンプル/ウィークリーレポート.md)
- [営業レポート](./DB設計とGremlinサンプル/営業レポート.md)

## GraphDB接続情報
各データベースの接続情報を db_info 以下に保存しています。  
マスキングは行っていますが**DA・顧客情報を取得可能**、
**Writableなキー**のため、取り扱いには十分注意してください。
