# -*- coding: utf-8 -*-
# インストールした discord.py を読み込む
import discord
import random

# 自分のBotのアクセストークンに置き換えてください
#public版なので隠します
TOKEN = '**************************************************'

# 接続に必要なオブジェクトを生成
client = discord.Client()

CHANNEL_ID = '*************************'

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
    if message.content == "^join":
        if message.author.voice is None:
            await message.channel.send("ボイスチャンネルに入ってから呼んでね！")
            return
        # ボイスチャンネルに接続する
        await message.author.voice.channel.connect()
        await message.channel.send("通話お邪魔しまーす！")

    elif message.content == "^leave":
        if message.guild.voice_client is None:
            await message.channel.send("初めからボイスチャンネルに入ってないよ！")
            return
        # 切断する
        await message.guild.voice_client.disconnect()
        await message.channel.send("また呼んでね！")

    if message.content == "^goodnight":
        if message.author.voice is not None and message.guild.me in message.author.voice.channel.members:
            await allkick(message)
        else:
            await message.channel.send("botを自分と同じボイスチャンネルに入れてからにしてね！")
        
    #if "^mute" in message.content:
    if message.content == "^mute":
        if message.author.voice is not None and message.guild.me in message.author.voice.channel.members:
            await mute(message)
        else:
            await message.channel.send("botを自分と同じボイスチャンネルに入れてからにしてね！")

    #if "^unmute" in message.content:
    if message.content == "^unmute":
        if message.author.voice is not None and message.guild.me in message.author.voice.channel.members:
            await unmute(message)
        else:
            await message.channel.send("botを自分と同じボイスチャンネルに入れてからにしてね！")
            
    #bot停止(管理者のみ)
    if "^stop" in message.content:
        if message.author.id == '*************************':
            await message.channel.send("ばいばーい！")
            await client.logout()
        else:
            await message.channel.send("管理者専用コマンドだよ！")
    #   クレジット表示
    if "^credit" in message.content:
        authormem = await client.fetch_user('*************************')
        await message.channel.send(f"製作者は「{authormem.name}」です。")
    #   ヘルプ表示
    if "^help" in message.content:
        await message.channel.send("```fix\n\
------------------------------メイン機能--------------------------------\n\
ボイスチャンネルを開始時、テキストチャットに通知が出ます。\n\
ボイスチャンネルを終了時、テキストチャットに通知が出ます。\n\
「^join」：botをボイスチャンネルに参加させます。\n\
「^leave」：botをボイスチャンネルから退出させます。\n\
「^mute」：自分とbotが参加しているボイスチャンネルの全員をミュートします。\n\
「^unmute」：自分botが参加しているボイスチャンネルの全員をミュート解除します。\n\
「^goodnight」：自分とbotが参加しているボイスチャンネルの全員を退出させます。\n\
--------------------------------サブ機能--------------------------------\n\
「^stop」：botをオフラインにします。(管理者(現在のところもぎ)のみ)\n\
「^help」：操作説明を表示します。\n\
「^credit」：製作者について表示します。\n\
------------------------------------------------------------------------\n\
```")
        

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
            #print(len(after.channel.members))
            # もし、ボイスチャットが開始されたら
            client.dispatch("vc_start",member,after.channel) #発火！

        if before.channel and len(before.channel.members) == 0:
            #print(len(before.channel.members))
            # もし、ボイスチャットが終了したら
            client.dispatch("vc_end",member,before.channel) #発火！

async def allkick(message):
    if message.author.guild_permissions.administrator:
        vc = message.guild.me.voice.channel
        await message.channel.send("おやすみなさい！")
        for member in vc.members:
            await member.move_to(None)

async def mute(message):
    if message.author.guild_permissions.administrator:
        #await message.channel.send("admin")
        vc = message.guild.me.voice.channel # ボイスチャンネルを取得
        await message.channel.send("ミュートするよ！")
        for member in vc.members:
            await member.edit(mute=True) # チャンネルの各参加者をミュートする
    else:
        await message.channel.send("管理者じゃないよ！")


async def unmute(message):
    if message.author.guild_permissions.administrator:
        #await message.channel.send("admin")
        vc1 = message.guild.me.voice.channel
        await message.channel.send("ミュート解除するよ！")
        for member in vc1.members:
            await member.edit(mute=False) # チャンネルの各参加者をミュート解除する
    else:
        await message.channel.send("管理者じゃないよ！")

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
