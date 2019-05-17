import pandas as pd
import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import json


def yapay_knn_fonksiyon(liste):
    veriler = pd.read_csv('veriler.csv')

    x = veriler.iloc[:, 0:13].values  # bağımsız değişkenler->urun id
    y = veriler.iloc[:, 13:].values  # bağımlı değişken->user id

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1, random_state=0)

    sc = StandardScaler()
    X_train = sc.fit_transform(x_train)
    X_test = sc.transform(x_test)

    knn = KNeighborsClassifier(n_neighbors=1, metric='minkowski')
    knn.fit(X_train, y_train.ravel())

    liste_oncesi = liste.replace("%2C", ",")[0:25]
    duzenli_veri = [i for i in liste_oncesi.split(",")]

    veri_listesi = np.array(duzenli_veri)
    veri_listesi = veri_listesi.astype(np.float)

    prediction2 = knn.predict([veri_listesi])
    return (str(prediction2[0]))
# print(r2_score(y_train, knn.predict(X_train)) )