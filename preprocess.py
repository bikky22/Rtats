import pandas as pd

def preprocess():
    """#######( read )########"""
    raw1 = pd.read_excel("./static/Classification.xlsx")
    print(len(raw1))
    raw1.head()
    print(raw1.Classification.value_counts())

    """#########( clean )##########"""
    raw1_p = ""
    for i in raw1.LONGDESC:
        raw1_p = raw1_p + "".join(i)

    from collections import Counter
    raw1_p.lower()
    c = Counter(raw1_p)
    print(c)

    ## remove word that has number
    ## remove -, +, ', &, /, (, ), *, %, , \xa0, ’, $

    raw1 = raw1.apply(lambda col: col.str.lower())
    noneed = "-+'&/()*%\xa0’$"
    for i in raw1.LONGDESC:
        for j in i:
            if j in noneed:
                raw1["LONGDESC"].replace('j',' ', inplace=True)

    # no cleaning is actually happening

    raw1 = raw1.apply(lambda col: col.str.lower())
    #########(preprocess)########
    classlable = list(set(raw1.Classification))

    classcode = dict()
    for x in range(len(tuple(set(raw1.Classification)))):
        classcode[classlable[x]] = x

    codeclass = dict()
    for i, j in enumerate(classcode):
        codeclass[i] = j

    raw1["clas"] = raw1.Classification.map(dict(classcode))

    X = raw1.LONGDESC
    y = raw1.clas

    print(X.shape)
    print(y.shape)

    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 1)
    print(X_train.shape)
    print(X_test.shape)
    print(y_train.shape)
    print(y_test.shape)

    """###############( vector )################"""

    from sklearn.feature_extraction.text import CountVectorizer
    vect = CountVectorizer()
    vect.fit(X_train) 
    X_train_dtm = vect.transform(X_train) # 1815x1092 sparse matrix 17380 stored elements
    print(vect.get_feature_names()) #vocab has unknown vocab, lets remove that
    X_train_dtm.toarray()
    print(X_train_dtm) # <1815x1092 sparse matrix of type '<class 'numpy.int64'>' with 17380 stored elements in Compressed Sparse Row format>

    pd.DataFrame(X_train_dtm.toarray(), columns=vect.get_feature_names())

    X_test_dtm = vect.transform(X_test) #779x1092  sparse mat 7351 stored elements

    return X_test, y_test, X_train_dtm, y_train, X_test_dtm, codeclass
