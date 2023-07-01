import requests
import json
import os
from utilities.steam_api import get_game_data
from utilities.get_leaderTable import  getGeneralLeaderInfo
import pandas as pd

file_path = os.path.dirname(__file__)
file_name = "game_data.json"
full_path = os.path.join(file_path, file_name)

# Create the Achivement data or update from Steam
if not os.path.isfile(full_path):
    print("Collecting the datas")
    get_game_data()  ## Crate the Achivement datas
else:
    upDate = input('Do You want to update your datas ? (y,n)')
    upDate.lower()
    if upDate == ('yes' or 'y'):
        get_game_data() ## Update Achivement Datas


# Read the Datas
with open("game_data.json") as openfile:
    data = json.load(openfile)

# JSON is currently { game_name : {Data}} we want to work only on the datas
data_achivement = data["Sid Meier's Civilization VI"]

df_full = pd.json_normalize(data_achivement) # Refactor json to pd dataframe
df_refactored = df_full.drop(columns=["apiname", "unlocktime"]) # Only keep "achived, name, description" cols

print(df_refactored.head(), df_refactored.columns, df_refactored.info())
print(df_refactored["achieved"].value_counts())

# ------ Get All Civilization Datas from Civ 6 wiki ------
## Make sur to get the Civilization datas exist
file_leader = 'leaderTable.csv'
full_path_leader = os.path.join(file_path, file_leader)
if not os.path.isfile(full_path_leader):
    getGeneralLeaderInfo()


### TO DO


## For each leader take the "related achievement"

## For each link the leader to the success in the df (some success can be done by different leaders)
## [df New Columns 'conditions'] for an achivement some elements might be in the game (artist / wonder)
## for each condition (hyper-link) add this element to the condition columns
## if [no leader put 'Other'// Latter will add a Scenario / Map / difficulty ]

## for scenario based achivement
## Go to "https://civilization.fandom.com/wiki/List_of_scenarios_in_Civ6" and for each link a  new column with (0/1)
