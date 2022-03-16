"""Main function to the discord bot foodette."""
from datetime import date, timedelta
from typing import List

import requests
from bs4 import BeautifulSoup
from discord_connector import Connector

# week argument have to be something like "202203" for March 2022.
def get_meals(week: str):
    """Retrieve Meals from foodette website."""
    page = requests.get(
        "https://www.foodette.fr/inscription-panier-semaine?step=formule"
    )

    soup = BeautifulSoup(page.content, "html.parser")
    liste_repas = soup.find_all(
        "div",
        class_=(
            "flex-1 flex flex-col relative p-2 sm:p-4 text-sm "
            "sm:text-base font-extralight space-y-2 sm:space-y-3"
        ),
    )

    repas_semaine: List[str] = []

    for repas in liste_repas:
        nom_repas = repas.find(
            "div",
            class_=(
                "flex-1 text-xs sm:text-sm md:text-base leading-4 "
                "sm:leading-5 font-medium cursor-pointer hyphens-auto"
            ),
        )
        if nom_repas:
            semaine = repas.find("input")["name"].split("][")[1]
            if semaine == week:
                repas_semaine.append(nom_repas.get_text().strip())

    return repas_semaine


def main():
    """Main function."""
    date_next_week = "".join(
        [f"{x:02}" for x in (date.today() + timedelta(days=7)).isocalendar()[0:2]]
    )

    Connector.meals = get_meals(date_next_week)
    Connector.run()


if __name__ == "__main__":
    main()
