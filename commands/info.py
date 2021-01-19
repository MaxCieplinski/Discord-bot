import discord
from discord.ext import commands
import datetime

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def info(self, ctx, member : discord.Member = None):
        if member == None:
            embed = discord.Embed(
                title = f'{member}',
                description = '',
                color = discord.Color.blurple()
            )
            embed.add_field(name='Discord join date : ', value=f'{ctx.author.created_at.strftime("%b %d, %Y")} ({(datetime.datetime.now() - ctx.author.created_at).days} day/s)', inline=False)
            embed.add_field(name='Server join date : ', value=f'{ctx.author.joined_at.strftime("%b %d %Y")} ({(datetime.datetime.now() - ctx.author.joined_at).days} day/s)', inline=False)
            embed.set_thumbnail(url=ctx.author.avatar_url)

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(
                title = f'{member}',
                description = '',
                color = discord.Color.blurple()
            )
            embed.add_field(name='Discord join date : ', value=f'{member.created_at.strftime("%b %d, %Y")} ({(datetime.datetime.now() - member.created_at).days} day/s)', inline=False)
            embed.add_field(name='Server join date : ', value=f'{member.joined_at.strftime("%b %d %Y")} ({(datetime.datetime.now() - member.joined_at).days} day/s)', inline=False)
            embed.set_thumbnail(url=member.avatar_url)

            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Info(client))