import discord
import asyncio
import randam
import json
import sys
@client.event
async def on_ready():
    print(f"Logged in as\n{client.user.name}\n{client.user.id}\n------")
@client.event
async def on_message(message):
    if message.author.bot:
        return
with open('F:/token.txt') as f:
    token = f.read()
client = discord.Client()
client.run(token)