import discord
from discord.ext import commands

client = commands.Bot(command_prefix="")

@client.event
async def on_ready():
    print("Bot is ready")
@client.command()
async def hello(ctx):
    await ctx.send("hi owner :D")

client.run("ODQ4MTc5ODkxNTI5NzExNjI3.YLI3FA.7GxK14PB518PUMtcCtbKpQl25Io")
