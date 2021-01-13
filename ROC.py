import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import plot_roc_curve
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score


def ROC ():
    import pandas as pd
    import numpy as np
    dataset = pd.read_csv("C:/Users/aviba/PycharmProjects/colors/2var.csv")
    print(dataset.head())
    X = dataset.iloc[:, 0:9].values
    y = dataset.iloc[:, 9].values

    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
    # print(X_train)

    svc = SVC(random_state=42)
    svc.fit(X_train, y_train)
    svc_disp = plot_roc_curve(svc, X_test, y_test)
    plt.show()

    from sklearn.ensemble import RandomForestClassifier
    rfc = RandomForestClassifier(n_estimators=1000, random_state=42)
    rfc.fit(X_train, y_train)
    ax = plt.gca()
    rfc_disp = plot_roc_curve(rfc, X_test, y_test, ax=ax, alpha=0.8)
    svc_disp.plot(ax=ax, alpha=0.8)
    plt.show()



ROC ()



