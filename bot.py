import os, dotenv
dotenv.load_dotenv()

import discord

print('TOKEN: ' + os.getenv("TOKEN"))

class Bot(discord.Client):
    async def on_ready(self):
        print('I\'m {}, and i\'m ready.\n----------'.format(self.user))

    async def on_message(self, m):
        if m.author == self.user: #niet op zichzelf reageren
           return
        res = ""
        s = str(m.content)
        for i in range(len(s)): 
            if not i % 2 : 
               res = res + s[i].upper() 
            else: 
               res = res + s[i].lower() 
        await m.channel.send(res[:-1] + '... ok brommer')

bot = Bot()
bot.run(os.getenv("TOKEN"))

# Bericht in text: str(m.content)