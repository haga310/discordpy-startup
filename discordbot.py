from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
InMember=[]
#インサイダーゲームの参加メンバリスト

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def InsiderJoin(ctx):
    await ctx.send(f"{ctx.author.mention}さんをインサイダーゲームのプレイヤーに追加しました。")
    InMember.append(str(ctx.author.mention))
    await ctx.send("log--"InMember)

@bot.command()
async def StartInsider(ctx):
    await ctx.send("インサイダーゲームの開始じゃい。参加プレイヤーはInsiderJoinコマンドを打つベシ")
    await ctx.send("log--"InMember)    
    
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def tell(ctx):
    await ctx.send('そんなキーワードは　ぜろっぺだよ')        
    
#@bot.command()
#async def help(ctx):
 #   embed = discord.Embed(title="Zeroppe", description="A Very Zeroppe bot. List of commands are:", color=0xeee657)
 #   embed.add_field(name="/ping", value="You will play Ping-Pong with Zeroppe", inline=False)
#    await ctx.send(embed=embed)

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
