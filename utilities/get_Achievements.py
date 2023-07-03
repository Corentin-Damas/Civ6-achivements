import pandas as pd
import os
import requests
from bs4 import BeautifulSoup


def getAchievements():

    dt = pd.read_csv("../leaderTable.csv", index_col=False)
    dt['achievements'] = ''
    # test = pd.read_html(dt['link'][0])
    for index, row in dt.iterrows():
        r = requests.get(row['link'])
        soup = BeautifulSoup(r.content, 'html.parser')
        newAchievements = soup.select('.steam-achievement-name')
        row['achievements'] = [newAchie.getText() for newAchie in newAchievements]

    # Save the datas on the db
    file_path = os.path.dirname(__file__)
    file_name = "../leaderTable.csv"
    full_path = os.path.join(file_path, file_name)
    dt.to_csv(full_path, index=False)