# 自然言語処理のすすめ

## 文字列を正規化処理する

辞書作成のベースとなるデータをあらかじめに処理、不要なデータや記号を除きます。

#### 参考

- [解析前に行うことが望ましい文字列の正規化処理](https://github.com/neologd/mecab-ipadic-neologd/wiki/Regexp)
- [自然言語処理における前処理の種類とその威力](https://qiita.com/Hironsan/items/2466fe0f344115aff177)



## 自然言語処理

自然言語処理には様々な技術存在している。各チームの目標によって必要な技術も異なるので、あくまで参考として使ってください。

### 形態素解析

```
形態素解析とは、文法的な情報の注記の無い自然言語から、対象言語の文法や、辞書と呼ばれる単語の品詞等の情報にもとづき、
形態素の列に分割し、それぞれの形態素の品詞（名詞、動詞など）を判別する作業である。
(Wikipediaより)
```

一部フリーで使える日本語の形態素解析エンジン

- [MeCab](http://taku910.github.io/mecab/#parse)
- [Janome](https://pypi.org/project/Janome/)
- [Sudachi](https://github.com/WorksApplications/Sudachi)

必要に応じて好きな方を使ってください。



### 辞書構築

- [Gensim公式サイト](https://radimrehurek.com/gensim/tut1.html)
  - Qiitaの参考記事：[gensim入門](https://qiita.com/u6k/items/5170b8d8e3f41531f08a)
- [Word2Vecモデル作成](https://qiita.com/kenta1984/items/93b64768494f971edf86)

