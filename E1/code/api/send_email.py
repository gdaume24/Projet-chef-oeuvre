import smtplib, ssl
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(message):
    # on rentre les renseignements pris sur le site du fournisseur
    smtp_address = 'smtp.gmail.com'
    smtp_port = 465

    # on rentre les informations sur notre adresse e-mail
    email_address = 'geoffroy.daumer@gmail.com'

    # on rentre les informations sur le destinataire
    email_receiver = 'geoffroy.daumer@gmail.com'

    # on crée la connexion
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
        # connexion au compte
        server.login(email_address, os.environ["CLEF"])
        # envoi du mail
        server.sendmail(email_address, email_receiver, message)