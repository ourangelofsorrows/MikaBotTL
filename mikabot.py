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
TOKEN = os.environ['TOKEN']
PRAW_SECRET = os.environ['CLIENT_SECRET']

def is_image_extension(p):
	ext = p.split(".")[-1]
	return ext.upper() in ['JFIF', 'JPEG', 'JPG','EXIF','TIFF','GIF',
	'BMP','PNG','PPM', 'PGM', 'PBM', 'PNM','WEBP','HDR','HEIF','BAT']

def set_embed_image(embed, attachment):
	if(is_image_extension(attachment["url"])):
		embed.set_image(url=attachment["url"])
		return True
	return False


async def merge_embeds(target_embed, message_embed_dict_list, message_attachments):
	def get_embedded_bold_sub(s):
		s_subbed = re.sub("""[*][*][*](.*?)[*][*][*]""", r"""\*\* *\1* \*\*""",s)
		s_resubbed = re.sub("""[*][*](.*?)[*][*]""", r"""\*\* \1 \*\*""", s_subbed)
		return s_resubbed
	
	def get_urls(m):
		return "\n".join([i["url"] for i in m])
	

	if(len(message_embed_dict_list) > 0 or len(message_attachments) > 0):
		embed_dict = dict()
		if(len(message_embed_dict_list) > 0 and len(message_attachments) > 0):
			embed_dict = message_embed_dict_list[0]
			embed_dict["description"] = """{des}\n---\n** {em_title} **\n{em_des}\n---\n{urls}""".format(
				des=target_embed.description,
				urls=get_urls(message_attachments),
				em_title=get_embedded_bold_sub(embed_dict["title"]),
				em_des=get_embedded_bold_sub(embed_dict["description"]))
		elif(len(message_embed_dict_list) > 0):
			embed_dict = message_embed_dict_list[0]
			embed_dict["description"] = """{des}\n---\n** {em_title} **\n{em_des}\n---""".format(
				des=target_embed.description,
				em_title=get_embedded_bold_sub(embed_dict["title"]),
				em_des=get_embedded_bold_sub(embed_dict["description"]))
		elif(len(message_attachments) > 0):
			embed_dict["description"] = """{des}\n{urls}""".format(des=target_embed.description, urls=get_urls(message_attachments))
	
		embed_dict["title"] = target_embed.title
		ret = discord.Embed(**embed_dict)
		for i in message_attachments:
			set_embed_image(ret, i)
		if("image" in embed_dict):
			set_embed_image(ret, embed_dict["image"])
		return ret
	else:
		return target_embed

   
