from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
from translation import translate
import sqlite3
import pickle
import uvicorn
import asyncio
import logging
import os
logging.basicConfig(level=logging.WARNING)

# Chemin dossier
chemin = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
# Chemin modèle
chemin_modele = os.path.join(chemin, "pipeline_logisticregression0.83f1.pkl")
# Chemin bdd prédictions
chemin_dossier_racine = os.path.dirname(chemin)
chemin_bdd_predictions = os.path.join(chemin_dossier_racine, "bdd_sqlite_predictions", "predictions.db")

app = FastAPI()

dict_example = {
    "Age" : 25,
    "Gender" : "Homme",
    "self_employed" : "Oui",
    "family_history" : "Oui",
    "work_interfere" : "Souvent",
    "no_employees" : '1-5',
    "remote_work" : "Oui",
    "tech_company" : "Oui",
    "benefits" : "Oui",
    "care_options" : "Oui",
    "wellness_program" : "Oui",
    "seek_help" : "Oui",
    "anonymity" : "Oui",
    "leave" : "Très facilement",
    "mental_health_consequence" : "Oui",
    "phys_health_consequence" : "Oui",
    "coworkers" : "Oui",
    "supervisor" : "Oui",
    "mental_health_interview" : "Oui",
    "phys_health_interview" : "Oui",
    "mental_vs_physical" : "Oui",
    "obs_consequence" : "Oui",
    "id_user" : 2
}

def charger_model():
    model = pickle.load(open(chemin_modele, "rb"))
    return model

model = charger_model()

@app.get("/")
def home():
    return {"details" : "Hellooooooo  !"}
 
@app.post("/predict")
def predict(input_data):
    print(input_data)

    dict_pred_fr = eval(input_data)

    # Traduction du dictionnaire en anglais pour la prédiction
    dict_pred_en = dict_pred_fr.copy()
    for key, value in dict_pred_en.items():
        value = translate(value)
        dict_pred_en[key] = value

    # Prédiction
    input_df = pd.DataFrame(dict_pred_en, index=[0])
    prediction = model.predict(input_df)[0]

    # Insertion des données en base sqlite
    # Complétion du dictionnaire avec le résultat
    if prediction == "Yes":
        reponse = "Besoin d'un traitement"
    elif prediction == "No":
        reponse = "Pas besoin d'un traitement"

    dict_pred_fr["reponse"] = reponse

    # Entrée du questionnaire complet en base
    conn = sqlite3.connect(chemin_bdd_predictions)
    cursor = conn.cursor()
    request = f"""INSERT INTO questionnaire {tuple(dict_pred_fr.keys())}
    VALUES {tuple(dict_pred_fr.values())}"""
    cursor.execute(request)
    conn.commit()
    conn.close()

    return {"prediction" : prediction}

def start_api(loop):
    # uvicorn.run(app, host="127.0.0.1", port=8000)
    config = uvicorn.Config(app, loop=loop)
    server = uvicorn.Server(config)
    loop.run_until_complete(server.serve())

def start_tracking():
    loop.create_task(track.go())

# For debugging with breakpoints in VS Code
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    # Lancer l'API dans un processus séparé
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # start_api(loop)
    # start_tracking(loop)