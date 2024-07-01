# bot.py
import os
import random
from dotenv import load_dotenv

# 1
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# 2
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

tree_cls = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@tree_cls.command(name='test', description='Test command')
async def test(interaction):
    responses = [
        'I am here.',
        'Hello!',
        'I am alive.',
        'Yes?',
        'What do you want?',
        'I am listening.',
        'I am ready.',
        'I am ready to serve.',
        'Whats good?'
    ]
    await interaction.response.send_message(random.choice(responses))

if __name__=='__main__':
    client.run(TOKEN)
