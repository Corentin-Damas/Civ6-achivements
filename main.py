import requests
import json
import os
from utilities.steam_api import get_game_data
import pandas as pd

file_path = os.path.dirname(__file__)
file_name = "game_data.json"
full_path = os.path.join(file_path, file_name)

# check if the data already exist, if it doesn't exist will go fetch them
if not os.path.isfile(full_path):
    print("apikey used")
    get_game_data()  ## Function in utilities

with open("game_data.json") as openfile:
    data = json.load(openfile)

data_achivement = data["Sid Meier's Civilization VI"]  ## break key value pair

df_full = pd.json_normalize(data_achivement)
df_refactored = df_full.drop(columns=["apiname", "unlocktime"])

print(df_refactored.head(), df_refactored.columns, df_refactored.info())

print(df_refactored["achieved"].value_counts())

### Untile here / get data and achived success;

### TO DO
## go to 'https://civilization.fandom.com/wiki/Leaders_(Civ6)'
## [df New Columns 'leader'] - And for scrap for each leader take the "related achievement"
## For each link the leader to the success in the df (some success can be done by different leaders)
## [df New Columns 'conditions'] for an achivement some elements might be in the game (artist / wonder)
## for each condition (hyper-link) add this element to the condition columns
## if [no leader put 'Other'// Latter will add a Scenario / Map / difficulty ]

## for scenario based achivement
## Go to "https://civilization.fandom.com/wiki/List_of_scenarios_in_Civ6" and for each link a  new column with (0/1)
