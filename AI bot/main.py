import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def credits(ctx):
    await ctx.send("Помог сделать код: Фарид  |aka|  captain_anonymous")

@bot.command()
async def check(ctx):
    if len(ctx.message.attachments) > 0:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f'./images/{file_name}')
            await ctx.send("Картинка сохранена!")

            class_name = get_class(f'./images/{file_name}')
            await ctx.send(class_name)

    else:
        await ctx.send("Вы забыли прикрепить фото")


bot.run('MTEwOTM4NDY1ODgyNDcyNDU0MA.G7vV5E.WLKICCt6Vwec6DwJ9a464bMcpfJWBfS0WPShwc')