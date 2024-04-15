import random
import matplotlib.pyplot as plt

def show_augmentation(data_augmentation, X, y):
    len_data = len(X)
    random_index = random.randint(0, len_data - 1)
    print(y[random_index])
    plt.axis('off')
    plt.imshow(data_augmentation(X)[random_index].numpy().astype("uint8"))