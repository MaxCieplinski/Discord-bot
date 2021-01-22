import discord
from discord.ext import commands

class Silence(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def silence(self, ctx):
		await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
		await ctx.message.add_reaction('✅')

	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def unsilence(self, ctx):
		await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
		await ctx.message.add_reaction('✅')

	@silence.error
	async def silence_error(self, ctx, error):
		if ctx.message.author.guild_permissions.ban_members:
			await ctx.message.add_reaction('❌')
		else:
			pass

	@silence.error
	async def unsilence_error(self, ctx, error):
		if ctx.message.author.guild_permissions.ban_members:
			await ctx.message.add_reaction('❌')
		else:
			pass

def setup(client):
	client.add_cog(Silence(client))