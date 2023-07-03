import requests
import json
import os
from utilities.steam_api import get_game_data
from utilities.get_leaderTable import  getGeneralLeaderInfo
from utilities.get_Achievements import getAchievements
import pandas as pd

file_path = os.path.dirname(__file__)
file_name = "game_data.json"
full_path = os.path.join(file_path, file_name)

# --------------------- Get Steam Data --------------------------
# Create the Achievement data or update from Steam
if not os.path.isfile(full_path):
    print("Collecting the datas")
    get_game_data()  ## Crate the Achivement datas
else:
    upDate = input('Do You want to update your datas ? (y,n)')
    upDate.lower()
    if upDate == ('yes' or 'y'):
        get_game_data() ## Update Achievement Datas

# Read the Datas
with open("game_data.json") as openfile:
    data = json.load(openfile)

# JSON is currently { game_name : {Data}} we want to work only on the datas
data_achievement = data["Sid Meier's Civilization VI"]

df_full = pd.json_normalize(data_achievement) # Refactor json to pd dataframe
df_steam = df_full.drop(columns=["apiname", "unlocktime"]) # Only keep "achieved, name, description" cols

# ------ Get All Civilization Datas from Civ 6 wiki ------
## Make sur to get the Civilization datas exist
file_leader = 'leaderTable.csv'
full_path_leader = os.path.join(file_path, file_leader)
if not os.path.isfile(full_path_leader):
    getGeneralLeaderInfo()
    getAchievements()


# Get scenario base and map base

# -------------- Join the tables --------------------
df_Civ = pd.read_csv('leaderTable.csv')
print("Steam info: ",df_steam.columns)
print("Civ info:",df_Civ.columns)


# for index, row in df_steam.iterrows():
#     for idx,r in df_Civ.iterrows():
#         print( r['achievements'][0])
#         for item in r['achievements']:
#             print(item)
#             print(r['achievements'][item])
#             if r['achievements'][item] == row["name"]:
#                 row['civ'] = (df_Civ['Leader'][idx], df_Civ["Civilization"][idx])
#                 print("found")

# BUG When taking back a CSV file with an array inside the array will be transform into a string '[...]'
# Witch will break the logic/  change the file type

# joined_db = "joined_db.csv"
# joined_db_path = os.path.join(file_path, joined_db)
# df_steam.to_csv(joined_db_path, index=False)



##Join the table on the achivement name

### TO DO


## [df New Columns 'conditions'] for an achivement some elements might be in the game (artist / wonder)
## for each condition (hyper-link) add this element to the condition columns
## if [no leader put 'Other'// Latter will add a Scenario / Map / difficulty ]

## for scenario based achivement
## Go to "https://civilization.fandom.com/wiki/List_of_scenarios_in_Civ6" and for each link a  new column with (0/1)
