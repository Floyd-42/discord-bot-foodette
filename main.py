import requests

from bs4 import BeautifulSoup
import discord_connector

# week sould be something like "202203"
def get_meals(week):
    page = requests.get(
        "https://www.foodette.fr/inscription-panier-semaine?step=formule")

    soup = BeautifulSoup(page.content, 'html.parser')
    liste_repas = soup.find_all(
        'div',
        class_=
        "flex-1 flex flex-col relative p-2 sm:p-4 text-sm sm:text-base font-extralight space-y-2 sm:space-y-3"
        )

    repas_semaine = []

    for repas in liste_repas:
        nom_repas = repas.find(
            'div',
            class_=
            "flex-1 text-xs sm:text-sm md:text-base leading-4 sm:leading-5 font-medium cursor-pointer hyphens-auto"
            )
        if nom_repas:
            semaine = repas.find('input')["name"].split('][')[1]
            if semaine == week:
                repas_semaine.append(nom_repas.get_text().strip())

    return repas_semaine


def main():
    # print(get_meals("202201"))
    discord_connector.connector()
if __name__ == '__main__':
    main()