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
            await message.channel.send ("uhhh...")  # normal text
            await message.channel.send (file=discord.File (r'C:\\Users\\91800\\Desktop\\something\\storyteller\\images\\1.png'))
            # for image
            await asyncio.sleep(5)
            f = open(r'C:\\Users\\91800\\Desktop\\something\\storyteller\\text\\1.txt', 'r')
            text = f.read()
            f.close()
            await message.channel.send(text) # for text in a txt file


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

client.run('token')
