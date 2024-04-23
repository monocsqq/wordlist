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

## Upgrade
Run the following command in the terminal(ターミナルで以下のコマンドを実行します):
```bash
python3 -m pip install --upgrade git+https://github.com/monocsqq/wordlist.git
```

## Usage
The app is very simple to use. You can add words and their meanings and search for a word to see its meaning.
You can change the mode of the app by typing,
- S: Search mode
- A: Add mode
- E: Edit mode
- R: Remove mode
- L: List mode
- Q: Quit


単語の検索，追加，編集，削除ができます．以下の文字を入力することでモードを変更できます．
- S: 検索モード
- A: 追加モード
- E: 編集モード
- R: 削除モード
- L: 一覧表示モード
- Q: 終了


## Caution
You may notice that `wordlist_data.pkl` is created in the home directory. This file contains all the words and their meanings. Do not delete this file or you will lose all your data.

ホームディレクトリ内に生成される`wordlist_data.pkl`は単語と意味を保存しています．このファイルを削除するとデータが失われるので注意してください．

## Notice
This app is still in development. If you find any bugs or have any suggestions, please let me know!

このアプリはまだ開発中です．バグや提案があれば教えてください！

- To users using this app before 04/22/2024: Please perform the following tasks before updating the app.
    - rename `data.pkl` to `wordlist_data.pkl`. You can find it in the directory where you installed the app.
    - move `wordlist_data.pkl` to `~/.wordlist/`

- 2024年4月22日以前からこのアプリを使用している方々へ：アプリを更新する前に以下の作業を行ってください．
    - `data.pkl`を`wordlist_data.pkl`にリネームしてください．アプリをインストールしたディレクトリ内にあります．
    - `wordlist_data.pkl`を`~/.wordlist/`に移動してください．
```
