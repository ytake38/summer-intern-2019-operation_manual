# Python環境の準備
本インターンシップは、Python3系が動作する環境を前提に進めます。予めご準備ください。  
すでに3系が動作する環境が整っている場合は、スキップしていただいて構いません。

## macOS環境で準備する場合

Homebrewが導入済みであることが前提となります。

### Python3系のインストール

Terminalを起動。以下のコマンドを実行。

```
$ brew update
$ brew install pyenv
$ pyenv install 3.6.5
$ pyenv global 3.6.5
```

3系がインストールされていることを確認。

```
$ python -V
Python 3.6.5
```

表示されるバージョンが2.7.xの場合、macOS標準の`/usr/bin/python`を参照しています。  
以下の手順を実施してください。

```
$ python -V
Python 2.7.10

$ pyenv init
# Load pyenv automatically by appending
# the following to ~/.bashrc:

eval "$(pyenv init -)"
```

`eval "$(pyenv init -)"` を `~/.bash_profile` に追記します。

```
$ vim  ~/.bashrc 

$ source ~/.bashrc

$ python -V      
Python 3.6.5
```

### pipenvのインストール

Pythonの仮想環境を管理するツール(依存パッケージ管理)、pipenvをインストールします。

同様に、Terminalで以下のコマンドを実行。

```
$ pip install pipenv
```
<!-- 
##### ※Tips:

- Python2系がインストールされた場合、pipのデフォルトが2系となり、上記コマンドがエラーになることがあります。
  - この場合、pipの代わりにpip3で上記コマンドを実行すると3系を利用することとなります。
  - (pip3がインストールされていない場合は[こちら](https://docs.python.org/ja/3/installing/index.html#pip-not-installed)の手順を参考してください)
- どうしてもできなければ、homebrewでインストールしても構いません。

```
brew install pipenv
```
 -->

## Windows環境で準備する場合

### Python3系のインストール

Python Japanのインストレーションガイドに従ってインストールを行います。  
https://www.python.jp/install/windows/install_py3.html

Windows PowerShellを起動。(Windows10の場合、スタートメニューから検索できます。)  
以下のコマンドを入力し、バージョン3系がインストールされていることを確認。

```
$ python -V
Python 3.6.5
```

### pipenvのインストール

同様にWindows PowerShellで以下のコマンドを実行。

```
$ pip install pipenv
```
