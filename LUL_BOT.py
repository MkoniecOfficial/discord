import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = ".") #Initialise client bot


@client.event 
async def on_ready():
    print("Bot is online and connected to Discord") #This will be called when the bot connects to the server

@client.event
async def on_message(message):
    if message.content == "cookie":
        await client.send_message(message.channel, ":cookie:") #responds with Cookie emoji when someone says "cookie"
@client.event
async def on_message(message):
    if message.content == "Twitch":
        await client.send_message(message.channel, "https://www.twitch.tv/mkoniec") 
@client.event
async def on_message(message):
    if message.content == "YT":
        await client.send_message(message.channel, "https://www.youtube.com/channel/UCSpXYRrwGCLCWQMqtSjmbzA") 
		
@client.event
async def on_message(message):
    if message.content == "GR":
        await client.send_message(message.channel, "@here gracie ?") 
		
client.run("NDg4MDE0MjI5Mzk2Mzg5ODkw.DncBLw.95dWohkQpKfq9iKHlZ-0_TWSZZE") #Replace token with your bots token
