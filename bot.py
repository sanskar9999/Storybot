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
        "text": "You’ve hiked through Snake Canyon once be­fore while visiting your Uncle Howard at Red Creek Ranch, but you never noticed any cave entrance. It looks as though a recent rock slide has uncovered it.Though the late afternoon sun is striking the opening of the cave, the interior remains in total darkness. You step inside a few feet, trying to get an idea of how big it is. As your eyes become used to the dark, you see what looks like a tunnel ahead, dimly lit by some kind of phosphorescent material on its walls. The tunnel walls are smooth, as if they were shaped by running water. After twenty feet or so, the tunnel curves. You wonder where it leads. You venture in a bit further, but you feel nervous being alone in such a strange place. You turn and hurry out.",
        "options": {
            "\U0001F1E6": "If you decide to start back home",
            "\U0001F1E7": "If you decide to wait"
        },
        "images": []
    },
    {
        "text": "As you start walking back toward the ranch, you notice the trail seems very different than you re­member it, though of course moonlight can play tricks on your eyes. But you suddenly realize you are not walking on the trail at all, but on what seems to be a dried-up river bed. You hurry back to the cave entrance. You look around you and realize the whole landscape has changed. While you were in the cave, torrents of water have washed out the trail; yet there is not so much as a puddle left. You shiver. It is cold, much colder than it should be at this time of year. You take a jacket out of your backpack and put it on, but you are still freezing.At least the world about you seems brighter. It’s getting light in the east. The sun will soon be up. You look at your watch. It has run down, though you wound it only a few hours ago. Nothing seems to make sense anymore.",
        "options": {
            "\U0001F1E6": "If you continue toward the ranch", 
            "\U0001F1E7": "If you go back into the cave"
        },
        "images": []
    },
    {
        "text": "You wait until morning, but, as the rosy wisps of dawn begin to light the eastern sky, a chill and forbidding wind begins to blow.If you seek shelter, .If you brave the freezing wind to see more of the world about you,",
        "options": {
            "\U0001F1E6": "If you seek shelter",
            "\U0001F1E7": "If you brave the freezing wind to see more of the world about you"
        },
        "images": []
    },
    {
        "text": "You step into a niche in the rocks to escape the merciless blast of wind and lean back against the rock wall that crumbles under your weight, causing you to fall backward down a muddy slope and into a pond. The sun shines brightly down on you as you pick yourself up, dripping wet, and wade to the grassy shore. You look back at the rock, rising out of the pond, but you can’t see where you fell through.While you are collecting your senses, a horse comes prancing up, its rider dressed in tin armor—a knight out of the history books—enough to make you laugh. The horseman lifts off his helmet and laughs himself. “What a place for a bath!” he calls out. “Well, it was worth it—you’re cleaner than a pig!” He al­ most falls off his horse, he is laughing so hard. “But climb on and I’ll take you back to the castle,” he says. “We’ll see if we can’t make a human out of you yet.”If you accept the ride back to the castle.If you decline the invitation and try to find your way back into the Cave of Time",
        "options": {
            "\U0001F1E6": "If you accept the ride back to the castle",
            "\U0001F1E7": "If you decline the invitation and try to find your way back into the Cave of Time"  
        },
        "images": []
    },
    {
        "text": "The horseman helps you up on his horse and you sit uncomfortably as it canters over the countryside. After traveling a mile or so, you come to a great, stone castle. The horse trots across the drawbridge and into the stable. “Jump,” the knight calls to you, and you slide off the rear of the horse. The knight escorts you into the grand chamber of the castle. All about you are stewards, attendants, and knights. A few min­ utes later you find yourself bowing before the King himself.After hearing your story, the King looks gravely at his advisors and knights and stewards. “Does anyone believe this tale?” he asks.Everyone cries back, “No, Your Majesty,” or “Certainly not, Your Majesty.”“Then tell us the truth!” the King roars at you.If you insist you are telling the truth If you try to make up a plausible story   ",
        "options": {
            "\U0001F1E6": "If you insist you are telling the truth",
            "\U0001F1E7": "If you try to make up a plausible story"
        },
        "images": []
    },
    {
        "text": "\"I know it sounds strange, Your Majesty,\" you say, \"but I have no reason to incur your wrath by making up a false story.\" The King looks around at his courtiers. They all have grave expressions on their faces, as if you have committed some unpardonable sin ",
        "options": {
            "\U0001F1E6": "..."
        },
        "images": []
    },
    {
        "text": "“I’m sorry to have intruded upon your royal domain, Your Majesty.’’ you say humbly, trying to think up a good story as fast as you can. “It is true, sire, I have been badly mistreated by my wicked stepfather, with whom I live, and I place myself under your wise and just protection.’’“Who is this wicked stepfather and where does he live?” the King asks. “If he is wicked enough, we may want him to be one of our knights,” he adds, laughing, as do all the courtiers.“He lives beyond that hill,” you say, pointing toward a high wooded ridge, “and his name is Smith.”The King laughs once again. “Then your step­ father must be a fish,” he says, “for beyond yon­ der hill is Loch Ness.”  ",
        "options": {
            "\U0001F1E6": "...."
        },
        "images": []
    },
    {
        "text": "'Off to the tower,' the King shouts. Two knights leap forward, drag you out of the chamber, and, with spears at your back, force you to climb forty­ eight stone steps to the tower prison—a tiny cylin­ drical room with one small window looking out over the moat and pasture land beyond. The only furniture is a bed of straw.You realize you are back in the early days of feudal Europe, where the only laws are the King's whims. You have no idea how long he intends to keep you in the tower. There is one possibility of escape. The water in the moat, about twenty-five feet almost directly below your window, is quite deep. If you jump out far enough, you should land in the deep water and not be hurt. If you jump,  If not, ",
        "options": {
            "\U0001F1E6": "If you jump",
            "\U0001F1E7": "If not"   
        },
        "images": []
    },
    {
        "text": "You jump far out and fall faster and faster. You enter the water feet first and hit bottom, but the soft mud receives you gently. In a few seconds you reach the surface. You swim to the outer banks of the moat, shaken but unharmed. You scramble up the bank and run for the cover of the forest.You walk along the edge of the forest until well out of sight of the castle, then head across the open countryside. You stop a peasant to ask him where you might stay for the night. “Walk up that hill and you’ll see before you the waters of Loch Ness,” he says. “You’ll find a place there.”You follow his directions and, seeing some little houses near the lake, proceed toward them. Dark­ ness is setting in, and you are glad when you meet a fisherman who says he will give you shelter for the night. He and his wife are kindly people; they invite you to stay and earn your keep by helping them fish. If you accept  . If you decide to travel on  ",
        "options": {
            "\U0001F1E6": "If you accept",
            "\U0001F1E7": "If you decide to travel on"
        },
        "images": []
    },
    {
        "text": "You decide to wait, but soon regret it. A guard visits you twice a day and brings you only black bread and water. In a few days you feel almost too weak to escape even if you have the chance.But just as you are beginning to despair of ever regaining your freedom, the guard walks in, smil­ ing. “The King has ordered you out of here,’’ he says. “We have a much more important prisoner—a man who insulted the King’s horse.” He laughs in your face. You don’t know whether he is telling the truth or not, but he holds the door and waves you out. You walk down the long flight of stone steps to the main courtyard, free again— at least for the moment. The drawbridge is down and there seems to be nothing in the way of your leaving the castle.There is a splendid black horse tied up near you, probably owned by one of the knights. It occurs to you that you could cover a lot of ground on that horse before anyone realizes what happened.",
        "options": {
            "\U0001F1E6": "If you mount the horse and ride off",
            "\U0001F1E7": "If you ask the King for refuge"
        },
        "images": []
    },
    {
        "text": "In a moment you are across the bridge and galloping over the countryside, feeling a good deal smarter than the King and his knights. When you pass some shepherds and wave, they wave back. You stop to rest at the cottage of a friendly goatherd, who feeds you a good dinner. “Do not fear the King,” he says. “He is a fool who sits and drinks grog all day. His only concern is deciding who to put in the tower. His own knights laugh at him, and he is more likely to fall from his throne than you from your horse. Be off now and on to Merrie England, for great things await you there. God speed and good fortune!”Your energies are renewed by good food and drink, and your horse too is ready to ride. You thank your host warmly and ride off to new adven­ tures and a new life—almost a thousand years before you are born. The End",
        "options": {
            "\U0001F1E6": "The End"
        },
        "images": []
    },
    {
        "text": "You gain entrance to the King and thank him for letting you out of the tower. “Think nothing of it,” the King replies. “We would do as much for any villain. We like your spirit and, though your story makes as much sense as a dancing mule, it brought laughter to our eyes. You have, without meaning it we are sure, per­ formed a service for your King. We thank you. “We’ll see that you have a horse and some pieces of gold,” the King continues. “Go and make your fortune. We command you though— come once a year and tell us a story no less amus­ ing than what we have heard from your lips. ’’“My lord,” you say. “My liege,” he replies.You ride off, somewhat apprehensive, but in­ tent upon making as much of your life as is possible in the year 982. The End",
        "options": {
            "\U0001F1E6": "The End"
        },
        "images": []
    },
    {
        "text": "You resolutely trudge along a rocky ridge. It has been cleared of whirling snow by the fierce wind, which bites and blows against your body. The world seems transformed, and much for the worse. You must find a house or a cabin—people who can help you—or you will die. As you ponder your fate, you stumble and fall, plunging into a deep crevasse. You black out and later awaken, still shivering, but in a warmer place at least. By the dim amber light, you can see that somehow you have fallen back into one of the chambers in the Cave of Time. A passageway leads to the right, another to the left. Does one lead to the future and one to the past?",
        "options": {
            "\U0001F1E6": "If you enter the left-hand passageway",
            "\U0001F1E7": "If you enter the right-hand passageway"
        },
        "images": []
    },  
    {
        "text": "You follow the left passageway. It leads upward to the surface. Before you, a grassy meadow slopes down to a clear, fast-flowing stream; be­ yond it are pine-covered foothills stretching in the distance toward snow-covered peaks. You might be in Wyoming in your own time, but, whatever time it is, the world you see appears to be a hospi­ table one. You notice a herd of buffalo grazing. But nowhere can you see a house, or fence, or road, or any sign of human presence. It is possible you are living hundreds, perhaps thousands, of years ago. You gaze upward. One of the puffy, white cumulus clouds is moving in a strange fashion. It is descending! A spaceship is landing right before your eyes, only a few hundred yards away! If you hide from view . If S° UP 1° the spaceship .",
        "options": {
            "\U0001F1E6": "If you hide from view",
            "\U0001F1E7": "If S° UP 1° the spaceship"
        },
        "images": []
    },
    {
        "text": "You walk along the right-hand passageway for a long distance, suddenly you are sliding. Your head strikes something and you are knocked unconscious. When you wake up, you find yourself by a small lake, bordered by woods. A boy about twelve years old is fishing nearby, but there is no one else in sight. You go up and introduce yourself, hoping you can find out what year it is without sounding crazy. Fortunately, the boy is friendly and good na- tured. He tells you his name is Nick Tyler and that he lives on Birch Street. He works in his father's business making candles and soap—the best in the Colonies, he says. If you try to make up a believable story . If you tell him you come from the twentieth Century through the Cave of Time, Nick smiles. Then you tell him a little about life in your own time—about cars and planes, telephones and tele­ vision. He listens intently, with a big grin on his face, as if you are telling th funniest story ever told.",
        "options": {
            "\U0001F1E6": "If you try to make up a believable story",
            "\U0001F1E7": "If you tell him you come from the Twentieth Century through the Cave of Time, Nick smiles. Then you tell him a little about life in your own time—about cars and planes, telephones and tele­vision. He listens intently, with a big grin on his face, as if you are telling th funniest story ever told."
        },
        "images": []
    },
    {
        "text": "You cautiously approach the spaceship and, to your amazement, see that it is resting a foot or so above the ground, without any visible mechanism keeping it aloft. There are no engines, rocket exhausts, port holes, landing gear, antennae, or any equipment you might imagine a spaceship would need. You realize it must be the product of a supremely advanced civilization. Trusting that such people have learned to be loving toward others, you approach the ship. A portal slides open, but all you can see within is shimmering blue light. A large cube is thrust out through the portal and lowered to the ground by mechanical arms. The top of the cube is with­drawn, leaving a pallet on which lie the sleeping forms of three men and three women, dressed in shrouds of animal skin. Their bodies and features remind you of pictures you have seen depicting the earliest men on earth. You have an impulse to jump aboard the spaceship before the portal closes. If you do . If not ",
        "options": {
            "\U0001F1E6": "If you do",
            "\U0001F1E7": "If not"
        },
        "images": []
    },
    {
        "text": "You run up the hill and out of sight before any of the primitive people awaken. You must find an entrance to the Cave of Time. You search in the high rocky ground for some opening. Hours go by; dusk is fast approaching. Just as you are about to give up hope, you spy the entrance to a cave under a rock ledge. You eagerly step inside and have only a moment’s awareness that it is the den of a saber-toothed tiger. The End.",
        "options": {
            "\U0001F1E6": "The End"
        },
        "images": []
    },
    {
        "text": "The people look around curiously. They hardly seem to notice your presence. One by one they get up and walk around. One of them drinks from the stream. They make grunting and clicking noises, but do not seem to be actually talking among themselves. The largest of the group picks up a stick from the ground and begins prying up the roots of plants along the edge of the stream. He bites at each one. Finally he smiles and passes the root around to the others. One woman claps her hands. The others begin to find sticks. One of the men hands you a piece of root. You bite at it. It tastes like a dirty carrot. The women smile at you. You are accepted in the group. The next morning you wake up in the soft mossy bank in Snake Cavern, a few dozen yards from the entrance to the cave, wondering how much of what has been happening to you has been a dream and how much has been reality. But you have no desire to go into the Cave of Time again. The End",
        "options": {
            "\U0001F1E6": "The End"
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
        await ctx.send("The story is already running.")
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
bot.run("token")
