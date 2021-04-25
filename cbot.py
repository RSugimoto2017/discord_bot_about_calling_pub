# インストールした discord.py を読み込む
import discord
import random

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'ODMyMjIxMzk4NjU4OTczNzQ2.YHgokw.9E9oVKXdAr3O9alFQmZFLr417xM'

# 接続に必要なオブジェクトを生成
client = discord.Client()

CHANNEL_ID = 735441730509209601

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '^neko':
        await message.channel.send('にゃーん')
        #await message.channel.send(message.author.id)

    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '^duel':
        rand = random.randint(0, 1)
        if rand == 0:
            await message.channel.send(f'{message.author.name}は先攻です！')
        if rand == 1:
            await message.channel.send(f'{message.author.name}は後攻です！')
        
    #bot停止(管理者のみ)
    if "^stop" in message.content:
        if message.author.id == 576319478606856193:
            await message.channel.send("ばいばーい！")
            await client.logout()
        else:
            await message.channel.send("管理者専用コマンドだよ！")
    #   クレジット表示
    if "^credit" in message.content:
        authormem = await client.fetch_user(576319478606856193)
        await message.channel.send(f"製作者は「{authormem.name}」です。")
    #   ヘルプ表示
    if "^help" in message.content:
        await message.channel.send("-----------------------------------------------メイン機能-------------------------------------------------\n\
ボイスチャンネルを開始時、テキストチャットに通知が出ます。\n\
ボイスチャンネルを終了時、テキストチャットに通知が出ます。\n\
------------------------------------------------サブ機能--------------------------------------------------\n\
「^stop」：botをオフラインにします。(管理者(現在のところもぎ)のみ)\n\
「^duel」：コマンド送信者が先攻か後攻かランダムに決定します。\
「^help」：操作説明を表示します。\n\
「^credit」：製作者について表示します。\n\
「^neko」：にゃーんって言います。\n\
----------------------------------------------------------------------------------------------------------")
        
@client.event
async def on_vc_start(member,channel):
    txchannel = client.get_channel(CHANNEL_ID)
    await txchannel.send(f"{member.name}さんが「{channel.name}」でボイスチャットを開始しました！誰か来てね！")

@client.event
async def on_vc_end(member,channel):
    txchannel = client.get_channel(CHANNEL_ID)
    await txchannel.send(f"{member.name}が「{channel.name}」のボイスチャットを終了しました。おやすみー")
    
"""メンバーのボイスチャンネル出入り時に実行されるイベントハンドラ"""
@client.event
async def on_voice_state_update(member,before,after):
    if before.channel != after.channel:
        # before.channelとafter.channelが異なるなら入退室
        if after.channel and len(after.channel.members) == 1:
            # もし、ボイスチャットが開始されたら
            client.dispatch("vc_start",member,after.channel) #発火！

        if before.channel and len(before.channel.members) == 0:
            # もし、ボイスチャットが終了したら
            client.dispatch("vc_end",member,before.channel) #発火！

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)