import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
import re
import json
import praw
from discord import Game
from discord import emoji
import datetime
import traceback

Client = discord.Client()
client = commands.Bot(command_prefix = "-")
command_prefix = "-"

#Environment Variables
TOKEN = os.environ['MIKABOT_DISCORD_TOKEN']
PRAW_SECRET = os.environ['MIKABOT_PRAW_CLIENT_SECRET']
PRAW_ID = os.environ['MIKABOT_PRAW_CLIENT_ID']

@client.event
async def on_ready():
    print("MikaBot for The Lab is ready to fight!")
    await client.change_presence(game=Game(name="with Angel<3 | -help"))


@client.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == '\U0001F57A':
        if reaction.count == 3:
            msg = ("\U0001F57A " + reaction.message.author.display_name + " has been invited to dance in " + reaction.message.channel.name + " \U0001F57A")
            msg2 = '*"' + reaction.message.content + '"*'
            embed = discord.Embed(title= msg, description= msg2, color=0x7f1ae5)
            await client.send_message(discord.Object(id='593076753157586954'), embed=embed)
    
@client.event
async def on_message_delete(message):
        fmt = '{0.author} has deleted the message:\n ***{0.content}***'
        await client.send_message(discord.Object(id='593077154116403230'), fmt.format(message))
    
@client.event
async def on_message_edit(before, after):
        reply = ('**{0.author}** has' + ' edited their message:\n'
                    '*{0.content}*\n'
                    '→ ***{1.content}***')
        await client.send_message(discord.Object(id='593077154116403230'), reply.format(after, before))
        

       
@client.event
async def on_member_join(member):
    server = member.server.default_channel
    channel = member.server.get_channel("593077154116403230")
    fmt = "***:man_dancing: Welcome to Lola's Book of Shadows, {0.mention}!! Please read the #rules and come say hi! :man_dancing:***"
    await client.send_message(channel, fmt.format(member, member.server))

@client.event
async def on_member_ban(member):
    msg = "{} Has been banned. DM Angel for more info ^-^.".format(member.name)
    print(msg)
    await client.send_message(client.get_channel('593077154116403230'), msg)

