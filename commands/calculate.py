import discord
from discord.ext import commands

import calculation
'''
USED LIBRARY CALCULATOR WHICH I MADE IN A DIFFERENT REPO (https://github.com/MaxCieplinski/Calculator)
'''

class Calculate(commands.cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def calculate(self, ctx, equation):
        try:
            result = calculation.Calculations.calculate(equation)
        except:
            result = "Error"

        embed = discord.Embed(
            title = f'Calculation : `{equation}`',
            description = f'Result : \n ```{result}```',
            color = discord.Color.blurple()
        )

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Calculate(client))