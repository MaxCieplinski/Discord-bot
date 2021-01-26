import discord
from discord.ext import commands
import asyncio

class Write(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def write(self, ctx, time, *, words):
        if time.isdecimal():
            await asyncio.sleep(int(time)*60)
            await ctx.send(''.join(words))
        else:
            words.append(time)
            await ctx.send(''.join(words))

def setup(client):
    client.add_cog(Write(client))