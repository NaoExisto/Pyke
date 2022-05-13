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

bot = commands.Bot(command_prefix='.', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def repeat(ctx, times: int, content='cala a boca macaco'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send('{0.name} joined in {0.joined_at}'.format(member))

@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')

@bot.command(name='bj')
async def bj(ctx):
    await ctx.send('===== Black Jack =====')
    nome1 = ''
    nome2 = ''
#==========================================================================================================
    while nome1 == '':
        await ctx.send('Digite o nome do jogador 1 /30sec')

        def check(m: discord.Message):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id 

        try:

            nome1 = await bot.wait_for(event = 'message', check = check, timeout = 30.0)
            
        except asyncio.TimeoutError:
            await ctx.send(f"**{ctx.author}**, you didn't send any message that meets the check in this channel for 60 seconds..")
            return

        await ctx.send(f"**{ctx.author}**, you responded with {nome1.content}!")

#==========================================================================================================
    while nome2 == '':
        await ctx.send('Digite o nome do jogador 2 /30sec')

        def check(m: discord.Message):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id 

        try:

            nome2 = await bot.wait_for(event = 'message', check = check, timeout = 30.0)
            
        except asyncio.TimeoutError: 
            await ctx.send(f"**{ctx.author}**, you didn't send any message that meets the check in this channel for 60 seconds..")
            return

        await ctx.send(f"**{ctx.author}**, you responded with {nome1.content}!")

#==========================================================================================================

    PlayAgain = 1

    while PlayAgain == 1:

        inicial1 = random.randint(1, 11)
        inicial2 = random.randint(1, 11)

        stand1 = False
        stand2 = False

        while inicial1 <= 21 and stand1 != True:

            await ctx.send(f'O {nome1.content} está com {inicial1}')
            await ctx.send('Digite HIT caso deseje comprar mais uma carta e STAND caso queria terminar.')
            escolha = await bot.wait_for(event = 'message', check=check,timeout=20)


            if escolha.content.lower() == 'hit':

                inicial1 = inicial1 + random.randint(1, 11)

            elif escolha.content.lower() == 'stand':
                        
                stand1 = True

        stand1 = True
        escolha = 0

        while inicial2 <= 21 and stand1 == True and stand2 != True:

            await ctx.send(f'O {nome1} está com {inicial1}')
            await ctx.send(f'O {nome2} está com {inicial2}')

            escolha = await bot.wait_for(event = 'message', check=check,timeout=20)

            if escolha == 1:

                inicial2 = inicial2 + random.randint(1, 11)

            elif escolha == 2:

                stand2 = True

        if inicial1 > 21:
                    
            await ctx.send('{} rebentou!'.format(nome1))
            await ctx.send('{} venceu!'.format(nome2))

        elif inicial2 > 21:

            await ctx.send('{} rebentou!'.format(nome2))
            await ctx.send('{} ganhou'.format(nome1))

        elif inicial1 > inicial2:

            print('Parabêns {} por ganhar o jogo'.format(nome1))

        elif inicial2 > inicial1:

            print('Parabêns {} por ganhar o jogo'.format(nome2))

        elif inicial1 == inicial2:

            print('Deu empate')

        print('Deseja joga novamente?\nDigite 1 para jogar novamente e 2 para parar.')
        PlayAgain = int(input())

        if PlayAgain == 1:
            PlayAgain = 1
            
        elif PlayAgain == 2:
            print('Obrigado por jogar!')
            PlayAgain = 2

        else:
            print('Alternativa inesxistente!')

bot.run(TOKEN)