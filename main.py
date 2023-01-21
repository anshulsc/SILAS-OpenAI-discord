from dotenv import load_dotenv
load_dotenv()

import os
import discord
import openai

def question(prompt: str) -> str:
    words = prompt.split()
    words = words[1:]
    return " ".join(words)



openai.api_key = os.getenv('OPENAI_API_KEY')

def chatgpt(prompt: str) -> str: 
    response = openai.Completion.create(
         engine="text-davinci-002", 
         prompt=prompt, 
         max_tokens=1024, 
         temperature=0.5,
         )
    print(response)
    return response['choices'][0]['text']


def ShowDallE(prompt: str) -> str:
    response = openai.Image.create(
        prompt= prompt,
         n=1,
         size="1024x1024"
         )
    return response['data'][0]['url']


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("CASE IS NOW ONLINE....")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("$Tell"):
        dprompt = question(message.content)
        await message.channel.send(chatgpt(dprompt))

    if message.content.startswith("$Show"):
        dprompt = question(message.content)
        await message.channel.send(ShowDallE(dprompt))
    


client.run(os.getenv("DISCORD_API_KEY"))