#!/usr/bin/python
import discord
from discord.ext import commands
import asyncio
import mispsearch


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=intents)


@bot.event
async def on_ready():
    print("Online")
    return await bot.change_presence(activity=discord.Activity(type=0,name='MISP',url='https://www.misp-project.org/'))


@bot.command()
async def search(ctx,arg):
    await ctx.message.add_reaction("✅")
    discord_message = mispsearch.search_misp_attributes(arg)
    await ctx.reply(discord_message)
    print(ctx.guild.id)
    print(ctx.guild.name)

bot.run("KEYKEYKEY")
