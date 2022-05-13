from tabnanny import check
import discord
from discord.ext import commands
import random
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

comandos = [
    'cogs.blackjack',
    'cogs.ily',
]

bot = commands.Bot(command_prefix='.', description=description)

@bot.event
async def on_ready():
    print('Estou online!')
    print(bot.user.name)
    print(bot.user.id)
    print(13*'=')

@bot.command(name='reload', hidden=True)
async def _reload(self, *, module : str):
    """Reloads a module."""
    try:
        self.bot.unload_extension(module)
        self.bot.load_extension(module)
    except Exception as e:
        await self.send('\N{PISTOL}')
        await self.send('{}: {}'.format(type(e).__name__, e))
    else:
        await self.send('\N{OK HAND SIGN}')

for extension in comandos:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Falha em carregar o comando {}\n{}: {}'.format(extension, type(e).__name__, e))

bot.run(TOKEN)