from discord.ext import commands
import random
import discord
import asyncio

class BlackJack(commands.Cog):
    """Blacjack game."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def blackjack(self, ctx):
        await ctx.send('===== Black Jack =====')
        nome1 = ''
        nome2 = ''
#==========================================================================================================
        while nome1 == '':
            await ctx.send('Digite o nome do jogador 1 /30sec')

            def check(m: discord.Message):
                return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id 

            try:

                nome1 = await commands.wait_for(event = 'message', check = check, timeout = 30.0)
                
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

                nome2 = await commands.wait_for(event = 'message', check = check, timeout = 30.0)
                
            except asyncio.TimeoutError: 
                await ctx.send(f"**{ctx.author}**, you didn't send any message that meets the check in this channel for 60 seconds..")
                return

            await ctx.send(f"**{ctx.author}**, you responded with {nome1.content}!")

    #==========================================================================================================

        PlayAgain = 'sim'

        while PlayAgain == 'sim':

            inicial1 = random.randint(1, 11)
            inicial2 = random.randint(1, 11)

            stand1 = False
            stand2 = False

            while inicial1 <= 21 and stand1 != True:

                await ctx.send(f'O {nome1.content} está com {inicial1}')
                await ctx.send('Digite HIT caso deseje comprar mais uma carta e STAND caso queria terminar.')
                escolha = await commands.wait_for(event = 'message', check=check,timeout=20)


                if escolha.content.lower() == 'hit':

                    inicial1 = inicial1 + random.randint(1, 11)

                elif escolha.content.lower() == 'stand':
                            
                    stand1 = True

            stand1 = True
            escolha = 0

            while inicial2 <= 21 and stand1 == True and stand2 != True:

                await ctx.send(f'O {nome1} está com {inicial1}')
                await ctx.send(f'O {nome2} está com {inicial2}')

                escolha = await commands.wait_for(event = 'message', check=check,timeout=20)

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

                await ctx.send('Parabêns {} por ganhar o jogo'.format(nome1))

            elif inicial2 > inicial1:

                await ctx.send('Parabêns {} por ganhar o jogo'.format(nome2))

            elif inicial1 == inicial2:

                await ctx.send('Deu empate')

            await ctx.send('Deseja joga novamente?\nDigite SIM para jogar novamente e NÃO para parar.')
            PlayAgain = await commands.wait_for(event = 'message', check = check, timeout = 20.0)

            if PlayAgain.content.lower() == 'sim':
                PlayAgain = 'sim'
                
            elif PlayAgain.content.lower() == 'não' or 'nao':
                await ctx.send('Obrigado por jogar!')
                PlayAgain = 'nao'

def setup(bot):
    bot.add_cog(BlackJack(bot))