@client.event
async def on_ready():
    print("MikaBot for The Lab is ready to fight!")
    await client.change_presence(game=Game(name="with Angel<3 | -help"))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.upper().startswith(command_prefix + "INFO"):
        embed = discord.Embed(title="MikaBot for The Lab", description="The cutest bot on discord! ^-^ - The Lab edition! so basically, this is a lite version.. yeesh", color=0x7f1ae5)
        embed.add_field(name="Owner", value="angel#9928", inline=False)
        await client.send_message(message.channel, embed=embed)
	
    if message.content.upper().startswith(command_prefix + "LAB PET"):
        reddit = praw.Reddit(client_id='3VJY49w5aP2XpQ',
                         client_secret=PRAW_SECRET,
                         user_agent='"MikaBot v1.0 (by /u/ourangelofsorrows)"')

        memes_submissions = reddit.subreddit('DiscordArtPets').new()
        post_to_pick = random.randint(1, 10)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        await client.send_message(message.channel, submission.url)
    
    if message.content.upper().startswith(command_prefix + "MIKA PIC"):
        reddit = praw.Reddit(client_id='3VJY49w5aP2XpQ',
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
        reddit = praw.Reddit(client_id='3VJY49w5aP2XpQ',
                         client_secret=PRAW_SECRET,
                         user_agent='"MikaBot v1.0 (by /u/ourangelofsorrows)"')

        memes_submissions = reddit.subreddit('catsstandingup').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        await client.send_message(message.channel, submission.url)
        
    if message.content.upper().startswith(command_prefix + "CUTE"):
        reddit = praw.Reddit(client_id='3VJY49w5aP2XpQ',
                         client_secret=PRAW_SECRET,
                         user_agent='"MikaBot v1.0 (by /u/ourangelofsorrows)"')

        memes_submissions = reddit.subreddit('aww').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        await client.send_message(message.channel, submission.url)
    

    if message.content.upper().startswith(command_prefix + "WHOLESOME MEME"):
        reddit = praw.Reddit(client_id='3VJY49w5aP2XpQ',
                         client_secret=PRAW_SECRET,
                         user_agent='"MikaBot v1.0 (by /u/ourangelofsorrows)"')

        memes_submissions = reddit.subreddit('wholesomememes').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)
        await client.send_message(message.channel, submission.url)

        
    if message.content.upper().startswith(command_prefix + "MEME"):
        reddit = praw.Reddit(client_id='3VJY49w5aP2XpQ',
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
    if message.content.upper().startswith(command_prefix + "BYE"):
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
    if message.content.upper().startswith(command_prefix + "MORNING"):
        msg = " {0.author.mention}".format(message)
        await client.send_message(message.channel, random.choice(["good morning",
                                                                     "meow",
                                                                     "too early",
                                                                     "I need another nap",])+ msg +"  "+"^-^" )
    if message.content.upper().startswith(command_prefix + "NIGHT"):
        msg = " {0.author.mention}".format(message)
        await client.send_message(message.channel, random.choice(["good night",
                                                                     "nighty",
                                                                     "sweet dreams",
                                                                     "nighty night",
                                                                     "don't let the shadows get you",
                                                                     "see you in the morning",])+ msg +"  "+"^-^" )      
    if message.content.upper().startswith(command_prefix + "FIGHT ME"):
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
            await client.send_message(message.channel, ":face_palm: " + auth + "shames" + rec + ":face_palm:")
        
            
        
    if message.content.upper().startswith(command_prefix + "CAN I KIN MIKA"):
        await client.send_message(message.channel, "beGONE furry :fencer:")
    if message.content.upper().startswith(command_prefix + "HUG"):
        for user in message.mentions:
            userID = message.author.id
            auth = "<@%s> " % (userID)
            rec = " {}".format(user.mention)
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
    
    
    if message.content.upper().startswith(command_prefix + "SECRET HUG"):
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

    if message.content.upper().startswith(command_prefix + "BEDTIME"):
        for user in message.mentions:
            userID = message.author.id
            auth = "<@%s> " % (userID)
            rec = " {}".format(user.mention)
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
            
    if message.content.upper().startswith(command_prefix + "LOVE"):
        for user in message.mentions:
            userID = message.author.id
            auth = "<@%s> " % (userID)
            rec = " {}".format(user.mention)
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
            
    if message.content.upper().startswith(command_prefix + "SECRET LOVE"):
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
    if message.content.upper().startswith(command_prefix + "FIGHT"):
        for user in message.mentions:
            userID = message.author.id
            auth = "<@%s>" % (userID)
            msg = "wants to fight {}".format(user.mention)
            await client.send_message(message.channel, ":fencer: " + auth + " " + msg + ":fencer:")

    if message.content.upper().startswith(command_prefix + "DANCE OFF"):
        for user in message.mentions:
            userID = message.author.id
            auth = "<@%s>" % (userID)
            msg = "challenges {}".format(user.mention)
            await client.send_message(message.channel, ":man_dancing: " + auth + " " + msg + "  " + "to a dance battle" + "  " + random.choice([":man_dancing:",
                                                                                                                             ":dancer:",
                                                                                                                             ":dancers:",]))
            
    if message.content.upper().startswith(command_prefix + "DUEL"):
        for user in message.mentions:
            userID = message.author.id
            auth = "<@%s>" % (userID)
            msg = "challenges {}".format(user.mention)
            await client.send_message(message.channel, ":fencer: " + auth + " " + msg + "  "+ "to a d-d-d-d-d-duel" + ":fencer:")
            
    if message.content.upper().startswith(command_prefix + "ASK MIKA"):
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





    

client.run(TOKEN)    
