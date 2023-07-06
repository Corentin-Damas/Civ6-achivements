import json
import pandas as pd
import os
import csv
def getToDoList():
    file_path = os.path.dirname(__file__)
    file_name = "../leaderTable.json"
    full_path = os.path.join(file_path, file_name)

    with open(full_path, "r") as file:
        data = json.load(file)

    temp_json = []


    for civ in data:

        for achi in civ['achievements']:
            if achi == "Thalassocratophile":
                achi = {"Thalassocratophile": "Have 5 cities on landmasses 5 or less tiles with Indonesia", "achived": 0} # scrap failed for that success
            temp_achi = {}
            temp_achi["leader"] = civ["leader"]
            temp_achi["civilization"] = civ["civilization"]
            temp_achi["name"] = list(achi.keys())[0]
            temp_achi["description"] = list(achi.values())[0]
            temp_achi['achived']= achi['achived']
            temp_json.append(temp_achi)

    df = pd.json_normalize(temp_json).set_index('leader')

    df_todo = df.query("achived==0")
    df_done = df.query("achived==1")
    with pd.ExcelWriter('../achievement_todo.xlsx') as writer:

        df_todo.to_excel(writer, sheet_name='To_do_achievements')
        df_done.to_excel(writer, sheet_name='Done_achievements')

