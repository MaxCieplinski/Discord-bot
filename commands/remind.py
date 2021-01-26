import discord
from discord.ext import commands

class Remind(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def remind(self, ctx, time, *,  words):
        if time.isdecimal():
            await asyncio.sleep(time*60)
            await ctx.send(f'Reminding {ctx.author.mention} : ' + ''.join(words))
        else:
            await ctx.send(f'Reminding {ctx.author.mention} : ' + ''.join(words))

def setup(client):
    client.add_cog(Remind(client))