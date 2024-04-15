from translation import translate
from pydantic import BaseModel
import pickle
import sqlite3
from send_email import send_email
import pandas as pd
import os
import sqlite3

try:
    print(sd,oml)
except Exception as e:
    # En cas d'erreur lors de la requête
    print(repr(e))
    send_email(repr(e))
    # print("Erreur lors de la requête à l'API:", e)
