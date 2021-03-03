import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix, accuracy_score
from .models import Spam_filtering

# Create your views here.
mdl = joblib.load("model_pickle")
X = pd.read_excel('test.xlsx', engine='openpyxl')
X = X[['result', 'comments']]
DF = pd.DataFrame(X)
vectorizer = CountVectorizer()
y_pred = vectorizer.fit_transform(DF['comments'])
mdl.fit(y_pred, DF['result'])
y_test = mdl.predict(y_pred)
accuracy = accuracy_score(y_test, DF['result'])


def Convert(string):
    li = list(string.split("-"))
    return li


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1


def detect_spam():
    message = "Hello"
    example_counts = vectorizer.transform(Convert(message))

    predictions = mdl.predict(example_counts)
    predict = listToString(predictions)
    spam_detection = Spam_filtering(comments=message, type=predict)
    spam_detection.save()
    print(predict)
