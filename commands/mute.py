import discord
from discord.ext import commands
import json
import datetime
import asyncio

class Mute(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.has_permissions(kick_members=True)
	@commands.command()
	async def mute(self, ctx, member : discord.Member, *, reason = 'Not specified'):
		with open('data.json', 'r') as f:
			data = json.load(f)

		for idx, i in enumerate(data[f"{ctx.message.guild.name} ({ctx.message.guild.id})"]["Muted"]):
			if i[0] == str(member.id):
				del data[f"{ctx.message.guild.name} ({ctx.message.guild.id})"]["Muted"][idx]

		with open('data.json', 'w') as f:
			json.dump(data, f)

		await ctx.message.add_reaction('✅')
		await self.client.get_channel(797787010113863721).send(f'`{member}` got muted by `{ctx.author}`. Reason = {reason}')
		role = discord.utils.get(member.guild.roles, name='Muted')
		await member.add_roles(role)

	@commands.has_permissions(kick_members=True)
	@commands.command()
	async def unmute(self, ctx, member : discord.Member):
		role = discord.utils.get(member.guild.roles, name='Muted')
		if role not in member.roles:
			await ctx.message.add_reaction('✅')
			await self.client.get_channel(797787010113863721).send(f'`{member}` got unmuted by `{ctx.author}`')

			with open('data.json', 'r') as f:
				data = json.load(f)

			for idx, i in enumerate(data[f"{ctx.message.guild.name} ({ctx.message.guild.id})"]["Muted"]):
				if i[0] == str(member.id):
					del data[f"{ctx.message.guild.name} ({ctx.message.guild.id})"]["Muted"][idx]
					break

			with open('data.json', 'w') as f:
				json.dump(data, f)

			await member.remove_roles(role)
		else:
			await ctx.message.add_reaction('❌')

	@commands.has_permissions(kick_members=True)
	@commands.command()
	async def tempmute(self, ctx, member : discord.Member, time : int = None, *, reason = 'Not specified'):
		if time != None and isinstance(time, int):
			await ctx.message.add_reaction('✅')
			await self.client.get_channel(797787010113863721).send(f'`{member}` got muted for {time} minutes by `{ctx.author}`. Reason = {reason}')
			role = discord.utils.get(member.guild.roles, name='Muted')

			with open('data.json', 'r') as f:
				data = json.load(f)

			changed = False
			unmute_time = datetime.datetime.now() + datetime.timedelta(minutes=time)
			unmute_time.strftime("%Y-%m-%d %H:%M:%S")

			for idx, i in enumerate(data[f"{ctx.message.guild.name} ({ctx.message.guild.id})"]["Muted"]):
				if i[0] == str(member.id):
					i[1] = str(unmute_time)
					changed = True

			if changed == False:
				data[f"{ctx.message.guild.name} ({ctx.message.guild.id})"]["Muted"].append([str(member.id), str(unmute_time), str(ctx.message.guild.id)])

			await member.add_roles(role)

			with open('data.json', 'w') as f:
				json.dump(data, f)

			with open('data.json', 'r') as f:
				data = json.load(f)

			await asyncio.sleep(time * 60)
			for idx, i in enumerate(data[f"{ctx.message.guild.name} ({ctx.message.guild.id})"]["Muted"]):
				if i[0] == str(member.id):
					await member.remove_roles(role)
					del data[f"{ctx.message.guild.name} ({ctx.message.guild.id})"]["Muted"][idx]

			with open('data.json', 'w') as f:
				json.dump(data, f)
		else:
			await ctx.message.add_reaction('❌')

	@mute.error
	async def mute_error(self, ctx, error):
		if ctx.message.author.guild_permissions.kick_members:
			await ctx.message.add_reaction('❌')
		else:
			pass

	@unmute.error
	async def unmute_error(self, ctx, error):
		if ctx.message.author.guild_permissions.kick_members:
			await ctx.message.add_reaction('❌')
		else:
			pass

	@tempmute.error
	async def tempmute_error(self, ctx, error):
		if ctx.message.author.guild_permissions.kick_members:
			await ctx.message.add_reaction('❌')
		else:
			pass

def setup(client):
	client.add_cog(Mute(client))