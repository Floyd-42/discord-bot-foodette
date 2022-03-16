"""Discord connector module."""
from datetime import date, timedelta
from typing import List
import os

from dotenv import load_dotenv
import discord

load_dotenv()

# import locale
# locale.setlocale(locale.LC_ALL, 'fr_FR')


EMOJIS = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]


class Connector:
    """Handler for discord client."""

    client = discord.Client()
    meals: List[str] = []

    @classmethod
    def run(cls) -> None:
        """Start the connection."""
        print("Running Connector")
        Connector.client.run(os.getenv("BOT_TOKEN"))

    @client.event
    async def on_ready():  # pylint: disable=no-method-argument
        """Executed when the setup is done."""
        print(f"Bot logged as {Connector.client.user}")
        await Connector.send()

    @classmethod
    def description(cls):
        """Create a description for the embed."""
        description = "Votez pour vos repas préférés :\n\n"
        for id, plate in enumerate(cls.meals):
            description += f"**Repas {id+1}** : {plate}\n"
        return description

    @classmethod
    async def send(cls):
        """Send message in a discord channel."""
        title = f"Foodette du {(date.today()+timedelta(days=8)).strftime('%A %d/%m/%Y').capitalize()}"
        embed = discord.Embed(
            title=title, description=cls.description(), color=0xFF5733
        )
        embed.set_thumbnail(
            url="https://touteslesbox.fr/wp-content/uploads/2016/07/logo-foodette.png"
        )

        # Testing
        channel = Connector.client.get_channel(923976716223914026)
        # CDC
        # channel = Connector.client.get_channel(945321786730483752)

        message = await channel.send(embed=embed)
        if len(cls.meals) > len(EMOJIS):
            print("Error: Unsupported meals count above 10.")
        for i in range(len(cls.meals)):
            await message.add_reaction(EMOJIS[i])
        await cls.close()

    @classmethod
    async def close(cls):
        """Close connection."""
        await cls.client.close()
