import discord
from discord.ext import commands

class Kick(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.has_permissions(kick_members=True)
	@commands.command()
	async def kick(self, ctx, member : discord.Member, *, reason = 'Not specified'):
		await ctx.message.add_reaction('✅')
		await self.client.get_channel(797787010113863721).send(f'`{member}` got kicked by `{ctx.author}`. Reason = {reason}')
		await member.send(f'You got kicked from `{ctx.message.guild.name}`. Reason = {reason}')
		await member.kick(reason = reason)

	@kick.error
	async def kick_error(self, ctx, error):
		if ctx.message.author.guild_permissions.kick_members:
			await ctx.message.add_reaction('❌')
		else:
			pass

def setup(client):
	client.add_cog(Kick(client))