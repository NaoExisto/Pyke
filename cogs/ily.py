from discord.ext import commands
import discord

class ily(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ily(self, ctx, times: int, content = 'Eu te amo S2'):
        """Repete a determinada de vezes oque estiver escrito em 'content'."""
        for i in range(times):
            await ctx.send(content)

def setup(bot):
    bot.add_cog(ily(bot))