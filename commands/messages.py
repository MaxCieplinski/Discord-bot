import discord
from discord.ext import commands
import json

class Messages(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if 'discord.gg/' in message.content.lower() or 'https://discord.com/api/' in message.content.lower():
            await message.delete()

        with open('data.json', 'r') as f:
            data = json.load(f)

        if f"{message.guild.name} ({message.guild.id})" not in data:
            data[f"{message.guild.name} ({message.guild.id})"] = {}
            data[f"{message.guild.name} ({message.guild.id})"]["Muted"] = []
            data[f"{message.guild.name} ({message.guild.id})"]["Banned"] = []
            data[f"{message.guild.name} ({message.guild.id})"]["Server_id"] = message.guild.id
            
        if f"{message.author.name} ({message.author.id})" not in data[f"{message.guild.name} ({message.guild.id})"]:
            data[f"{message.guild.name} ({message.guild.id})"][f"{message.author.name} ({message.author.id})"] = {}
            data[f"{message.guild.name} ({message.guild.id})"][f"{message.author.name} ({message.author.id})"]['Messages'] = 0

        data[f"{message.guild.name} ({message.guild.id})"][f"{message.author.name} ({message.author.id})"]['Messages'] += 1
        with open('data.json', 'w') as f:
            json.dump(data, f)

def setup(client):
    client.add_cog(Messages(client))