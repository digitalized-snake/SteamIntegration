import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Nerd'):
        await message.channel.send('Awwww')

client.run('ODg1Mjg4MzAxNzgxNzIxMDg4.YTk2-w.FERRmT2MZknKBVsRZk1_swuufH0')
