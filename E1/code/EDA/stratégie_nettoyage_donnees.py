import pandas as pd


def nettoyage_df(df):

    # Valeurs manquantes
    df["self_employed"].fillna("Other", inplace=True)
    df["work_interfere"].fillna("Not concerned", inplace=True)

    # Suppression colonnes
    deleted_columns = ['Timestamp"', "Country", "state", "comments"]
    df = df.drop(deleted_columns, axis=1)

    # Suppression lignes
    df = df[(df['Age'] >= 0) & (df['Age'] <= 100)]

    # Simplification de la colonne Genre
    def grouper_genres(genre):

        ancien_genre = genre.lower()

        if ancien_genre in ['male', 'm', 'man', "male ", "man"]:
            nouveau_genre = "Male"
        elif ancien_genre in ['female', 'f', 'woman', "female "]:
            nouveau_genre = "Female"
        else:
            nouveau_genre = "Other"
        return nouveau_genre

    df["Gender"] = df["Gender"].apply(grouper_genres)

    return df


