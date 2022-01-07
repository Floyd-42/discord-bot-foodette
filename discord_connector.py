import os
from typing import Counter
import discord
from discord import emoji
from discord.ext import tasks

from datetime import datetime, date, timedelta
from dotenv import load_dotenv
load_dotenv()

import random

class Connector:

    client = discord.Client()
    meals = []
    emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]

    def run() -> None:
        print("Running Connector")
        Connector.client.run(os.getenv('BOT_TOKEN'))


    @client.event
    async def on_ready():
        print(f"Bot logged as {Connector.client.user}")
        Connector.send.start(Connector)
        # await Connector.close()

    
    @classmethod
    def description(cls):
        description = "Votez pour vos repas préférés :\n\n"
        for id, plate in enumerate(cls.meals):
            rand = random.randint(1, len(cls.meals))
            description += f"**Repas {id+1}** : {plate}\n"
        return description
    
    @classmethod
    @tasks.loop(minutes=1)
    # @tasks.loop(hours=336)
    async def send(cls):
        title = f"Foodette du {(date.today()+timedelta(days=10)).strftime('%A %m/%d/%Y')}"
        embed=discord.Embed(title=title, description=Connector.description(), color=0xFF5733)
        embed.set_thumbnail(url="https://touteslesbox.fr/wp-content/uploads/2016/07/logo-foodette.png")

        # Testing
        channel = cls.client.get_channel(923976716223914026)
        # CDC
        # channel = cls.client.get_channel(920426362089652235)

        message  = await channel.send(embed=embed)
        if len(cls.meals) > len(cls.emojis):
            print("Error: Unsupported meals size above 10.")
        for i in range(len(cls.meals)):
            await message.add_reaction(cls.emojis[i])


    @classmethod
    async def close(cls):
        await cls.client.close()