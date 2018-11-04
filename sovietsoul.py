import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '.')
Clientdiscord = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Soviet Propaganda', type = 3))
    ##await client.send_message(discord.Object(id=421762417572446220),'Good morning comrades!! Another blissful day in the Soviet Union!!')
    print('Ready, Lets go') 
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Hey, member.name Welcome to Zanwer (best gaming discord) enjoy your stay!!!')
    print('Sent message to ' + member.name)

##https://cdn.discordapp.com/attachments/504000732387868692/504004531646890004/soviet6.png
##https://cdn.discordapp.com/attachments/504000732387868692/504004361106489367/saviet5.png
##https://cdn.discordapp.com/attachments/504000732387868692/504004196865933312/soviet4.png
##https://cdn.discordapp.com/attachments/504000732387868692/504003938807185409/germany6.png
##https://cdn.discordapp.com/attachments/504000732387868692/504003797316796428/germany5.png
##https://cdn.discordapp.com/attachments/504000732387868692/504003595625300006/Germany4.png
##https://cdn.discordapp.com/attachments/504000732387868692/504003147421974529/Start.png


@client.event
async def on_message(message):
    if message.content == '.russia':
        await client.send_message(message.channel,'I come from the mother land and it is beautiful!!')
    if message.content.startswith('.helpmerussia'):
        em = discord.Embed(title= 'COMMANDS:', description= '.russia, .howcommunist, .starofhumanity, .amigay, .rolldice, .flipcoin, .dicksize, .vaginsize, .titsize, .howgay')
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('.dicksize'):
        randomlist = [' 8====D',' 8========D','8=D','8==D','8===D','8=========D','8===========================D','8=============D',]
        em = discord.Embed(title= 'Dick Size: :rotating_light: ', description= '%s' %(random.choice(randomlist)))
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('.vaginsize'):
        randomlist = ['(  .  )','(.)','(    .    )','(   .   )','(          .          )','(                 .               )',]
        em = discord.Embed(title= 'Vagina Size: :rotating_light: ', description= '%s' %(random.choice(randomlist)))
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('.titsize'):
        randomlist = ['( + )( + )','(  +  )(  +  )','(   +   )(   +   )','(       +       )(         +         )','(+)(+)','(              +               )(               +               )',]
        em = discord.Embed(title= 'Tits Size: :rotating_light: ', description= '%s' %(random.choice(randomlist)))
        await client.send_message(message.channel,embed=em)
    if message.content.startswith('.flipcoin'):
        randomlist = [' heads',' tails',]
        em = discord.Embed(title= 'Game: Coin Flip: :moneybag:', description= 'Great! *FLIPS COIN* You got %s' %(random.choice(randomlist)))
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('.rolldice'):
        randomlist = [' 1',' 2','3','4','5','6',]
        em = discord.Embed(title= 'Game: Roll Dice: :game_die:', description= 'Great! *ROLLS DICE* You got %s' %(random.choice(randomlist)))
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('.amigay'):
        randomlist = [' GAY',' STRAIGHT',]
        em = discord.Embed(title= 'Test: Gay testing: :gay_pride_flag: ', description= 'Wait! *TESTING* You are %s' %(random.choice(randomlist)))
        await client.send_message(message.channel, embed=em)
    if message.content.startswith('.howcommunist'):
        randomlist = ["1%","13%","29%","33%","26%","38%","42%","49%","58%","52%","64%","61%","75%","72%","89%","86%","97%","92%","95%",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '.starofhumanity':
        em = discord.Embed(description='The Ever-Shining STAR of humanity!!')
        em.set_image(url='https://cdn.discordapp.com/attachments/496727517063938058/496746278630326273/stalin.jpg')
        await client.send_message(message.channel, embed=em)
    ##if message.content == '.declarewargermanreich':
        em = discord.Embed(title= 'What is the Soviet Union called with a different name??(send answer lowercase)',description= 'A Fatherland / B Motherland')
        em.set_image(url='https://cdn.discordapp.com/attachments/496727517063938058/496746278630326273/stalin.jpg')
        await client.send_message(message.channel, embed=em)
        if message.content == 'a':
                em = discord.Embed(title= 'What does Anschluss MEAN??(send answer lowercase)', description= 'A Germany joining Austria / B Germany Taking over Poland')
                em.set_image(url='https://cdn.discordapp.com/attachments/504000732387868692/504003595625300006/Germany4.png')
                await client.send_message(message.channel, embed=em)
                if message.content == 'a':
                    em = discord.Embed(title= 'Who did Lenin and Stalin want to pull from the government??(send answer lowercase)', description= 'A The Tsar / B The King')
                    em.set_image(url='https://cdn.discordapp.com/attachments/504000732387868692/504003147421974529/Start.png')
                    await client.send_message(message.channel, embed=em)
                    if message.content == 'a':
                        em = discord.Embed(title= 'Which army was under the rule of Stalin and Lenin??(send answer lowercase)', description= 'A The White Army / B The Red Army')
                        em.set_image(url='https://cdn.discordapp.com/attachments/504000732387868692/504004196865933312/soviet4.png')
                        await client.send_message(message.channel, embed=em)
                    if message.content == 'b':
                        em = discord.Embed(title= 'Did Stalin have a wife(send answer lowercase)', description= 'A Yes / B No')
                        em.set_image(url='https://cdn.discordapp.com/attachments/504000732387868692/504003595625300006/Germany4.png')
                        await client.send_message(message.channel, embed=em)
                if message.content == 'b':
                    em = discord.Embed(title= 'What ideology did Russia follow during WW2??(send answer lowercase)', description= 'A Fascism / B Communism')
                    em.set_image(url='https://cdn.discordapp.com/attachments/504000732387868692/504003797316796428/germany5.png')
                    await client.send_message(message.channel, embed=em)
                if message.content == 'a':
                    em = discord.Embed(title= 'You ugly CUNT you lost this is a tough hit for russia!!', description= 'You are noob shit comrade you will not be greeted in Russia again!!')
                    em.set_image(url='https://cdn.discordapp.com/attachments/504000732387868692/504003938807185409/germany6.png')
                    await client.send_message(message.channel, embed=em)
                if message.content == 'b':
                    em = discord.Embed(title= 'Did Stalin have a wife(send answer lowercase)', description= 'A Yes / B No')
                    em.set_image(url='https://cdn.discordapp.com/attachments/504000732387868692/504003595625300006/Germany4.png')
                    await client.send_message(message.channel, embed=em)
    if message.content == 'oofed':
        await client.send_message(message.channel,'Stop oofing start working!!')
    if message.content == 'oof':
        await client.send_message(message.channel,'Stop oofing start working!!')
    if message.content == 'gei':
        await client.send_message(message.channel,'Gays are not allowed into russia!!')
    if message.content == 'gey':
        await client.send_message(message.channel,'Gays are not allowed into russia!!')
    if message.content == 'gai':
        await client.send_message(message.channel,'Gays are not allowed into russia!!')
    if message.content == 'gay':
        await client.send_message(message.channel,'Gays are not allowed into russia!!')
    if message.content == 'гей':
        await client.send_message(message.channel,'Gays are not allowed into russia!!')
    if message.content == 'wow':
        await client.send_message(message.channel,'Stop wowing and grab the shovel!!')
    if message.content == 'russia':
        await client.add_reaction(message, '👍')
      








        


        

    







client.run('NTAzOTY3NzI0MDc5Mjg0MjI0.Dq-TCg.26l4CHOB7SZKEw5djV9weQWbabU')
