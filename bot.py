import discord
import asyncio
import random

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        if message.author == client.user:
            return

        if message.content.startswith('!help'):
            await message.channel.send("type  !story  for an interactive story \n(thats all i do for now)")

        if message.content.startswith('!story'):    
            await self.start_story(message.channel) # call a function to start the story

    async def start_story(self, channel):
        # define the scenarios and options as dictionaries
        scenarios = {
            1: ("scenario 1", "https://cdn.discordapp.com/attachments/1113823013872357476/1113823546288910447/1.png"),
            2: ("scenario 2", "https://cdn.discordapp.com/attachments/1113823013872357476/1113823546288910447/2.png"),
            3: ("scenario 3", "https://cdn.discordapp.com/attachments/1113823013872357476/1113823546288910447/3.png"),
            4: ("scenario 4", "https://cdn.discordapp.com/attachments/1113823013872357476/1113823546288910447/4.png"),
            5: ("scenario 5", "https://cdn.discordapp.com/attachments/1113823013872357476/1113823546288910447/5.png")
        }

        options = {
            1: ("option A", "option B"),
            2: ("option C", "option D"),
            3: ("option E", "option F"),
            4: ("option G", "option H"),
            5: ("option I", "option J")
        }

        # define the emojis for different options
        emojis = {
            "A": "\U0001F1E6",
            "B": "\U0001F1E7",
            "C": "\U0001F1E8",
            "D": "\U0001F1E9",
            "E": "\U0001F1EA",
            "F": "\U0001F1EB",
            "G": "\U0001F1EC",
            "H": "\U0001F1ED",
            "I": "\U0001F1EE",
            "J": "\U0001F1EF"
        }

        # choose a random scenario and option pair
        scenario_id = random.randint(1, len(scenarios))
        scenario_text, scenario_image = scenarios[scenario_id]
        option_text_1, option_text_2 = options[scenario_id]

        # send the scenario and options as an embed with image
        embed = discord.Embed(title=scenario_text, color=0x00ff00)
        embed.set_image(url=scenario_image)
        embed.add_field(name="Choose one:", value=f"{emojis[option_text_1[-1]]} {option_text_1}\n{emojis[option_text_2[-1]]} {option_text_2}", inline=False)
        message = await channel.send(embed=embed)

        # add the emojis as reactions to the message
        await message.add_reaction(emojis[option_text_1[-1]])
        await message.add_reaction(emojis[option_text_2[-1]])

        # wait for a reaction from the user
        def check(reaction, user):
            return user != client.user and reaction.message.id == message.id and str(reaction.emoji) in emojis.values()

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send("Sorry, you took too long to choose.")
        else:
            # get the option letter from the emoji
            option_letter = list(emojis.keys())[list(emojis.values()).index(str(reaction.emoji))]
            
            # send a response based on the option chosen
            if option_letter == option_text_1[-1]:
                await channel.send(f"You chose {option_text_1}.")
                # do something based on the option chosen
                # ...
                
            elif option_letter == option_text_2[-1]:
                await channel.send(f"You chose {option_text_2}.")
                # do something based on the option chosen
                # ...

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

client.run('token')
