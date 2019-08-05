## 日本語Wikipedia

一部前処理済みのテキストデータ。(2018/10/30の日本語wiki snapshot)

* テキストコーパス
https://interndata.blob.core.windows.net/wiki-ja-sudachi/wiki.ja.txt

```
$ head -10 wiki.ja.txt
一畑電車1000系電車

一畑電車1000系電車（いちばたでんしゃ1000けいでんしゃ）は、一畑電車が2014年(平成26年)に導入した通勤型電車である。

老朽化した3000系置き換えのため、東急1000系を譲り受けたものである。
東急テクノシステムで中間車を先頭車に改造のうえ2014年(平成26年)に2本、2015年(平成27年)に1本が導入された。
一畑電車では5000系以来16年ぶりの新車両であり、「オールステンレス車体」「ワンハンドルマスコン」「シングルアームパンタグラフ」「VVVFインバータ制御」など、同社初の新機軸が数多く盛り込まれている。

車体はビード補強付き軽量ステンレス製である。前面は中間車からの改造車であるため、東急1000系とは全く異なる形状となっており、上田電鉄6000系と同一の形態になっている。また、1003編成はライト類が角形から丸型に変更されたほか、前照灯はLEDに変更されている。非貫通型のため、連結運転時に通り抜けはできない。
スカートはスノープロウが付いた大きなものとなり、密着連結器と電気連結器を装備している。

```

* 分かち書き済みのテキストコーパス（sudachi type cを利用）
https://interndata.blob.core.windows.net/wiki-ja-sudachi/wiki.ja.sudachi.txt

```
$ head -10 wiki.ja.sudachi.txt
一畑電車 1000 系 電車

 一畑電車 1000 系 電車 いち ばたでん しゃ 1000 けい でんしゃ は 一畑電車 が 2014 年 平成 26 年 に 導入 し た 通勤 型 電車 で ある

 老朽化 し た 3000 系 置き換え の ため 東急 1000 系 を 譲り受け た もの で ある
 東急 テクノ システム で 中間 車 を 先頭 車 に 改造 の うえ 2014 年 平成 26 年 に 2 本 2015 年 平成 27 年 に 1 本 が 導入 さ れ た
 一畑電車 で は 5000 系 以来 16 年 ぶり の 新 車両 で あり オール ステンレス車体 ワンハンドルマスコン シングルアーム パンタグラフ VVVF インバータ 制御 など 同社 初 の 新機軸 が 数多く 盛り込ま れ て いる

 車体 は ビード 補強 付き 軽量 ステンレス製 で ある 前面 は 中間 車 から の 改造車 で ある ため 東急 1000 系 と は 全く 異なる 形状 と なっ て おり 上田電鉄 6000 系 と 同一 の 形態 に なっ て いる また 1003 編成 は ライト 類 が 角形 から 丸型 に 変更 さ れ た ほか 前 照灯 は LED に 変更 さ れ て いる 非 貫通 型 の ため 連結 運転 時 に 通り抜け は でき ない
 スカート は スノープロウ が 付い た 大きな もの と なり 密着 連結器 と 電気 連結器 を 装備 し て いる
```


* 分かち書き済みのテキストコーパス、英数字は全部小文字化
https://interndata.blob.core.windows.net/wiki-ja-sudachi/wiki.ja.sudachi.lower.txt 

```
$ head -10 wiki.ja.sudachi.lower.txt

一畑電車 1000 系 電車

 一畑電車 1000 系 電車 いち ばたでん しゃ 1000 けい でんしゃ は 一畑電車 が 2014 年 平成 26 年 に 導入 し た 通勤 型 電車 で ある

 老朽化 し た 3000 系 置き換え の ため 東急 1000 系 を 譲り受け た もの で ある
 東急 テクノ システム で 中間 車 を 先頭 車 に 改造 の うえ 2014 年 平成 26 年 に 2 本 2015 年 平成 27 年 に 1 本 が 導入 さ れ た
 一畑電車 で は 5000 系 以来 16 年 ぶり の 新 車両 で あり オール ステンレス車体 ワンハンドルマスコン シングルアーム パンタグラフ vvvf インバータ 制御 など 同社 初 の 新機軸 が 数多く 盛り込ま れ て いる

 車体 は ビード 補強 付き 軽量 ステンレス製 で ある 前面 は 中間 車 から の 改造車 で ある ため 東急 1000 系 と は 全く 異なる 形状 と なっ て おり 上田電鉄 6000 系 と 同一 の 形態 に なっ て いる また 1003 編成 は ライト 類 が 角形 から 丸型 に 変更 さ れ た ほか 前 照灯 は led に 変更 さ れ て いる 非 貫通 型 の ため 連結 運転 時 に 通り抜け は でき ない
 スカート は スノープロウ が 付い た 大きな もの と なり 密着 連結器 と 電気 連結器 を 装備 し て いる
```


## 名人関連api

### 形態素解析api (wakati)

#### 使い方

