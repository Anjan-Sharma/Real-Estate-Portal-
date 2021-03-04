import joblib
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix, accuracy_score
from .models import Spam_filtering
from django.shortcuts import redirect
from listings.models import Listing
from django.contrib.auth.decorators import login_required

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

@login_required(login_url="/accounts/login")
def detect_spam(request,listing_id):
    listing = Listing.objects.get(pk=listing_id)
    if request.method == 'POST':
        listing_id = request.POST['listing_id_value']
        comments = request.POST['message']
        type = request.POST['type']
        example_counts = vectorizer.transform(Convert(comments))
        listToString(comments)
        predictions = mdl.predict(example_counts)
        predict = listToString(predictions)
        spam_detection = Spam_filtering(comments=comments, type=predict, user=request.user, listing=listing)
        spam_detection.save()
        print(listToString(type))
        if predict == 'spam':
            # messages.error(request,
            #                "Looks like you have posted something that is spam in comment so your comment cannot be posted! Thank you!")
            message = ("Looks like you have posted something that is spam in comment so your comment cannot be posted! Thank you!")
        else:
            message = ("Your comment has been posted thank you for your response")
            # messages.success(request, "Your comment has been posted thank you for your response")
        print(message)
        return redirect('/listings/' + listing_id)
