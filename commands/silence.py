import discord
from discord.ext import commands

class Silence(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def silence(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unsilence(self, ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)

def setup(client):
    client.add_cog(Silence(client))