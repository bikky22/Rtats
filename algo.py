import pandas as pd
import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from preprocess import preprocess

X_test, y_test, X_train_dtm, y_train, X_test_dtm, codeclass = preprocess()
not_learnt = pd.DataFrame(columns=["algo not learnt"])

algo_dict = {   "DT": "DecisionTreeClassifier()",
                "LR": "LogisticRegression()",
                "RF": "RandomForestClassifier()",
                "KNN": "KNeighborsClassifier()",
                "NB": "MultinomialNB()"
}

def algorithm(method):
    """###########( model )############"""
    if method == "DT":
        clf = DecisionTreeClassifier() # 95
    elif method == "LR":
        clf = LogisticRegression() # 93
    elif method == "RF":
        clf = RandomForestClassifier() # 91
    elif method == "KNN":
        clf = KNeighborsClassifier() # 76
    elif method == "NB":
        clf = MultinomialNB() # 66
    else:
        result = not_learnt
        score = """score cannot generated"""
        return result, score
        
    print("model is {}".format(clf))

    model = clf.fit(X_train_dtm, y_train)

    pred = clf.predict(X_test_dtm)

    """#######( score )#########"""
    import sklearn.metrics as skm
    score =  skm.accuracy_score(y_test, pred) #need to clean

    result = pd.DataFrame({'feature': X_test,'actual':y_test, 'predict':pred})

    result["Class Actual"] = result.actual.map(dict(codeclass))
    result["Class Predicted"] = result.predict.map(dict(codeclass))
    result.drop(["actual", "predict"], axis=1, inplace=True)


    return result, score