import discord
from discord.ext import commands
import random

class Coinflip(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['cf'])
    async def coinflip(self, ctx, side = None):
        choice = random.choice(['tails', 'heads'])
        if side != None:
            side.lower()
            if side == 'tails' or 'heads':
                if choice == 'tails' and side == 'tails':
                    embed = discord.Embed(
                        title = '✅ Correct! ✅',
                        description =  'It was tails!',
                        color = discord.Color.blurple()
                    )

                    await ctx.send(embed=embed)
                elif choice == 'heads' and side == 'heads':
                    embed = discord.Embed(
                        title = '✅ Correct! ✅',
                        description =  'It was heads!',
                        color = discord.Color.blurple()
                    )

                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(
                        title = '❌ Incorrect! ❌',
                        description = f"It was {'tails' if side == 'heads' else 'heads'}!",
                        color = discord.Color.blurple()
                    )

                    await ctx.send(embed=embed)

        else:
            embed = discord.Embed(
                title = f'{choice}',
                color = discord.Color.blurple()
            )

            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Coinflip(client))