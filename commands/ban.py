import discord
from discord.ext import commands
import json
import datetime
import asyncio

class Ban(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.has_permissions(ban_members=True)
	@commands.command()
	async def ban(self, ctx, member : discord.Member, *, reason = 'Not specified'):
		with open('data.json', 'r') as f:
			data = json.load(f)

		for idx, i in enumerate(data[f"{ctx.message.guild.name} ({ctx.message.guild.id})"]["Banned"]):
			if i[0] == str(member.id):
				del data[f"{ctx.message.guild.name} ({ctx.message.guild.id})"]["Banned"][idx]

		with open('data.json', 'w') as f:
			json.dump(data, f)

		await ctx.message.add_reaction('✅')
		await self.client.get_channel(797787010113863721).send(f'`{member}` got banned by `{ctx.author}`. Reason = {reason}')
		await member.send(f'You got banned from `{ctx.message.guild.name}`. Reason = {reason}')
		await member.ban(reason = reason)

	@commands.has_permissions(ban_members=True)
	@commands.command()
	async def tempban(self, ctx, member : discord.Member, time : int = None, *, reason = 'Not specified'):
		if time != None and isinstance(time, int):
			await ctx.message.add_reaction('✅')
			await self.client.get_channel(797787010113863721).send(f'`{member}` got banned for {time} minutes by `{ctx.author}`. Reason = {reason}')
			await member.send(f'You got banned for {time}from `{ctx.message.guild.name}`. Reason = {reason}')

			with open('data.json', 'r') as f:
				data = json.load(f)

			changed = False
			unban_time = datetime.datetime.now() + datetime.timedelta(minutes=time)
			unban_time.strftime("%Y-%m-%d %H:%M:%S")

			for idx, i in enumerate(data[f"{ctx.message.guild.name} ({ctx.message.guild.id})"]["Banned"]):
				if i[0] == str(member.id):
					i[1] = unban_time
					changed = True

			if changed == False:
				data[f"{ctx.message.guild.name} ({ctx.message.guild.id})"]["Banned"].append([str(member.id), str(unban_time), str(ctx.message.guild.id)])

			await member.ban(reason = reason)

			with open('data.json', 'w') as f:
				json.dump(data, f)

			with open('data.json', 'r') as f:
				data = json.load(f)

			await asyncio.sleep(time * 60)
			for idx, i in enumerate(data[f"{ctx.message.guild.name} ({ctx.message.guild.id})"]["Banned"]):
				if i[0] == str(member.id):
					await member.unban()
					del data[f"{ctx.message.guild.name} ({ctx.message.guild.id})"]["Banned"][idx]

			with open('data.json', 'w') as f:
				json.dump(data, f)
		else:
			await ctx.message.add_reaction('❌')

	@ban.error
	async def ban_error(self, ctx, error):
		if ctx.message.author.guild_permissions.ban_members:
			await ctx.message.add_reaction('❌')
		else:
			pass

	@tempban.error
	async def tempban_error(self, ctx, error):
		raise error
		if ctx.message.author.guild_permissions.ban_members:
			await ctx.message.add_reaction('❌')
		else:
			pass

def setup(client):
	client.add_cog(Ban(client))