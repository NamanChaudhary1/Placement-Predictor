from django.shortcuts import render




from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle


def predict(request):
    if request.method=='POST':
        # LogisticRegression was used on the dataset availabe at:- https://drive.google.com/file/d/17nlKhuMBi6F0HDKoQUvPJTSV2OVd8b6Y/view
        filename = 'finalized_model.sav'
        loaded_model = pickle.load(open(filename, 'rb'))

        val1 = float(request.POST['n1'])
        val2 = float(request.POST['n2'])
        val3 = float(request.POST['n3'])
        val4 = float(request.POST['n4'])
        val5 = float(request.POST['n5'])
        val6 = float(request.POST['n6'])
        val7 = float(request.POST['n7'])


        pred=loaded_model.predict([[val1, val2, val3,val4, val5, val6, val7]])

        if pred == [0]:
            res="You may not be placed !!."
            # print("You are not placed !.")
        else:
           res="You are placed !!."
        #    print("You are placed !." )   

        context={
            'result':res
        }

        return render(request,'result.html',context)

    return render(request,'index.html')