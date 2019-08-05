# 本番環境herokuに手元のBOTを反映する方法

## githubのリポジトリを作成する

`$ git init`

## herokuコマンドのインストール

以下のURLからインストール
https://devcenter.heroku.com/articles/heroku-cli#download-and-install

## herokuにlogin

`$ heroku login`

- herokuアカウントを入力

## 「Procfile」ファイルを作成し以下を記述

`web: gunicorn app:app`

## herokuにデプロイ

```
$ git add -A
$ git commit -m "hello heroku"
$ heroku create
$ git push heroku master
$ heroku open
```

## herokuに環境変数をセット

`$ heroku config:set ENV_NAME="ENV_VAR" --app "APP_NAME"`

## BOTとherokuを繋ぐ

デプロイの`$ heroku open`で開いたページのURLを[BOTに登録](./05_%E3%82%A8%E3%82%B3%E3%83%BCBOT%E3%82%92%E4%BD%9C%E3%81%A3%E3%81%A6%E5%8B%95%E3%81%8B%E3%81%97%E3%81%A6%E3%81%BF%E3%82%8B.md#%E8%A1%A8%E7%A4%BA%E3%81%95%E3%82%8C%E3%82%8Bngrok%E3%81%AEurl%E3%82%92%E7%9F%A5%E8%A9%B1%E8%BC%AA%E7%AE%A1%E7%90%86%E7%94%BB%E9%9D%A2%E3%81%A7webhookurl%E3%81%AB%E7%99%BB%E9%8C%B2%E3%81%99%E3%82%8B)

- 完了！[確認してみよう](./05_%E3%82%A8%E3%82%B3%E3%83%BCBOT%E3%82%92%E4%BD%9C%E3%81%A3%E3%81%A6%E5%8B%95%E3%81%8B%E3%81%97%E3%81%A6%E3%81%BF%E3%82%8B.md#bot%E3%81%AB%E6%8A%95%E3%81%92%E3%81%8B%E3%81%91%E3%82%8B)
