import discord
from discord.ext import commands

class Log(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.client.get_channel(797787010113863721).send(f'`{member}` has joined.')
        embed = discord.Embed(
            title = 'Welcome',
            description = f"{member} has just joined! Let's welcome him warmly.",
            color = discord.Color.blurple()
        )
        embed.set_thumbnail(url=member.avatar_url)

        message = await self.client.get_channel(797780459026120717).send(embed=embed)
        await message.add_reaction("👋")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.client.get_channel(797787010113863721).send(f'`{member}` has left.')

def setup(client):
    client.add_cog(Log(client))