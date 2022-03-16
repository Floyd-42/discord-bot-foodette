import json
from datetime import date, timedelta


release_date = {"foodette": []}


for i in range(10):
    _date = (date.today() + timedelta(days=-2) + timedelta(days=14 * i)).strftime(
        "%d/%m/%Y"
    )
    release_date["foodette"].append({_date: "event.foodette_survey"})

with open("foodette_calendar.json", "w", encoding="utf-8") as outfile:
    json.dump(release_date, outfile)
