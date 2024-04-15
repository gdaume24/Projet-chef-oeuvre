import os
from PIL import Image
import tqdm
import numpy as np
import matplotlib.pyplot as plt


def get_data_for_training(train_val_test_data_path, side_eye):

    def shuffle_data(X, y):
        data = list(zip(X, y))
        np.random.shuffle(data)
        X, y = zip(*data)

        return X, y

    """Retourne un jeu de données de type X_train, y_train, X_val, y_val, X_test, y_test en fonction de l'entraînement que l'on souhaite effectuer
    
    Keyword arguments:
    side_eye -- "left" si on veut des données du type: photo oeil gauche en X, numéro employé en y
                "right" pour photo oeil droit
                "left-right" pour photos des deux yeux en X et coté oeil en y
    """

    X_train = []
    y_train = []
    X_val = []
    y_val = []
    X_test = []
    y_test = []


    if side_eye in ["left", "right"]:

        for dossier_employe in tqdm.tqdm(os.listdir(train_val_test_data_path)):
            dossier_employe_path = os.path.join(train_val_test_data_path, dossier_employe)
            dossier_oeil_employe_path = os.path.join(dossier_employe_path, side_eye)
            for type_dossier in os.listdir(dossier_oeil_employe_path):
                type_dossier_path = os.path.join(dossier_oeil_employe_path, type_dossier)
                for image in os.listdir(type_dossier_path):
                    image_path = os.path.join(type_dossier_path, image)
                    image = Image.open(image_path)
                    image_array = np.array(image)

                    if type_dossier == "train":
                        X_train.append(image_array)
                        y_train.append(dossier_employe)

                    elif type_dossier == "val":
                        X_val.append(image_array)
                        y_val.append(dossier_employe)

                    elif type_dossier == "test":
                        X_test.append(image_array)
                        y_test.append(dossier_employe)



    elif side_eye == "left-right":
              

        for dossier_employe in tqdm.tqdm(os.listdir(train_val_test_data_path)):
            dossier_employe_path = os.path.join(train_val_test_data_path, dossier_employe)
            for cote_oeil in os.listdir(dossier_employe_path):
                dossier_oeil_employe_path = os.path.join(dossier_employe_path, cote_oeil)
                for type_dossier in os.listdir(dossier_oeil_employe_path):
                    type_dossier_path = os.path.join(dossier_oeil_employe_path, type_dossier)
                    for image in os.listdir(type_dossier_path):
                        image_path = os.path.join(type_dossier_path, image)
                        image = Image.open(image_path)
                        image_array = np.array(image)

                        if type_dossier == "train":
                            X_train.append(image_array)
                            y_train.append(cote_oeil)

                        elif type_dossier == "val":
                            X_val.append(image_array)
                            y_val.append(cote_oeil)

                        elif type_dossier == "test":
                            X_test.append(image_array)
                            y_test.append(cote_oeil)


    X_train, y_train = shuffle_data(X_train, y_train)
    X_val, y_val = shuffle_data(X_val, y_val)
    X_test, y_test = shuffle_data(X_test, y_test)


    return X_train, y_train, X_val, y_val, X_test, y_test

def check_donnees(X, y, numero):
    plt.imshow(X[numero])
    print(y[numero])