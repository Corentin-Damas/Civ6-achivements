import pandas as pd
import os

dt = pd.read_csv("leaderTable.csv", index_col=False)
URL = "https://civilization.fandom.com/wiki/"

# pre format all links
dt['link'] = URL + dt['Leader'].str.replace(' ','_')+"_(Civ6)"

file_path = os.path.dirname(__file__)
file_name = "leaderTable.csv"
full_path = os.path.join(file_path, file_name)

dt.to_csv(full_path, index=False)