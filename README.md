# wordlist

## Description
This is a simple vocabulary app that works in the terminal. It is a simple way to keep track of words you are learning and their meanings.

ターミナル上で動作するシンプルな単語帳アプリです．学習中の単語と意味を整理できます．

## Installation
1. Run the following command in the terminal(ターミナルで以下のコマンドを実行します):
```bash
python3 -m pip install git+https://github.com/monocsqq/wordlist.git
```
2. You can now run the app by typing `wordlist` in the terminal!(ターミナルで`wordlist`と入力するとアプリが起動します)

## Usage
The app is very simple to use. You can add words and their meanings and search for a word to see its meaning.
You can change the mode of the app by typing,
- S: Search mode
- A: Add mode
- E: Edit mode
- R: Remove mode
- Q: Quit


単語の検索，追加，編集，削除ができます．以下の文字を入力することでモードを変更できます．
- S: 検索モード
- A: 追加モード
- E: 編集モード
- R: 削除モード
- Q: 終了


## Caution
You may notice that `wordlist_data.pkl` is created in the home directory. This file contains all the words and their meanings. Do not delete this file or you will lose all your data.

ホームディレクトリ内に生成される`wordlist_data.pkl`は単語と意味を保存しています．このファイルを削除するとデータが失われるので注意してください．
