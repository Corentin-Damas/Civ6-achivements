import pandas as pd
import os

file_path = os.path.dirname(__file__)
file_name = "leaderTable.csv"
full_path = os.path.join(file_path, file_name)


dt = pd.read_csv("leaderTable.csv", index_col=False)


pd.read_html(dt['link'][0])


# Save the datas on the db
# dt.to_csv(full_path, index=False)

