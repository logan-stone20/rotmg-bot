import discord
import asyncio
from bs4 import BeautifulSoup
from search import player_search, item_search, guild_search
import sqlite3
import json

file = open("token.json")
data = file.read()
o = json.loads(data)
token = str(o["token"])


client = discord.Client()

@client.event
async def on_message(message):

    if message.content.startswith("?help"):
        response = '''Need help aquiring knowledge of the realm? \n
?playersearch **player name** \n
?guildsearch **guild name** \n
?itemsearch **item name** '''
        await message.channel.send(response)
                    

    if message.content.startswith("?playersearch "):
        await player_search(message)

    if message.content.startswith("?itemsearch "):
        await item_search(message)

    if message.content.startswith("?guildsearch "):
        await guild_search(message)

    if message.content.startswith("?addScoreboard"):
        print("yeey")
        
    if message.author == client.user:
        return

    

    

@client.event
async def on_ready():
    client.display_name = "Avalon the Archivist"
    print("logged in as " + str(client.user.name))
    game = discord.Game("in the Cursed Library | ?help")
    await client.change_presence(activity = game)


client.run(token)
