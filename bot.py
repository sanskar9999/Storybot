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

# Sample story data (You can customize this)
story = [
    {
        "text": "Once upon a time, you find yourself standing at a crossroad.",
        "options": {
            "\U0001F1E6": "Go left",
            "\U0001F1E7": "Go right"
        },
        "images": [
            "image_url_here"
        ]
    },
    {
        "text": "You encounter a magical forest. What will you do?",
        "options": {
            "\U0001F1E8": "Explore the forest",
            "\U0001F1E9": "Leave the forest"
        },
        "images": []
    }
]

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def story_help(ctx):
    # Provide a list of available commands here
    await ctx.send("List of available commands:\n"
                   "!story_help - Show available commands\n"
                   "!begin_story - Start the interactive story")

@bot.command()
async def begin_story(ctx):  # Renamed the story command to begin_story
    global is_story_running, story_chapter, story_options
    if is_story_running:
        await ctx.send("The story is already running. Type !continue to proceed.")
    else:
        is_story_running = True
        story_chapter = 0
        story_options = story[story_chapter]["options"]
        await ctx.send(story[story_chapter]["text"])
        await show_options(ctx)

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
            story_chapter += 1
            if story_chapter < len(story):
                story_options = story[story_chapter]["options"]
                await reaction.message.channel.send(story[story_chapter]["text"])
                await show_options(reaction.message.channel)
            else:
                await reaction.message.channel.send("The story has ended.")
                is_story_running = False
        else:
            await reaction.message.channel.send("Invalid option. Please choose a valid option.")

# Run the bot with the provided token
bot.run(token)

# PS: my code finally works as intended omg iam so happy literally cheering
