import os, dotenv
dotenv.load_dotenv()

import discord

print(os.getenv("TOKEN"))

class Bot(discord.Client):
    async def on_ready(self):
        print('I\'m {}, and i\'m ready.\n----------'.format(self.user))

    async def on_message(self, m):
        if m.author == self.user: #niet op zichzelf reageren
           return

bot = Bot()
bot.run(os.getenv("TOKEN"))



# Reageer op bericht (binnen on_message):
    # await m.channel.send('AAAAaaaaa')
# Bericht in text: str(m.content)

# 
# simpele login/ready log:
