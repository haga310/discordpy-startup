from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
InMember=[]

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command()
async def InsiderAdd(ctx):
    await ctx.send(f"{ctx.author.mention}さんをインサイダーゲームのプレイヤーに追加しました。")
    InMember.append(str(ctx.author.mention))

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def tell(ctx):
    await ctx.send('そんなキーワードは　ぜろっぺだよ')        
    
    
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
