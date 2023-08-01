import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.message_reactions = True

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
            "A": "Go left",
            "B": "Go right"
        },
        "images": [
            "image_url_here"
        ]
    },
    {
        "text": "You encounter a magical forest. What will you do?",
        "options": {
            "A": "Explore the forest",
            "B": "Leave the forest"
        },
        "images": []
    },
    # Add more story chapters here...
]

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
async def help(ctx):
    # Provide a list of available commands here
    await ctx.send("List of available commands:\n"
                   "!help - Show available commands\n"
                   "!story - Start the interactive story")

@bot.command()
async def story(ctx):
    global is_story_running, story_chapter, story_options
    if is_story_running:
        await ctx.send("The story is already running. Type !continue to proceed.")
    else:
        is_story_running = True
        story_chapter = 0
        story_options = story[story_chapter]["options"]
        await ctx.send(story[story_chapter]["text"])
        await show_options(ctx)

@bot.command()
async def continue_story(ctx, option: str):
    global is_story_running, story_chapter, story_options
    if is_story_running:
        if option.upper() in story_options:
            story_chapter += 1
            if story_chapter < len(story):
                story_options = story[story_chapter]["options"]
                await ctx.send(story[story_chapter]["text"])
                await show_options(ctx)
            else:
                await ctx.send("The story has ended.")
                is_story_running = False
        else:
            await ctx.send("Invalid option. Please choose a valid option.")
    else:
        await ctx.send("The story has not started yet. Type !story to begin.")

async def show_options(ctx):
    options_text = "\n".join([f"{emoji}: {option}" for emoji, option in story_options.items()])
    await ctx.send(options_text)

# Add other event handlers and commands as needed...

# Run the bot with the provided token
bot.run("YOUR_DISCORD_BOT_TOKEN")