@client.event
async def on_member_remove(member):
    since_joined = (datetime.datetime.now() - member.joined_at).days
    msg = "Our friend {} has left Lola's Book of Shadows :fencer:. they had only been with us {} days.".format(member.name, since_joined)
    print(msg)
    await client.send_message(client.get_channel('593077154116403230'), msg)
    

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.upper().startswith(command_prefix + "INFO"):
        embed = discord.Embed(title="MikaBot for The Lab", description="The cutest bot on discord! ^-^ - The Lab edition! so basically, this is a lite version.. yeesh", color=0x7f1ae5)
        embed.add_field(name="Owner", value="angel#9928", inline=False)
        await client.send_message(message.channel, embed=embed)
	
    if message.content.upper().startswith(command_prefix + "LAB PET"):
        reddit = praw.Reddit(client_id=PRAW_ID,
                         client_secret=PRAW_SECRET,
                         user_agent='"MikaBot v1.0 (by /u/ourangelofsorrows)"')

        memes_submissions = reddit.subreddit('DiscordArtPets').new()
        post_to_pick = random.randint(1, 10)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        await client.send_message(message.channel, submission.url)
    
    if message.content.upper().startswith(command_prefix + "MIKA PIC"):
        reddit = praw.Reddit(client_id=PRAW_ID,
                         client_secret=PRAW_SECRET,
                         user_agent='"MikaBot v1.0 (by /u/ourangelofsorrows)"')

        memes_submissions = reddit.subreddit('mikabot').new()
        post_to_pick = random.randint(1, 50)
        for i in range(0, post_to_pick):            
            submission = next(x for x in memes_submissions if not x.stickied)
     
        if message.author.id == "244838220259393538":
            await client.send_message(message.channel, "no you don't deserve Mika pics")
        else:
                await client.send_message(message.channel, submission.url)
        
    if message.content.upper().startswith(command_prefix + "CAT STANDING UP"):
        reddit = praw.Reddit(client_id=PRAW_ID,
                         client_secret=PRAW_SECRET,
                         user_agent='"MikaBot v1.0 (by /u/ourangelofsorrows)"')

        memes_submissions = reddit.subreddit('catsstandingup').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        await client.send_message(message.channel, submission.url)
        
    if message.content.upper().startswith(command_prefix + "CUTE"):
        reddit = praw.Reddit(client_id=PRAW_ID,
                         client_secret=PRAW_SECRET,
                         user_agent='"MikaBot v1.0 (by /u/ourangelofsorrows)"')

        memes_submissions = reddit.subreddit('aww').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        await client.send_message(message.channel, submission.url)
    

    if message.content.upper().startswith(command_prefix + "WHOLESOME MEME"):
        reddit = praw.Reddit(client_id=PRAW_ID,
                         client_secret=PRAW_SECRET,
                         user_agent='"MikaBot v1.0 (by /u/ourangelofsorrows)"')

        memes_submissions = reddit.subreddit('wholesomememes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        await client.send_message(message.channel, submission.url)

        
    if message.content.upper().startswith(command_prefix + "MEME"):
        reddit = praw.Reddit(client_id=PRAW_ID,
                         client_secret=PRAW_SECRET,
                         user_agent='"MikaBot v1.0 (by /u/ourangelofsorrows)"')

        memes_submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        await client.send_message(message.channel, submission.url)


    if message.content.upper().startswith(command_prefix + "HELP"):
        msg = "```Hi I'm MikaBot! ^-^. These are my commands:```  \n **-info** \n *Gives you basic info about the bot* \n \n \n `Greetings:` \n **-hello** \n *Say hi to me! ^-^*  \n **-bye** \n *Say goodbye to me!* \n **-morning** \n *Wish me good morning!* \n **-night** \n *Wish me good night!* \n \n \n `Love:` \n **-hug (@user)** \n *Hug someone!* \n **-secret hug (@user)** \n *Secretly hug someone!*\n **-love (@user)** \n *Declare your love!* \n **-secret love(@user)** \n *Declare your love secretly!*  \n **-bedtime(@user)** \n *tell someone to take a catnap!* \n \n \n `Fight:` \n **-fight me** \n  *Challenge me to a fight!* \n **-duel (@user)** \n *Challenge someone else to a fight!* \n **-dance off(@user)** \n *Challenge someone to a dance battle!* \n **-shame (@user)** \n *Shame someone!* \n \n \n"
        await client.send_message(message.author, msg)
        msg2 = "`fun:` \n **-say (message)** \n *Get me to say something!* \n **-says (message)** \n *Get me to say something, but don't delete your say command message!* \n **-ask mika (message)** \n *Ask me a question! I am a psychic you know.* \n **-what should i draw** \n *Gives you a thing to draw!* \n \n \n `misc:` \n **-coin** \n *Flips a coin!* \n **-ping** \n *Pong!* \n **-pointless** \n *Press the pointless button!* \n **-brain** \n *get brained* \n \n \n `Reddit` \n **-wholesome meme** \n *I will show you a meme* \n **-meme** \n *I will show you a WHOLESOME meme* \n **-cute** \n *I will show you something adorable* \n **-cat standing up** \n *I will show you a cat standing up* \n **-mika pic** \n *I will show you a selfie ^-^* \n **-lab pet** \n *I will show you a pic of a pet of the server's members ^-^*"
        await client.send_message(message.author, msg2)                                    
         
    if message.content.upper().startswith("I KIN MIKA"): 
         await client.send_message(message.author, "don't kin me. you furry.")
         
    if message.content.upper().startswith("ANGEL SUCKS"): 
         await client.send_message(message.author, "angel doesn't suck. you do.")
         
    if message.content.upper().startswith("I AM GAY"): 
         await client.send_message(message.author, "Angel is the gayest")
    
    if message.content.upper().startswith(command_prefix + "BRAIN"):
        if message.author.id == "150440931080798210":
            await client.send_message(message.channel, random.choice(["no brains for u hana.",
                                                                     "okay fine, you can have .0005 brain",
                                                                     "you zombie furry",
                                                                     "fine hana, you get brained",
                                                                     "nope, I'll brian you instead! Ha-Ha",
                                                                     "no.",]))
        else:
            await client.send_message(message.channel, "{0.author.mention}".format(message) + " has been brained" )
        

    
    
         
    if message.content.upper().startswith(command_prefix + "HELLO"):
        msg = " {0.author.mention}".format(message)
        imgList = os.listdir("./gifs/hello/") 
        imgString = random.choice(imgList) 
        path = "./gifs/hello/" + imgString 
        await client.send_message(message.channel, random.choice(["hi, hi, hi",
                                                                     "sup",
                                                                     "Meowello ",
                                                                     "Heyo",
                                                                     "hi",
                                                                     "yo.",
                                                                     "wasssup",
                                                                     "why, hello",
                                                                     "meow??",
                                                                     "did you bring tuna",
                                                                     "hey",
                                                                     "I'd say hi, but I'm busy doing.. uh catstuff? botstuff? what am I?",
                                                                     "Did ya miss me",
                                                                     "meow!",
                                                                     "hello",])+ msg +"  "+"^-^" )
        await client.send_file(message.channel, path)
    if message.content.upper().startswith(command_prefix + "BYE"):
        imgList = os.listdir("./gifs/bye/") 
        imgString = random.choice(imgList) 
        path = "./gifs/bye/" + imgString 
        msg = " {0.author.mention}".format(message)
        await client.send_message(message.channel, random.choice(["bye",
                                                                     "goodbye",
                                                                     "I'll miss you",
                                                                     "meow",
                                                                     "meow??",
                                                                     "see ya!",
                                                                     "come back soon!",
                                                                     "take care",
                                                                     "buh-bye friend",
                                                                     "remember to close the god damn door",])+ msg +"  "+"^-^" )
        await client.send_file(message.channel, path)
    if message.content.upper().startswith(command_prefix + "MORNING"):
        msg = " {0.author.mention}".format(message)
        imgList = os.listdir("./gifs/hello/") 
        imgString = random.choice(imgList) 
        path = "./gifs/hello/" + imgString 
        await client.send_message(message.channel, random.choice(["good morning",
                                                                     "meow",
                                                                     "too early",
                                                                     "I need another nap",])+ msg +"  "+"^-^" )
        await client.send_file(message.channel, path)
    if message.content.upper().startswith(command_prefix + "NIGHT"):
        msg = " {0.author.mention}".format(message)
        imgList = os.listdir("./gifs/sleep/") 
        imgString = random.choice(imgList) 
        path = "./gifs/sleep/" + imgString
        await client.send_message(message.channel, random.choice(["good night",
                                                                     "nighty",
                                                                     "sweet dreams",
                                                                     "nighty night",
                                                                     "don't let the shadows get you",
                                                                     "see you in the morning",])+ msg +"  "+"^-^" )
        await client.send_file(message.channel, path)     
    if message.content.upper().startswith(command_prefix + "FIGHT ME"):
                imgList = os.listdir("./gifs/fight/") 
                imgString = random.choice(imgList) 
                path = "./gifs/fight/" + imgString
                await client.send_message(message.channel, random.choice([":fencer:",
                                                                          "come at me bro :fencer:",
                                                                          "can you beat me in a dance competition? :man_dancing:",
                                                                          "you're not a worthy opponent.",
                                                                          "IT'S TIME TO D-D-D-D-D-D-DUEL!:fencer:",
                                                                          "Sasuke? is that you?",
                                                                          "bring it! :fencer:",
                                                                          "While you were busy playing with bots, I studied the blade :fencer:",
                                                                          "silly mortal :fencer:",
                                                                          ":fencer: :fencer: :fencer:",
                                                                          ":fencer: :fencer: :fencer:",
                                                                          ":fencer: :fencer: :fencer:",
                                                                          "I have seen all of naruto. you can't defeat me :fencer:",
                                                                          ":fencer: :fencer: :fencer:",]))
                await client.send_file(message.channel, path)
    if message.content.upper().startswith(command_prefix + "PING"):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith(command_prefix + "SAYS "):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" %(" ".join(args[1:])))
    if message.content.upper().startswith(command_prefix + "SAY "):
        try:
            await client.delete_message(message)
        except discord.Forbidden as f:
            await client.send_message(message.channel, "Angel didn't give me permission to delete in this channel. :(")
            return 
        except Exception as e:
            print(e)
            traceback.print_tb(e.__traceback__)
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" %(" ".join(args[1:])))

    if message.content.upper().startswith(command_prefix + "POINTLESS"):
        if message.author.id == "343160195075276801":
            await client.send_message(message.channel, "pointless button has been pressed")
        else:
            await client.send_message(message.channel, "thou shall not press the button!")

    if message.content.upper().startswith(command_prefix + "SHAME"):
        for user in message.mentions:
            userID = message.author.id
            auth = "<@%s> " % (userID)
            rec = " {}".format(user.mention)
            imgList = os.listdir("./gifs/shame/") 
            imgString = random.choice(imgList) 
            path = "./gifs/shame/" + imgString
            await client.send_message(message.channel, ":face_palm: " + auth + "shames" + rec + ":face_palm:")
            await client.send_file(message.channel, path)
        
            
        
    if message.content.upper().startswith(command_prefix + "CAN I KIN MIKA"):
        await client.send_message(message.channel, "beGONE furry :fencer:")
    if message.content.upper().startswith(command_prefix + "HUG"):
        for user in message.mentions:
            userID = message.author.id
            auth = "<@%s> " % (userID)
            rec = " {}".format(user.mention)
            imgList = os.listdir("./gifs/hug/") 
            imgString = random.choice(imgList) 
            path = "./gifs/hug/" + imgString
            await client.send_message(message.channel, " :turtle:" + auth + random.choice(["hugs",
                                                                     "embraces",
                                                                     "super hugs",
                                                                     "cuddles",
                                                                     "wants to hold",
                                                                     "wants a hug from",
                                                                     "wishes to be held by",
                                                                     "hugs and hugs and hugs and HUGS",
                                                                     "wishes to hug ",
                                                                     "fucking hugs",]) + rec + " :turtle:")
            await client.send_file(message.channel, path)
    
    
    if message.content.upper().startswith(command_prefix + "SECRET HUG"):
        imgList = os.listdir("./gifs/hug/") 
        imgString = random.choice(imgList) 
        path = "./gifs/hug/" + imgString
        try:
            await client.delete_message(message)
        except discord.Forbidden as f:
            await client.send_message(message.channel, "Angel didn't give me permission to delete in this channel. :(")
            return 
        except Exception as e:
            print(e)
            traceback.print_tb(e.__traceback__)
        for user in message.mentions:
            msg = "Someone has hugged {}".format(user.mention)
            await client.send_message(message.channel, ":ghost: " + msg + ". " + random.choice(["was it you Ashe?",
                                                                     "I wonder who it was.",
                                                                     "hmm",
                                                                     "interesting...",
                                                                     "...",
                                                                     "   ",
                                                                     "   ",
                                                                     "   ",               
                                                                     "Zoinks!",]) + ":ghost:")
            await client.send_file(message.channel, path)
    if message.content.upper().startswith(command_prefix + "BEDTIME"):
        for user in message.mentions:
            userID = message.author.id
            auth = "<@%s> " % (userID)
            rec = " {}".format(user.mention)
            imgList = os.listdir("./gifs/sleep/") 
            imgString = random.choice(imgList) 
            path = "./gifs/sleep/" + imgString
            await client.send_message(message.channel, ":zzz: " + auth + "wants" + rec + random.choice([" to go to bed",
                                                                     " to sleep",
                                                                     " to rest",
                                                                     " to go the fuck to sleep",
                                                                     " to shup up, close their eyes, and sleep",
                                                                     " to sleep because they really care about their friend.",
                                                                     " to sleep in hopes that it will make them smarter",
                                                                     " to sleep because they aren't making any sense anymore",
                                                                     " to sleep",
                                                                     " to bring mika tuna--uh-- yeah, I wrote this one. uh. please give me tuna?",
                                                                     " to sleep, but don't look under the bed",
                                                                     " to count sheep and fall asleep",]) + " :zzz:")
            await client.send_file(message.channel, path)
            
    if message.content.upper().startswith(command_prefix + "LOVE"):
        for user in message.mentions:
            userID = message.author.id
            auth = "<@%s> " % (userID)
            rec = " {}".format(user.mention)
            imgList = os.listdir("./gifs/love/") 
            imgString = random.choice(imgList) 
            path = "./gifs/love/" + imgString
            await client.send_message(message.channel, ":heart:" + auth + random.choice(["loves",
                                                                     "adores",
                                                                     "will never fight",
                                                                     "wants to be with",
                                                                     "appreciates",
                                                                     "stands by",
                                                                     "is obsessed with",
                                                                     "is really into",
                                                                     "wishes to stargaze with",
                                                                     "wants to hold",
                                                                     "wants to be loved by",
                                                                     "would never anime betray",]) + rec + ":heart:")
            await client.send_file(message.channel, path)
            
    if message.content.upper().startswith(command_prefix + "SECRET LOVE"):
        imgList = os.listdir("./gifs/love/") 
        imgString = random.choice(imgList) 
        path = "./gifs/love/" + imgString
        try:
            await client.delete_message(message)
        except discord.Forbidden as f:
            await client.send_message(message.channel, "Angel didn't give me permission to delete in this channel. :(")
            return 
        except Exception as e:
            print(e)
            traceback.print_tb(e.__traceback__)
        for user in message.mentions:
            msg = "Someone secretly loves {}".format(user.mention)
            await client.send_message(message.channel, ":thinking: " + msg + ". " + random.choice(["was it you John?",
                                                                     "ooh la la!",
                                                                     "hmm..hmm..",
                                                                     "OOF",
                                                                     "...",
                                                                     "   ",
                                                                     "   ",
                                                                     "   ",
                                                                     "wompety womp!",]) + ":thinking:")
            await client.send_file(message.channel, path)
    if message.content.upper().startswith(command_prefix + "FIGHT"):
        for user in message.mentions:
            userID = message.author.id
            auth = "<@%s>" % (userID)
            msg = "wants to fight {}".format(user.mention)
            imgList = os.listdir("./gifs/fight/") 
            imgString = random.choice(imgList) 
            path = "./gifs/fight/" + imgString
                                   
            await client.send_message(message.channel, ":fencer: " + auth + " " + msg + ":fencer:")
            await client.send_file(message.channel, path)
    if message.content.upper().startswith(command_prefix + "DANCE OFF"):
        for user in message.mentions:
            userID = message.author.id
            auth = "<@%s>" % (userID)
            msg = "challenges {}".format(user.mention)
            imgList = os.listdir("./gifs/dance/") 
            imgString = random.choice(imgList) 
            path = "./gifs/dance/" + imgString
            await client.send_message(message.channel, ":man_dancing: " + auth + " " + msg + "  " + "to a dance battle" + "  " + random.choice([":man_dancing:",
                                                                                                                             ":dancer:",
                                                                                                                             ":dancers:",]))
            await client.send_file(message.channel, path)
            
    if message.content.upper().startswith(command_prefix + "DUEL"):
        for user in message.mentions:
            userID = message.author.id
            auth = "<@%s>" % (userID)
            msg = "challenges {}".format(user.mention)
            imgList = os.listdir("./gifs/duel/")
            imgString = random.choice(imgList)
            path = "./gifs/duel/" + imgString
            await client.send_message(message.channel, ":fencer: " + auth + " " + msg + "  "+ "to a d-d-d-d-d-duel" + ":fencer:")
            await client.send_file(message.channel, path)
            
    if message.content.upper().startswith(command_prefix + "ASK MIKA"):
            imgList = os.listdir("./gifs/ask/") 
            imgString = random.choice(imgList) 
            path = "./gifs/ask/" + imgString
            await client.send_message(message.channel, ":8ball: " + random.choice(["Maybe? idk. Now that I think about it, this thing may be broken. NEXT!:8ball:",
                                                                     "Certainly. :8ball:",
                                                                     "Yes. I'd even bet one of my 9 lives on it. :8ball:",
                                                                     "Not a chance. nope. :8ball:",
                                                                     "The chance of a reality star becoming a president is higher- oh wait :8ball:",
                                                                     "I think it's possible... :8ball:",
                                                                     "no. :8ball:",
                                                                     "Ask again later. I'm tired. Gotta take a cat nap... :8ball:",
                                                                     "womp :8ball:",
                                                                     "Honestly, at this point. I don't even care :8ball:",
                                                                     "Nah :8ball:",
                                                                     "Depends on how many cans of tuna you are willing to spend on the right answer :8ball:",
                                                                     "Yep :8ball:",
                                                                     "Do you want my honest answer, or my nice answer? :8ball:",
                                                                     "Ask yourself! :8ball:",]))
            await client.send_file(message.channel, path)
            
    if message.content.upper().startswith(command_prefix + "COIN"):
         await client.send_message(message.channel, random.choice(("Heads "*22).split() + ("Tails "*22).split() + ["it landed on the side! :O!"]))
         
    if message.content.upper().startswith(command_prefix + "WHAT SHOULD I DRAW"):
        person = ["a man", "a woman", "a teenager", "a child", "a baby", "a firefighter", "a princess",
                  "a mermaid", "a dragon", "a cheerleader", "a furry", "an emo", "a vampire", "a lion",
                  "a hunter", "a knight", "an alien", "a cowboy", "an anime character", "a cat",
                  "a dog", "a teacher", "a salesperson", "a rockstar", "a rebel", "a ninja", "a samurai",
                  "a body builder", "a doctor", "a monkey"]

        clothing = ["a hat", "a snazzy jacket", "a leather skirt", "a cowboy hat", "a cool cape", "a pair of clown shoes",
                    "chain mail armor", "a little backpack", "a pair of skinny jeans", "a summer dress", "a fursuit",
                    "heavy eyeliner", "an anime-like hairstyle", "a vest", "nothing", "a giant poofy jacket"]
        
        activity = ["dancing", "fighting robots", "giving a speech", "watching anime", "eating fruits", "a pair of clown shoes",
                    "hunting evil zombies", "chilling with friends", "studying","baking a cake", "hanging out with puppies",
                    "playing the guitar", "stargazing", "drawing", "playing a game", "having a picnic"]
        
        place = ["the cinema", "the park", "at a concert", "the opening of a mountain cave", "the graveyard", "home",
                 "the zoo", "a furry convention", "a furry convention", "a party", "school", "a friends' house", "the beach",
                 "the mall", "the department store", "a playground"]

        await client.send_message(message.channel, """:paintbrush: {person} wearing {clothing} while {activity} at {place} :paintbrush:""".format(person=random.choice(person), clothing=random.choice(clothing), activity=random.choice(activity), place=random.choice(place)))
    
    if message.content.upper().startswith(command_prefix + "UPTOP"):
        imgList = os.listdir("./gifs/uptop/") 
        imgString = random.choice(imgList) 
        path = "./gifs/uptop/" + imgString
        await client.send_file(message.channel, path)




    

client.run(TOKEN)    
