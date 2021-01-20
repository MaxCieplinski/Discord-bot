import discord
from discord.ext import commands
import json

class Roles(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def roles(self, ctx):
		emotes = {'Assembly': '<:Assembly:798519446318481418>', 'Python': '<:Python:798519446967812096>', 'C_lang': '<:C_lang:798519446004039692>', 'Cpp': '<:Cpp:798519446263169035>', 'Csharp': '<:Csharp:798519446570139658>', 'Kotlin': '<:Kotlin:798519446364880949>', 'Swift': '<:Swift:798519446733062155>', 'Php': '<:Php:798519446682599445>', 'Typescript': '<:Typescript:798519446813016064>', 'Lua': '<:Lua:798519446767009792>', 'Rust': '<:Rust:798519446759145482>', 'Ruby': '<:Ruby:798519446510895155>', 'Visual basic': '<:Visualbasic:798519446603431968>', 'Elixir': '<:Elixir:798519446511419453>', 'Go': '<:Go:798519446296985601>', 'Javascript': '<:Javascript:798519446490316800>', 'Java': '<:Java:798519446486253628>', 'Haskell': '<:Haskell:798519446197108738>', 'Sql': '<:Sql:798519446503292980>', 'Dart': '<:Dart:798678123746557952>'}
		emotes = {key: value for key, value in sorted(emotes.items(), key = lambda item: item[1])}
		emotes = dict((value, key) for key, value in emotes.items())
		emotes = [item for pair in emotes.items() for item in pair]
		embed = discord.Embed(
			title = 'Available roles',
			description = f"Please take roles of programming languages you actually know as everyone can see the same chanels and the roles are purely for information purposes. \n \n {emotes[0]} {emotes[1]} \n {emotes[2]} {emotes[3]} \n {emotes[4]} {emotes[5]} \n {emotes[6]} {emotes[7]} \n {emotes[8]} {emotes[9]} \n {emotes[10]} {emotes[11]} \n {emotes[12]} {emotes[13]} \n {emotes[14]} {emotes[15]} \n {emotes[16]} {emotes[17]} \n {emotes[18]} {emotes[19]} \n {emotes[20]} {emotes[21]} \n {emotes[22]} {emotes[23]} \n {emotes[24]} {emotes[25]} \n {emotes[26]} {emotes[27]} \n {emotes[28]} {emotes[29]} \n {emotes[30]} {emotes[31]} \n {emotes[32]} {emotes[33]} \n {emotes[34]} {emotes[35]} \n {emotes[36]} {emotes[37]} \n {emotes[38]} {emotes[39]}",
			color = discord.Color.blurple()
		)

		message = await ctx.send(embed=embed)
		
		await message.add_reaction(emotes[0])
		await message.add_reaction(emotes[2])
		await message.add_reaction(emotes[4])
		await message.add_reaction(emotes[6])
		await message.add_reaction(emotes[8])
		await message.add_reaction(emotes[10])
		await message.add_reaction(emotes[12])
		await message.add_reaction(emotes[14])
		await message.add_reaction(emotes[16])
		await message.add_reaction(emotes[18])
		await message.add_reaction(emotes[20])
		await message.add_reaction(emotes[22])  
		await message.add_reaction(emotes[24])  
		await message.add_reaction(emotes[26])  
		await message.add_reaction(emotes[28])  
		await message.add_reaction(emotes[30])  
		await message.add_reaction(emotes[32])  
		await message.add_reaction(emotes[34])  
		await message.add_reaction(emotes[36])  
		await message.add_reaction(emotes[38])   

	async def change_roles(self, reaction, value : bool):
		guild = self.client.get_guild(reaction.guild_id)
		member = discord.utils.get(guild.members, id=reaction.user_id)
		emoji = str(reaction.emoji)
		emotes = {'Assembly': '<:assembly:798519446318481418>', 'Python': '<:python:798519446967812096>', 'C': '<:c_lang:798519446004039692>', 'C++': '<:cpp:798519446263169035>', 'C#': '<:csharp:798519446570139658>', 'Kotlin': '<:kotlin:798519446364880949>', 'Swift': '<:swift:798519446733062155>', 'Php': '<:php:798519446682599445>', 'Typescript': '<:typescript:798519446813016064>', 'Lua': '<:lua:798519446767009792>', 'Rust': '<:rust:798519446759145482>', 'Ruby': '<:ruby:798519446510895155>', 'Visual basic': '<:visualbasic:798519446603431968>', 'Elixir': '<:elixir:798519446511419453>', 'Go': '<:go:798519446296985601>', 'JavaScript': '<:javascript:798519446490316800>', 'Java': '<:java:798519446486253628>', 'Haskell': '<:haskell:798519446197108738>', 'Sql': '<:sql:798519446503292980>', 'Dart': '<:dart_lang:798678123746557952>'}
		emotes = {key: value for key, value in sorted(emotes.items(), key = lambda item: item[1])}
		emotes = dict((value, key) for key, value in emotes.items())
		role_name = emotes.get(emoji)
		print(emotes)
		print(member, role_name, emoji)
		if None not in (member, role_name):
			print('0')
			role = discord.utils.get(guild.roles, name=role_name)
			print(role)
			if value:
				await member.add_roles(role)
			else:
				await member.remove_roles(role)
		

	@commands.Cog.listener()
	async def on_raw_reaction_add(self, reaction):
		if reaction.channel_id == 798618801016537178:
		   await self.change_roles(reaction, True)

	@commands.Cog.listener()
	async def on_raw_reaction_remove(self, reaction):
		if reaction.channel_id == 798618801016537178:
			await self.change_roles(reaction, False)

def setup(client):
	client.add_cog(Roles(client))