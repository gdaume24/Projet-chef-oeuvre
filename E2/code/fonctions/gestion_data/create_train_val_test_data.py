import os
import tqdm
import random
import shutil

def create_train_val_test_data(basic_path):

  """Fonction qui créé un dossier data mais dans lequel les photos sont regroupées dans des dossiers train, val, test, cela permet de distinguer les photos pour la constitution des
  différents jeux de données (oeil gauche, oeil gauche/droit...) afin que les modèles s'entraînent toujours sur les mêmes photos.

  Le dossier est créé à la racine du chemin "basic_path".
  
  Keyword arguments:
  basic_path -- the path where the original data is (1, 2, 3 ... -> left, right -> photo1, photo2 ...)
  """

  # Création chemin du dossier train_val_test_data
  chemin_dossier_racine, dossier_data = os.path.split(basic_path)
  train_val_test_data_path = os.path.join(chemin_dossier_racine, 'train_val_test_data')


  for dossier_employe in tqdm.tqdm(os.listdir(basic_path)):
    dossier_employe_path = os.path.join(basic_path, dossier_employe)
    nouveau_dossier_employe = os.path.join(train_val_test_data_path, dossier_employe)
    for cote_oeil in os.listdir(dossier_employe_path):
      dossier_oeil_employe_path = os.path.join(dossier_employe_path, cote_oeil)
      nouveau_dossier_oeil = os.path.join(nouveau_dossier_employe, cote_oeil)

      photos = []
      for photo in os.listdir(dossier_oeil_employe_path):
        if photo.lower().endswith(('.bmp', '.jpg', '.jpeg', '.png', '.gif')):
          chemin_photo = os.path.join(dossier_oeil_employe_path, photo)
          photos.append(chemin_photo)
      
      random.shuffle(photos)

      # Créé les 3 dossiers de sortie
      nouveau_dossier_train = os.path.join(nouveau_dossier_oeil, "train")
      nouveau_dossier_val = os.path.join(nouveau_dossier_oeil, "val")
      nouveau_dossier_test = os.path.join(nouveau_dossier_oeil, "test")
      os.makedirs(nouveau_dossier_train)
      os.makedirs(nouveau_dossier_val)
      os.makedirs(nouveau_dossier_test)

      for photo in photos[:3]:
        shutil.copy(photo, nouveau_dossier_train)

      shutil.copy(photos[3], nouveau_dossier_val)
      shutil.copy(photos[4], nouveau_dossier_test)