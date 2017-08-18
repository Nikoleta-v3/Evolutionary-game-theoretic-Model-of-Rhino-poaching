import pandas as pd
import pathlib

# Replace this with a script that writes it to `data/main.csv`
data_path = pathlib.Path("raw")
dfs = []
for data_file in data_path.glob("*.csv"):
    dfs.append(pd.read_csv(data_file))

df = pd.concat(dfs).drop_duplicates()
df.to_csv("main.csv", index=False)
