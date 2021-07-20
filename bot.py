import discord
import os
import requests
import json
import random

TOKEN = os.getenv('TOKEN')

client = discord.Client()  # this is the connection with the discord

# list with sad words
sad_words = ['sad', 'depressed', 'unhappy', 'angry', 'miserable',
             ' blue', 'triste', 'chateado', 'depressivo', 'pra baixo', 'magoado', 'tristinho', 'down']

starter_encouragements = [
    "Se motiva, maan! A vida realmente tem seus altos e baixos",
    "A vida é assim, só continua indo em frente",
    "Quer falar sobre? Então que tal ligar pra aquele seu amigo?",
    "Cara...foda...",
    "Pior...",
    "O que faço nessas horas é jogar um videogame pra dar uma animada geral!",
    "E que tal ler um livro novo, /bot?",
    "Porque não espairece a cabeça assistindo aquela série na Netflix?",
    "Bota aquele projetinho que vc engavetou em prática! Vai ajudar a pensar"
]

inspire = [
    'conselho', 'dicas', 'inspiração'
]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)


@client.event
async def on_ready():
    print(f'{client.user} conectou com o Discord!!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if any(word in msg for word in inspire):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

        # .env for declaring environment variables
# substitute your Token right here
client.run('TOKEN')
