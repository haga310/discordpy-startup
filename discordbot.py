from discord.ext import commands
import os
import traceback
import random 

bot = commands.Bot(command_prefix='/')#,help_command=commands.MinimalHelpCommand())
token = 'Njk3MDAzNTUwMzcwMTY4ODMy.Xpl-WA.paoFH34Krxd8a2GXV5gAeSsCOYk'
#token = os.environ['DISCORD_BOT_TOKEN']
InMember=[]
master=0
insider=1
f = open('text.txt',"r",encoding="utf-8")
odai= f.readlines()
odailen=len(odai)
for a in range(odailen):
    odai[a]=odai[a].strip()
f.close

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command(aliases=['join'])
async def InsiderJoin(ctx):
    """インサイダーゲームに参加 /join"""
    await ctx.send(f"{ctx.author.mention} さんをインサイダーゲームのプレイヤーに追加しました。")
    InMember.append([(ctx.author),"nomal"])
    #await ctx.send("log--"InMember)

@bot.command(aliases=['show'])
async def ShowPlayer(ctx):
    """インサイダーゲーム参加プレイヤー表示 /show"""
    await ctx.send("インサイダーゲームの参加者は")
    await ctx.send(InMember)

@bot.command(aliases=['start'])
async def StartInsider(ctx):
    """インサイダーゲーム開始、役職配分 /start"""
    count=len(InMember)
    if count>=2:
        await ctx.send(f"インサイダーゲームを {count} 人で開始します")
        master=random.randint(0,count-1)
        insider=master
        while insider==master:
            insider=random.randint(0,count-1)
        InMember[master][1]="master"
        InMember[insider][1]="insider"
        await ctx.send(f"{InMember[master][0].mention}　さんがマスターです")
        await ctx.send("お題をガチャしてください　/Odai ")
    else:
        await ctx.send("参加人数が足りません")
#@bot.command()
#async def Odai(ctx):
@bot.command()
async def Odai(ctx):
    """masterがお題ガチャ→DMでmastarとinsiderに通知"""
    for count in range(len(InMember)):
        if InMember[count][1]=="master":
            target1=InMember[count][0] #master
        elif InMember[count][1]=="insider":
            target2=InMember[count][0] #insider
    dm= await target1.create_dm()
    dm2= await target2.create_dm()
    choice=random.randint(0,len(odai)-1)
    await dm.send(odai[choice])
    await dm2.send(odai[choice])

@bot.command(aliases=['Preset'])
async def PlayerReset(ctx):
    """参加プレイヤーをリセット /Preset"""
    InMember.clear()
    await ctx.send(InMember)

@bot.command(aliases=['Jreset'])
async def JobReset(ctx):
    """役職をリセット(人が同じで連戦) /Jreset"""
    for count in range(len(InMember)):
        InMember[count][1]="normal"

@bot.command()
async def ping(ctx):
    """Play Ping-Pong with Zeroppe"""
    await ctx.send('pong')
    
@bot.event
async def on_message(message):
    """メッセージを処理"""
    if message.author.bot:  # ボットのメッセージをハネる
        return

    if message.content == "!眠たい":
        # チャンネルへメッセージを送信
        await message.channel.send(f"{message.author.mention}さん 寝ましょう")  # f文字列（フォーマット済
        
    await bot.process_commands(message)


bot.run(token)
