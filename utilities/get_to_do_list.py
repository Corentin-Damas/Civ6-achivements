import json
import pandas as pd
import os

def getToDoList():
    file_path = os.path.dirname(__file__)
    file_name = "../leaderTable.json"
    full_path = os.path.join(file_path, file_name)

    with open(full_path, "r") as file:
        data = json.load(file)
        dt = pd.json_normalize(data)
        print(dt)

        # write a new line open exel write -| leader / civ achivement not done



getToDoList()