```
$ curl -X POST https://da-wakati.azurewebsites.net -d "これはドリーム・アーツ社の主要製品のSmartDBである"
これ	代名詞,*,*,*,*,*	此れ
は	助詞,係助詞,*,*,*,*	は
ドリーム・アーツ	名詞,固有名詞,一般,*,*,*	ドリーム・アーツ
社	名詞,普通名詞,助数詞可能,*,*,*	社
の	助詞,格助詞,*,*,*,*	の
主要	形状詞,一般,*,*,*,*	主要
製品	名詞,普通名詞,一般,*,*,*	製品
の	助詞,格助詞,*,*,*,*	の
SmartDB	名詞,固有名詞,一般,*,*,*	Sm@rtDB
で	助動詞,*,*,*,助動詞-ダ,連用形-一般	だ
ある	動詞,非自立可能,*,*,五段-ラ行,終止形-一般	有る
```

#### 仕様

* 内部はSudachiを使っている。現状、[タイプ C](https://github.com/WorksApplications/Sudachi#the-modes-of-splitting) の決め打ちになっている。
* UTF-8 text/plain で渡す 。UTF-8 text/plain で結果が返ってくる。

### 名人を探すapi

一文またはキーワードから社内名人を返す

#### 使い方

```
$ curl -H 'X-Api-Token:c7458a2ca18a48b8' -G https://da-meijin.dabaas.net/api/search --data-urlencode 'q=ポータル提案最強の人'

{
  "code" : "200",
  "data" : [ {
    "userName" : "村瀬 健太郎",
    "userId" : "murase",
    "mid" : 1000041,
    "mail" : "murase@dreamarts.co.jp",
    "photoUrl" : "https://dadev.dabaas.net/profileImages/murase@dreamarts.co.jp",
    "primaryGroupName" : "マーケティンググループ",
    "primaryGroupId" : 2006014,
    "type" : "GENERAL_USER",
    "score" : 0.4403885646983661,
    "hitReason" : {
      "keywords" : [ {
        "keyword" : "ポータル",
        "count" : 1014
      }, {
        "keyword" : "提案",
        "count" : 225
      }, {
        "keyword" : "最強",
        "count" : 2
      }, {
        "keyword" : "検討",
        "count" : 2655
      }, {
        "keyword" : "notes移行",
        "count" : 0
      }, {
        "keyword" : "bcp",
        "count" : 157
      } ]
    },
    "selfReference" : false
  }, {
    "userName" : "栗木 楽",
    "userId" : "r_kuriki",
    "mid" : 1000139,
    "mail" : "r_kuriki@dreamarts.co.jp",
    "photoUrl" : "https://dadev.dabaas.net/profileImages/r_kuriki@dreamarts.co.jp",
    "primaryGroupName" : "AEグループ2",
    "primaryGroupId" : 2000366,
    "type" : "GENERAL_USER",
    "score" : 0.43505043909346847,
    "hitReason" : {
      "keywords" : [ {
        "keyword" : "ポータル",
        "count" : 352
      }, {
        "keyword" : "提案",
        "count" : 1035
      }, {
        "keyword" : "最強",
        "count" : 7
      }, {
        "keyword" : "検討",
        "count" : 506
      }, {
        "keyword" : "notes移行",
        "count" : 183
      }, {
        "keyword" : "bcp",
        "count" : 4
      } ]
    },
    "selfReference" : false
  }]

```

#### 仕様

* qはクエリパラメータで、キーワードまたは一文を返す
* scoreは関連度（0.0~1.0）
* hitReasonはなぜこの人がヒットしたかを参考として、一部関連キーワード及びそのユーザのWeeklyReportに出現した回数をを返す
* selfReferenceは自分のscoreと比較するためのもので、ここで無視して良い
* UTF-8 application/json で結果を返す

### ユーザのradar chart api
指定する分野において、ユーザの関連度を返す

#### 使い方

```
curl -H 'X-Api-Token:c7458a2ca18a48b8' -G https://da-meijin.dabaas.net/api/users/sakurai@dreamarts.co.jp/radar --data-urlencode 'keywords=企画,マーケティング,営業,提案,実装,サポート'

{
  "code" : "200",
  "data" : [ {
    "keyword" : "企画",
    "point" : 4.5
  }, {
    "keyword" : "マーケティング",
    "point" : 5.8
  }, {
    "keyword" : "営業",
    "point" : 4.6
  }, {
    "keyword" : "提案",
    "point" : 5.7
  }, {
    "keyword" : "実装",
    "point" : 8.3
  }, {
    "keyword" : "サポート",
    "point" : 7.2
  } ]
}

```

### 仕様
* userIdはemailアドレス
* keywordsはカンマ区切りの単語(radar図の軸となる)
    * デフォルトは"企画,マーケティング,営業,提案,実装,サポート"となる
* pointは 0.0 ~ 10.0。 高いほど指定するキーワードに詳しい
* UTF-8 application/json で結果を返す


