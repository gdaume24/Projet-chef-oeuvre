import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import pandas as pd
import tensorflow as tf
import cv2
import numpy as np
import json
import matplotlib.pyplot as plt
import joblib
from fonctions.back.load_models import load_models
# from fonctions.back import load_models
# from fonctions.front import *

dirpath = os.path.dirname(__file__)
updir, nothing = os.path.split(dirpath)

json_path = os.path.join(updir, "data")
json_path = os.path.join(json_path, "employees_info.json")

model_path = os.path.join(updir, "modeles")
model_path = os.path.join(model_path, "nouvelle_data_aug")

class ImagePredictionApp:

    def __init__(self, root):
        
        # Définition de la fenêtre
        self.root = root
        self.root.geometry("750x400")
        self.root.title("Application d'Authentification")

        # Load models
        self.model_gauche, self.model_droit, self.model_gauche_droit, self.labelenc_gauche, self.labelenc_droit, self.labelenc_gauche_droit = load_models(model_path)

        # Load infos employés
        with open(json_path, "r", encoding="utf-8") as f:
            self.info_employes = json.load(f)

        # Bouton prédiction
        self.select_button = tk.Button(self.root, text="Sélectionner une image", command=self.load_image)
        self.select_button.place(x=80, y=12)

        
    def load_image(self):

        file_path = tk.filedialog.askopenfilename()

        if file_path:
            
            # Image
            self.pil_image = Image.open(file_path)

            self.tk_image = ImageTk.PhotoImage(self.pil_image)
            image_label = tk.Label(self.root, image=self.tk_image, width=300)
            image_label.place(x=10, y=50)

            # Image_path
            imagepath_label = tk.Label(self.root, text=f"Image path : {file_path}")
            imagepath_label.place(x=10, y=320)            

            # Prediction
            self.image_pour_pred = Image.open(file_path)
            self.image_pour_pred = np.array(self.image_pour_pred)
            self.image_pour_pred = np.expand_dims(self.image_pour_pred, axis=0)


            cote_oeil = self.model_gauche_droit.predict(self.image_pour_pred)
            cote_oeil = np.argmax(cote_oeil)
            cote_oeil = cote_oeil.reshape(-1, 1)
            cote_oeil = self.labelenc_gauche_droit.inverse_transform(cote_oeil)

            if cote_oeil[0] == "left":
                id_salarie = self.model_gauche.predict(self.image_pour_pred)
                id_salarie = np.argmax(id_salarie)
                id_salarie = id_salarie.reshape(-1, 1)
                id_salarie = self.labelenc_gauche.inverse_transform(id_salarie)

            elif cote_oeil == "right":
                id_salarie = self.model_droit.predict(self.image_pour_pred)
                id_salarie = np.argmax(id_salarie)
                id_salarie = id_salarie.reshape(-1, 1)
                id_salarie = self.labelenc_droit.inverse_transform(id_salarie)

            employe_info = self.info_employes[str(id_salarie[0])]
            formatted_info = "\n".join([f"{key} : {value}" for key, value in employe_info.items()])

            info = tk.Label(root, text=formatted_info, justify="left")
            info.place(x=320, y=70)

    

if __name__ == "__main__":
    root = tk.Tk()
    app = ImagePredictionApp(root)
    root.mainloop()
