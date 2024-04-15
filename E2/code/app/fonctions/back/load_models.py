import joblib
import tensorflow as tf
import os

def load_models(path):

    """Args : path = chemin ou il y a les modèles (chemin/droit/modeldroit.hdf5)
    Retourne model_gd, labelenc_gd, model_droit, labelenc_droit, model_gauche, labelenc_gauche"""
    
    chemin_gauche = os.path.join(path, "gauche")
    chemin_droit = os.path.join(path, "droit")
    chemin_gauche_droit = os.path.join(path, "gauche_droit")

    chemin_modele_gauche = os.path.join(chemin_gauche, "modelegauche.hdf5")
    chemin_modele_droit = os.path.join(chemin_droit, "modeledroit.hdf5")
    chemin_modele_gauche_droit = os.path.join(chemin_gauche_droit, "modelegauche_droit.hdf5")

    modele_gauche = tf.keras.models.load_model(chemin_modele_gauche)
    modele_droit = tf.keras.models.load_model(chemin_modele_droit)
    modele_gauche_droit = tf.keras.models.load_model(chemin_modele_gauche_droit)



    chemin_labelenc_gauche = os.path.join(chemin_gauche, "labelenc")
    chemin_labelenc_droit = os.path.join(chemin_droit, "labelenc")
    chemin_labelenc_gauche_droit = os.path.join(chemin_gauche_droit, "labelenc")

    labelenc_gauche = joblib.load(chemin_labelenc_gauche)
    labelenc_droit = joblib.load(chemin_labelenc_droit)
    labelenc_gauche_droit = joblib.load(chemin_labelenc_gauche_droit)




    return modele_gauche, modele_droit, modele_gauche_droit, labelenc_gauche, labelenc_droit, labelenc_gauche_droit