# wordlist

## Description
This is a simple vocabulary app that works in the terminal. It is a simple way to keep track of words you are learning and their meanings.

ターミナル上で動作するシンプルな単語帳アプリです．学習中の単語と意味を整理できます．

## Installation
1. Clone this repository
2. Run the following command in the terminal:
```bash
cd wordlist
python3 -m pip install .
```
3. You can now run the app by typing `wordlist` in the terminal!

1. リポジトリをクローンします．
2. ターミナルで以下のコマンドを実行します：
```bash
cd wordlist
python3 -m pip install .
```
3. ターミナルで`wordlist`と入力するとアプリが起動します．

## Usage
The app is very simple to use. You can add words and their meanings and search for a word to see its meaning.
You can change the mode of the app by typing,
- S: Search mode
- E: Edit mode
- R: Remove mode
- Q: Quit

You can add a word when you can't find it in the search mode(I plan to add Add mode in the future).

単語の検索，追加，編集，削除ができます．以下の文字を入力することでモードを変更できます．
- S: 検索モード
- E: 編集モード
- R: 削除モード
- Q: 終了
単語の追加は検索モードで見つからなかった場合に行うことができます（将来的に追加モードを追加する予定です）．

## Caution
You may notice that `data.pkl` is created in the directory where you run the app. This file contains all the words and their meanings. Do not delete this file or you will lose all your data.

同一ディレクトリ内に生成される`data.pkl`は単語と意味を保存しています．このファイルを削除するとデータが失われるので注意してください．
