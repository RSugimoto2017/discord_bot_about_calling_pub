# discord_bot_about_calling_pub

こちらはpublic版なのでトークンが隠されています

Discordの通話に関する操作、通知をまとめたbotです。

随時更新予定です。

## 操作方法

<span style="color: orange; ">
- メイン機能<br>
1. ボイスチャンネルを開始時、テキストチャットに通知が出ます。<br>
2. ボイスチャンネルを終了時、テキストチャットに通知が出ます。  <br>
3. 「^join」：botをボイスチャンネルに参加させます。<br>
4. 「^leave」：botをボイスチャンネルから退出させます。<br>
5. 「^mute」：自分とbotが参加しているボイスチャンネルの全員をミュートします。<br>
6. 「^unmute」：自分とbotが参加しているボイスチャンネルの全員をミュート解除します。<br>
7. 「^goodnight」：自分とbotが参加しているボイスチャンネルの全員を退出させます。<br>
- サブ機能  <br>
1. 「^stop」：botをオフラインにします。(管理者(現在のところもぎ)のみ)  <br>
2. 「^help」：操作説明を表示します。  <br>
3. 「^credit」：製作者について通知します。<br>
</span>  

## 以下テンプレートより

## 各種ファイル情報

### discordbot.py
PythonによるDiscordBotのアプリケーションファイルです。

### requirements.txt
使用しているPythonのライブラリ情報の設定ファイルです。

### Procfile
Herokuでのプロセス実行コマンドの設定ファイルです。

### runtime.txt
Herokuでの実行環境の設定ファイルです。

### app.json
Herokuデプロイボタンの設定ファイルです。

### .github/workflows/flake8.yaml
GitHub Actions による自動構文チェックの設定ファイルです。

### .gitignore
Git管理が不要なファイル/ディレクトリの設定ファイルです。

### LICENSE
このリポジトリのコードの権利情報です。MITライセンスの範囲でご自由にご利用ください。

### README.md
このドキュメントです。
