from fastapi.testclient import TestClient
from api import app, chemin_bdd_predictions
import sqlite3

input_data_dict = {
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
    "obs_consequence" : "Oui"
}

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200 
    assert response.json() == {"details" : "Hellooooooo  !"}


def test_prediction():
    
    # Requête à l'API
    response = client.post("/predict", params={"input_data":input_data_dict})

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
    print("valeur automatiquement supprimé de la base")

    assert response.status_code == 200 
    assert response.json() == {"prediction": "Yes"}

