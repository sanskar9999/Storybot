# Storybot
A discord based story bot for a choose-your-adventure type interactive story game

## Goals
- ~~running and showing online
- ~~can log messages and read them
- ~~the ability to write messages as response
- ~~the ability to respond to !help command with a list of available commands
- ~~the ability to respond to the !story command to start the story
- ~~the ability to send images along with text messages
- ~~the ability to choose different options after a scenario has been laid down
- ~~the ability to add emojis for different options
- ~~the ability to make this choice by reacting with emojis on the message

errors

- On line 67, you have an `elif` statement without a corresponding `if` statement. You need to add an `if` statement before the `elif` statement to check the option chosen by the user.
- On line 69, you have an indentation error. You need to indent the code block under the `elif` statement to match the indentation level of the previous code block.
- On line 71, you have a comment that says \"do something based on the option chosen\", but you have not written any code to do that. You need to write some code to handle the different outcomes of the story based on the user's choice.
- On line 73, you have an `else` statement without a corresponding `if` or `elif` statement. You need to remove the `else` statement or add an `if` or `elif` statement before it.
- On line 74, you have an indentation error. You need to indent the code block under the `else` statement to match the indentation level of the previous code block.

These are some of the errors I found in your code. There may be more errors that I did not catch, so I suggest you test your code thoroughly and use a code editor that can highlight syntax errors for you.

If you need more help with coding a discord bot in Python, you can check out some of these web search results that I found for you:

- [How to Make a Discord Bot in Python – Real Python](^2^): This is a comprehensive tutorial that covers how to create a discord bot account, how to invite your bot to join a server, how to code a basic discord bot with the discord.py library, how to create discord connections, how to handle events, how to accept commands and validate assumptions, and how to interact with various discord APIs.
- [Python Discord Bot Tutorial – Code a Discord Bot And Host it for Free](^3^): This is another tutorial that shows you how to build your own discord bot completely in the cloud using Repl.it, an online IDE that you can use in your web browser. It also explains how to install discord.py, how to create a discord application and bot, how to create a discord guild (server), how to add the bot into the server, and how to code the bot.
- [Ztuu/Discord-Python-Bot-Tutorial - GitHub](^4^): This is a GitHub repository that contains a simple discord bot as a teaching exercise for learning Python and discord.py. It also has a README file that explains how to set up and run the bot.

I hope these resources are helpful for you. Good luck with your project! 😊

Source: Conversation with Bing, 19/7/2023
(1) How to Make a Discord Bot in Python – Real Python. https://realpython.com/how-to-make-a-discord-bot-python/.
(2) Python Discord Bot Tutorial – Code a Discord Bot And Host it for Free. https://www.freecodecamp.org/news/create-a-discord-bot-with-python/.
(3) Ztuu/Discord-Python-Bot-Tutorial - GitHub. https://github.com/Ztuu/Discord-Python-Bot-Tutorial.
(4) Build a Discord Bot With Python | Built In. https://builtin.com/software-engineering-perspectives/discord-bot-python.
(5) How to make a Discord bot in Python - CodeSpeedy. https://www.codespeedy.com/how-to-make-a-discord-bot-in-python/.
...