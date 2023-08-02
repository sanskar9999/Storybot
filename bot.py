import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Other necessary variables and data structures
is_story_running = False
story_chapter = 0
story_options = {}

# Full story data
story = [
    {
        "text": "You are an adventurer exploring the ancient ruins of a forgotten city. As you wander through the ruins, you spot two paths before you. Which path will you choose?",
        "options": {
            "\U0001F1E6": 1,  # If user selects Option A, go to Scenario 1
            "\U0001F1E7": 2   # If user selects Option B, go to Scenario 2
        },
        "images": []
    },
    {
        "text": "Scenario 1: You follow the path on the left and come across a dark cave. Will you enter the cave or continue exploring the ruins?",
        "options": {
            "\U0001F1E6": 3,  # If user selects Option A, go to Scenario 3
            "\U0001F1E7": 4   # If user selects Option B, go to Scenario 4
        },
        "images": []
    },
    {
        "text": "Scenario 2: You choose the path on the right and encounter a massive stone door. Do you try to open the door or turn back?",
        "options": {
            "\U0001F1E6": 5,  # If user selects Option A, go to Scenario 5
            "\U0001F1E7": 6   # If user selects Option B, go to Scenario 6
        },
        "images": []
    },
    {
        "text": "Scenario 3: You enter the dark cave and find a hidden passage that leads to a room full of treasures! Congratulations, you found the mysterious treasure!",
        "options": {},
        "images": []
    },
    {
        "text": "Scenario 4: You decide to continue exploring the ruins, but unfortunately, you get lost and never find the treasure.",
        "options": {},
        "images": []
    },
    {
        "text": "Scenario 5: You attempt to open the massive stone door, but it triggers a trap, and you are captured by ancient guardians. You never find the treasure.",
        "options": {},
        "images": []
    },
    {
        "text": "Scenario 6: You wisely choose to turn back and continue exploring the ruins. Eventually, you stumble upon a hidden chamber containing the mysterious treasure!",
        "options": {},
        "images": []
    },
]

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def story_help(ctx):
    # Provide a list of available commands here
    await ctx.send("List of available commands:\n"
                   "!story_help - Show available commands\n"
                   "!begin_story - Start the interactive story\n"
                   "!restart_story - Restart the interactive story")

@bot.command()
async def begin_story(ctx):  # Renamed the story command to begin_story
    global is_story_running, story_chapter, story_options
    if is_story_running:
        await ctx.send("The story is already running.")
    else:
        is_story_running = True
        story_chapter = 0
        story_options = story[story_chapter]["options"]
        await ctx.send(story[story_chapter]["text"])
        await show_options(ctx)

@bot.command()
async def restart_story(ctx):
    global is_story_running, story_chapter, story_options
    is_story_running = False
    story_chapter = 0
    story_options = {}
    await ctx.send("The story has been reset. You can now start a new adventure with !begin_story.")

async def show_options(ctx):
    options_text = "\n".join([f"{emoji}: {option}" for emoji, option in story_options.items()])
    message = await ctx.send(options_text)

    for emoji in story_options.keys():
        await message.add_reaction(emoji)

@bot.event
async def on_reaction_add(reaction, user):
    global is_story_running, story_chapter, story_options

    if user.bot:  # Ignore reactions from bots
        return

    if is_story_running:
        if reaction.emoji in story_options.keys():
            next_chapter = story_options[reaction.emoji]
            if 0 <= next_chapter < len(story):
                story_chapter = next_chapter
                story_options = story[story_chapter]["options"]
                await reaction.message.channel.send(story[story_chapter]["text"])
                if story_options:  # If there are more options, show them
                    await show_options(reaction.message.channel)
                else:
                    await reaction.message.channel.send("The story has ended.")
                    is_story_running = False
        else:
            await reaction.message.channel.send("Invalid option. Please choose a valid option.")

# Run the bot with the provided token
bot.run("token")
