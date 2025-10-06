import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")
print(f"Token carregado: {token}")

permissoes= discord.Intents.default()
permissoes.message_content = True
permissoes.members = True
HazeNexus = commands.Bot(command_prefix='/HZ', intents=permissoes)

@HazeNexus.command()
async def ola(ctx):
    await ctx.send('Olá! Eu sou o Haze Nexus, seu assistente virtual. Como posso ajudar você hoje?')


@HazeNexus.event
async def on_ready():
    print("Estou Pronto!")


HazeNexus.run(token) 
