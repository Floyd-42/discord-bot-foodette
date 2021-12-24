import os
import discord
from dotenv import load_dotenv
load_dotenv()

print("discord-connector.py")
client = discord.Client()

@client.event
async def on_ready():
    print(f"we have loggend in as {client.user}")
    # await message.channel.send('Hello!')
    await client.get_channel(id=923976716223914026).send("I'm alive!")
    await client.close()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # if message.content == "hello":

client.run(os.getenv('BOT_TOKEN'))

def connector():
    pass




# import os
# import discord
# from dotenv import load_dotenv
# load_dotenv()

# print("discord_connector.py")
# client = discord.Client()
# print(client)
# client.run(os.getenv('BOT_TOKEN'))

# @client.event
# async def on_ready():
#     print(f"we have logged in as {client.user}")
#     await client.close()


# def connector():
#     pass