import discord
from discord.ext import commands

class Invite(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(
            title = 'Invite link',
            description = 'In order to invite me to your server, click the link below \n \n [Invite me!](https://discord.com/api/oauth2/authorize?client_id=797832568665145354&permissions=8&scope=bot)',
            color = discord.Color.blurple()
        )

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Invite(client))