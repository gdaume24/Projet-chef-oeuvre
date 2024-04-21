import requests
import time
import sqlite3
from tkinter import *
from send_email import send_email
import os

# Chemin dossier
chemin = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
# Chemin bdd prédictions
chemin_dossier_racine = os.path.dirname(chemin)
chemin_bdd_predictions = os.path.join(chemin_dossier_racine, "bdd_sqlite_predictions", "predictions.db")

# Exemple de données d'insertion
dict_pred_fr = {
    "Age" : 55,
    "Gender" : "Femme",
    "self_employed" : "Non",
    "family_history" : "Non",
    "work_interfere" : "Souvent",
    "no_employees" : '1-5',
    "remote_work" : "Non",
    "tech_company" : "Non",
    "benefits" : "Non",
    "care_options" : "Non",
    "wellness_program" : "Non",
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

requests.packages.urllib3.disable_warnings()
def track():
    while True:
        try:
            # Effectuer la requête à l'API
            response = requests.post("http://localhost:8000/predict", params={"input_data":str(dict_pred_fr)})

            # Suppresion automatique de la valeur insérée en bdd
            conn = sqlite3.connect(chemin_bdd_predictions)
            cursor = conn.cursor()
            request = """Select MAX(id_questionnaire) from questionnaire"""
            cursor.execute(request)
            max_id = cursor.fetchall()[0][0]
            request = f"""DELETE FROM questionnaire
            WHERE id_questionnaire = {max_id};"""
            cursor.execute(request)
            conn.commit()
            conn.close()
            print("Requête ok")

        except Exception as e:
            # En cas d'erreur lors de la requête
            print(repr(e))
            if "CLEF" in os.environ:
                send_email(repr(e))

        # # Attendre 4 secondes avant d'effectuer la prochaine requête
        time.sleep(4)

track()


