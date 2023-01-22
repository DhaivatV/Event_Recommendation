import requests
import pandas as pd

Event_Name = []
Event_Description = []
Fields = []
response = requests.get("http://3.111.149.79/data")
data = response.json()
k = data.values()
for items in k:
    for item in items:
        Event_Name.append(item[0])
        Event_Description.append(item[1])
        Fields.append(item[2:])

df = pd.DataFrame()
df['Event'] = Event_Name
df['Event_Description'] = Event_Description
df['Fields'] = Fields

print(df)
df.to_csv("Event_Dataset.csv")