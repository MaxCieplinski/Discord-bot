import discord
from discord.ext import commands
import os
import time
import json
import datetime
import asyncio

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

for file_name in os.listdir('./commands'):
    if file_name.endswith('.py'):
        client.load_extension(f'commands.{file_name[:-3]}')

async def wait_unmute(member : discord.Member, time, role):
    await syncio.sleep(time)
    await member.remove_roles(role)

async def wait_unban(member : discord.Member, time, role, guild):
    await asyncio.sleep(time)
    await guild.unban(member)

@client.event
async def on_ready():
    with open('data.json', 'r') as f:
	    data = json.load(f)

    for server in data:
        for category in data[server]:
            if category == "Muted":
                for index, muted in enumerate(data[server][category]):
                    if datetime.datetime.strptime(data[server][category][index][1], '%Y-%m-%d %H:%M:%S') < datetime.datetime.now():
                        guild = client.get_guild(data[server]["Server_id"])
                        member = guild.get_member(data[server][category][index][0])
                        role = discord.utils.get(member.guild.roles, name='Muted')
                        await member.remove_roles(role)
                        del data[server][category][index]
                    else:
                        time = datetime.datetime.now() - datetime.datetime.strptime(data[server][category][index][1], '%Y-%m-%d %H:%M:%S')
                        await wait_unmute(member, time.total_seconds(), role)
            elif category == "Banned":
                for index, banned in enumerate(data[server][category]):
                    if datetime.datetime.strptime(data[server][category][index][1], '%Y-%m-%d %H:%M:%S') < datetime.datetime.now():
                        guild = client.get_guild(data[server]["Server_id"])
                        member = guild.get_member(data[server][category][index][0])
                        await guild.unban(member)
                        del data[server][category][index]
                    else:
                        time = datetime.datetime.now() - datetime.datetime.strptime(data[server][category][index][1], '%Y-%m-%d %H:%M:%S')
                        await wait_unban(member, time.total_seconds(), role, guild)
    with open('data.json', 'w') as f:
	    json.dump(data, f)

client.run('')