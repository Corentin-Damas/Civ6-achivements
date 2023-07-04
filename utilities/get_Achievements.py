import pandas as pd
import os
import requests
from bs4 import BeautifulSoup
import json


def getAchievements():

    dt = pd.read_csv("utilities/leaderScrape.csv", index_col=False)
    dt['achievements'] = ''
    print(dt.head())
    # test = pd.read_html(dt['link'][0])

    # Get achievement
    for index, row in dt.iterrows():
        r = requests.get(row['link'])
        soup = BeautifulSoup(r.content, 'html.parser')
        newAchievements = soup.select('.steam-achievement-name')
        row['achievements'] = [newAchie.getText() for newAchie in newAchievements]

    # Restructure Data

    file_path = os.path.dirname(__file__)
    file_name = "../leaderTable.json"
    full_path = os.path.join(file_path, file_name)
    # Create the JSON DB
    with open(full_path, "w") as outfile:
        data = []
        for index, row in dt.iterrows():
            temp = {
                "leader": row["Leader"],
                "civilization": row['Civilization'],
                "achievements": row['achievements']
            }
            data.append(temp)
            # Save the datas
        json.dump(data, outfile)
