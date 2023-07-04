import matplotlib.pyplot as plt
import os
import logging
import pandas as pd
from pathlib import Path

def getGeneralLeaderInfo():
    # Get the Leader table from the website
    URL = "https://civilization.fandom.com/wiki/Leaders_(Civ6)"
    scraper = pd.read_html(URL)
    leaderTable = scraper[0]
    leaderTable_filter = leaderTable.drop(['Leader Ability', 'Leader Agenda'], axis=1)

    leaderTable_filter = leaderTable_filter.replace('\[\d*\]', '', regex=True)

    urlBase = "https://civilization.fandom.com/wiki/"
    leaderTable_filter['link'] = urlBase + leaderTable_filter['Leader'].str.replace(' ', '_') + "_(Civ6)"

    # Save the Table
    file_path = os.path.dirname(__file__)
    file_name = "leaderScrape.csv"
    full_path = os.path.join(file_path, file_name)

    leaderTable_filter.to_csv(full_path, index=False)
