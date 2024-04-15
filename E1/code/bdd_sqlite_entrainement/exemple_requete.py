import pandas as pd
import sys
import os
import sqlite3
import inspect


# Sélection des âges entre 30 et 40 ans
con = sqlite3.connect("db.db")
df = pd.read_sql_query("select * from Questionnaires where Age >= 30 and Age <= 40; ", con)
con.close()
print(df)
