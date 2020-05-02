print('Initializing discord...')
import discord

class Commands:
    def __init__(self):
        self.list = {
            'stop' : self.stop,
            'read' : self.read,
            'prefix': self.prefix
        }

    async def stop(self, m, agrs):
        print('Stopping bot...')
        await m.channel.send('Stopping!')
        await bot.logout()
    
    async def read(self, m, args):
        c = m.channel
        async with c.typing():
            status_message = await c.send('Berichten ophalen...')
            messages = await c.history(limit=1000).flatten()
            messages.reverse()

            for message in messages:
                if message.content.lower().strip() == '-start-':
                    messages = messages[messages.index(message)+1:]
            for message in messages:
                if message.content.lower().strip() == '-end-':
                    messages = messages[:messages.index(message)]

            await status_message.edit(content=statusmessage.content+' ✅')
        return messages

    async def prefix(self, m, args):
        global prefix
        prefix = args[0].lower()
        update_config('prefix', args[0].lower())
        await m.channel.send('New prefix is set to **{}**!'.format(args[0]))

def update_config(key, value):
    with open("config.json", "r+") as config_file:
        new_config = json.load(config_file)
        new_config[key] = value
        config_file.seek(0)
        json.dump(new_config, config_file)

class Bot(discord.Client):
    async def on_ready(self):
        print(self.user.name + ' is online!')
        print('Setting status...')
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Beter dan theier."))
        print('Bot ready!')
    
    async def on_message(self, m):
        if m.author == self.user: #niet op zichzelf reageren
           return
        if m.content.lower().strip().startswith(prefix):
            for command in commands.list:
                if m.content.lower().strip().startswith(prefix + command):
                    args = m.content[len(prefix + command):].split()
                    await commands.list[command](m, args)          

print('Reading token...')
import os, dotenv, json
dotenv.load_dotenv()

if os.path.isfile('config.json'):
    with open("config.json", "r") as config_file:
        config = json.load(config_file)
else:
    print('Config file doesn\'t exist, creating...')
    config = {
        'prefix': '.'
        }
    with open("config.json", 'w') as config_file:
        json.dump(config, config_file)

prefix = config['prefix']
commands = Commands()
bot = Bot()

print('Starting bot...')
bot.run(os.getenv("TOKEN"))