import discord
client = discord.Client()
@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(game=discord.Game(name="Making a bot"))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Hello":
        await client.send_message(message.channel, "World")
client.run('NTc4NjA4MzYyMTM3MzIxNDkz.XN2H1g.Yol5gmTxyaJf_zWQV5QxonDav14')