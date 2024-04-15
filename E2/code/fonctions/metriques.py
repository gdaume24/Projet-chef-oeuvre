from sklearn.utils.multiclass import unique_labels
from sklearn.metrics import confusion_matrix
import pandas as pd
import seaborn as sns

def plot_matrix(y_test, y_pred):
    "C i,j matrxi = i ligne et j colonnes, ligne = réalité et colonne = prediction"
    labels = unique_labels(y_test)
    columns = [f'Predicted {label}' for label in labels]
    indices = [f'Actual {label}' for label in labels]
    table = pd.DataFrame(confusion_matrix(y_test, y_pred),
                        columns=columns, index=indices)
    
    return sns.heatmap(table, annot=True, fmt="d", cmap="viridis")