import pandas as pd
import sys
import os
import sqlite3
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
data_path = os.path.join(parentdir, "data/survey.csv")
from EDA.stratégie_nettoyage_donnees import nettoyage_df

con = sqlite3.connect("db.db")

df = pd.read_csv(data_path)
df = nettoyage_df(df)
df['ids'] = df.index
df.to_sql('Questionnaires', con=con, if_exists='replace', index=False, dtype={'ids': 'INTEGER PRIMARY KEY AUTOINCREMENT'})

print("Les données ont été ajoutées en base.")
