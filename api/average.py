import pandas as pd

df = pd.read_json(r'/Users/milouvanlaarhoven/PycharmProjects/zomer2020/api/csvjson.json')

df.drop(df.loc[df["Hoe voel je je vandaag?"] == ""].index, inplace=True)

df["Hoe voel je je vandaag?"] = df["Hoe voel je je vandaag?"].astype(float)

print(df["Hoe voel je je vandaag?"].mean())
