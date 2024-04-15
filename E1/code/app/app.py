import streamlit as st
import sys
import requests
import pickle
from pathlib import Path
import sqlite3
from streamlit.web import cli as stcli
import streamlit_authenticator as stauth

names = ["Peter Parker", "Rebecca Miller"]
usernames = ["pparker", "rmiller"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "application", "abcdef")

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == False:
    st.error("Veuillez Entrer votre identifiant et mot de passe")

if authentication_status:
    conn = sqlite3.connect(r"C:\Users\Utilisateur\Desktop\PCO\E1\code\bdd_sqlite_predictions\predictions.db")
    cursor = conn.cursor()
    request = f"""select id_user from user where identifiant="{username}";"""
    cursor.execute(request)
    id_user = cursor.fetchall()[0][0]
    conn.close()

    col1, col2 = st.columns([4, 2])
    with col1:
        authenticator.logout("Logout", "main")
    with col2:
        st.text(f"Bienvenue {name}")

    st.title("Détection de besoin de traitement pour la santé mentale avec l'IA")

    # Questionage
    Age = st.text_input("Quel est votre âge ?")

    st.write("##")

    # Question genre
    st.write("Genre")
    Gender = st.radio("1", ["Homme", "Femme", "Autre"], label_visibility="collapsed")

    st.write("##")

    # Question self_employed
    st.write("Êtes-vous travailleur indépendant ?")
    self_employed = st.radio("2", ["Oui", "Non", "Autre"], label_visibility="collapsed")

    st.write("##")

    # Question family_history
    st.write("Avez-vous des antécédents de problèmes de santé mentale dans la famille ?")
    family_history = st.radio("3", ["Oui", "Non"], label_visibility="collapsed")

    st.write("##")

    # Question work_interfere
    st.write("Si vous avez un problème de santé mentale, sentez-vous que cela interfère avec votre travail ?")
    work_interfere = st.radio("4", ["Souvent", "Parfois", "Rarement", "Jamais", "Non concerné"], label_visibility="collapsed")

    st.write("##")

    # Question no_employees
    st.write("Combien d'employés votre entreprise ou organisation possède-t-elle ?")
    no_employees = st.radio("5", ["1-5", "6-25", "26-100", "100-500", "500-1000", "Plus de 1000"], label_visibility="collapsed")

    st.write("##")

    # Question remote_work
    st.write("Travaillez-vous à distance (en dehors du bureau) au moins 50% du temps ?")
    remote_work = st.radio("6", ["Oui", "Non"], label_visibility="collapsed")

    st.write("##")

    # Question tech_company
    st.write("Votre employeur est-il principalement une entreprise ou organisation technologique ?")
    tech_company = st.radio("7", ["Oui", "Non"], label_visibility="collapsed")

    st.write("##")

    # Question benefits
    st.write("Votre employeur offre-t-il des prestations en matière de santé mentale aux employés ?")
    benefits = st.radio("8", ["Oui", "Non", "Je ne sais pas"], label_visibility="collapsed")

    st.write("##")

    # Question care_options
    st.write("Connaissez-vous ces prestations ?")
    care_options = st.radio("9", ["Oui", "Non", "Je ne suis pas sûr"], label_visibility="collapsed")

    st.write("##")

    # Question wellness_program
    st.write("Votre employeur a-t-il déjà abordé la question de la santé mentale dans le cadre d'un programme de bien-être des employés ?")
    wellness_program = st.radio("10", ["Oui", "Non", "Je ne sais pas"], label_visibility="collapsed")

    st.write("##")

    # Question seek_help
    st.write("Votre employeur met-il à votre disposition des ressources permettant d'en savoir plus sur les problèmes de santé mentale et sur la manière de demander de l'aide ?")
    seek_help = st.radio("11", ["Oui", "Non", "Je ne sais pas"], label_visibility="collapsed")

    st.write("##")

    # Question anonymity
    st.write("Votre anonymat est-il protégé si vous choisissez de profiter des ressources de traitement de la santé mentale ou de la toxicomanie ?")
    anonymity = st.radio("12", ["Oui", "Non", "Je ne sais pas"], label_visibility="collapsed")

    st.write("##")

    # Question leave
    st.write("Est-il facile pour vous de prendre un congé médical pour un problème de santé mentale ?")
    leave = st.radio("13", ["Très facilement", "Assez facilement", "Assez difficilement", "Très difficilement", "Je ne sais pas"], label_visibility="collapsed")

    st.write("##")

    # Question mental_health_consequence
    st.write("Pensez-vous que le fait de parler d'un problème de santé mentale à votre employeur aurait des conséquences négatives ?")
    mental_health_consequence = st.radio("14", ["Oui", "Non", "Peut-être"], label_visibility="collapsed")

    st.write("##")

    # Question phys_health_consequence
    st.write("Pensez-vous que le fait de parler d'un problème de santé physique à votre employeur aurait des conséquences négatives ?")
    phys_health_consequence = st.radio("15", ["Oui", "Non", "Peut-être"], label_visibility="collapsed")

    st.write("##")

    # Question coworkers
    st.write("Seriez-vous prêt à discuter d'un problème de santé mentale avec vos collègues de travail ?")
    coworkers = st.radio("16", ["Oui", "Non", "Certains d'entre eux"], label_visibility="collapsed")

    st.write("##")

    # Question supervisor
    st.write("Seriez-vous prêt à discuter d'un problème de santé mentale avec votre (vos) supérieur(s) hiérarchique(s) ?")
    supervisor = st.radio("17", ["Oui", "Non", "Certains d'entre eux"], label_visibility="collapsed")

    st.write("##")

    # Question mental_health_interview
    st.write("Parleriez-vous d'un problème de santé mentale à un employeur potentiel lors d'un entretien ?")
    mental_health_interview = st.radio("18", ["Oui", "Non", "Peut-être"], label_visibility="collapsed")

    st.write("##")

    # Question phys_health_interview
    st.write("Parleriez-vous d'un problème de santé physique à un employeur potentiel lors d'un entretien ?")
    phys_health_interview = st.radio("19", ["Oui", "Non", "Peut-être"], label_visibility="collapsed")

    st.write("##")

    # Question mental_vs_physical
    st.write("Pensez-vous que votre employeur prend autant au sérieux la santé mentale que la santé physique ?")
    mental_vs_physical = st.radio("20", ["Oui", "Non", "Je ne sais pas"], label_visibility="collapsed")

    st.write("##")

    # Question obs_consequence
    st.write("Avez-vous entendu parler ou observé des conséquences négatives pour les collègues souffrant de troubles mentaux sur votre lieu de travail ?")
    obs_consequence = st.radio("21", ["Oui", "Non"], label_visibility="collapsed")

    # Bouton prédiction
    bouton = st.button("Lancer la prédiction")
    if bouton:
        dict_pred_fr = {"Age" : Age,
        "Gender" : Gender,
        "self_employed" : self_employed,
        "family_history" : family_history,
        "work_interfere" : work_interfere,
        "no_employees" : no_employees,
        "remote_work" : remote_work, 
        "tech_company" : tech_company,
        "benefits" : benefits, 
        "care_options" : care_options, 
        "wellness_program" : wellness_program, 
        "seek_help" : seek_help,
        "anonymity" : anonymity, 
        "leave" : leave, 
        "mental_health_consequence" : mental_health_consequence,
        "phys_health_consequence" : phys_health_consequence, 
        "coworkers" : coworkers, 
        "supervisor" : supervisor,
        "mental_health_interview" : mental_health_interview, 
        "phys_health_interview" : phys_health_interview,
        "mental_vs_physical" : mental_vs_physical, 
        "obs_consequence" : obs_consequence}

        dict_pred_fr["id_user"] = id_user

        # Je mets le dictionnaire en string parce que l'api attends une string
        dict_pred_fr = str(dict_pred_fr)

        response = requests.post("http://127.0.0.1:8000/predict", params={"input_data":dict_pred_fr})
        print(f"reponse ==== {response}")
        reponse = response.json()["prediction"]
        
        if reponse=="Yes":
            texte = "Vous devriez considérer le fait de prendre un traitement ou de chercher de l'aide."
        elif reponse=="No":
            texte = "Vous êtes en bonne santé mentale."

        st.text(texte)
