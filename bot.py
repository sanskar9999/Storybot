# This example requires the 'message_content' intent.
import discord
import asyncio

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        if message.author == client.user:
            return

        if message.content.startswith('!help'):
            await message.channel.send("type  !story  for an interactive story \n(thats all i do for now)")

        if message.content.startswith('!story'):    # if the !story command has been sent
            await message.channel.send ("scenario 1")  # normal text
            await message.channel.send ("https://cdn.discordapp.com/attachments/1113823013872357476/1113823546288910447/1.png")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

client.run('token')
