
import discord
import sys

# discord access info -----------------------------------------------------------------
client = discord.Client()
bot_id = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
server_id = 00000000000000000000
channel_name = "xxxxx"


# end--------------------------------------------------------------------------------------


@client.event # run the code when the bot goes online
async def on_ready():
    bot_testing = client.get_channel(server_id) # accessing the channel
    await bot_testing.send("ReZeroK Auto deletion bot is now online")

@client.event
async def on_message(message):
    bot_testing = client.get_channel(server_id)
    gate = True

    if message.content.find('$$') != -1:
        gate = False

    if message.content.lower() == '$$exit':
        await bot_testing.send("Auto Deletion Bot Terminated")
        sys.exit(0)

    if message.content == "Auto deletion bot is now online":
        print(message)
        

    elif str(message.channel).lower() == channel_name:
        pic_ext = ['.jpg','.png','.jpeg']
        for ext in pic_ext:
            if message.content.endswith(ext):
                print('image')
                gate = False

        try:
            if message.attachments[0] != '':
                print('image')
                gate = False
        except IndexError:
            print('text')

        if message.content != '' and gate:
            await message.channel.purge(limit=1)



while True:
    client.run(bot_id)