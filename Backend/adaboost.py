#create a machine learning model with scikit-learn using linear regression
#import the linear regression model
from sklearn.ensemble import AdaBoostClassifier
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
le.fit(['a', 'c', 'g', 't'])
regressor = AdaBoostClassifier()
def adaboost(X,y,z):
#create a linear regression object
  #create a feature matrix of the input variables
  try:
    #X = ['gctattgaaa','tgaacttcac','atacattccg','cagcatgcaa','gcgtgactca','agaggagtcc','cccgttgtat']
    for i, n in enumerate(X):
        X[i] = list(n)
    for asdf in X:
      for asa,qw in enumerate(asdf):
        if qw=='a':
          asdf[asa]=0
        if qw=='c':
          asdf[asa]=1
        if qw=='g':
          asdf[asa]=2
        if qw=='t':
          asdf[asa]=3

    print(X)

      
    #create a target vector
    #y = [85,65,93,90,60,77,67]
    #fit the model to the data
    regressor.fit(X, y)
    #create a feature vector of the input variables
    #x_test = [le.transform(list('ggacatcttc'))]
    diff=[]
    for asdf in z:
      diff.append(le.transform(list(asdf)))
    #x_test = [le.transform(diff)]
    #predict the target vector
    y_pred = regressor.predict(diff)
    #print the predicted target vector
    return list(y_pred)
  except Exception as e:
    return 'Error,Check your input. For more details the error is ' + str(e)

if __name__=="__main__":
  X = ['gctattgaaa','tgaacttcac','atacattccg','cagcatgcaa','gcgtgactca','agaggagtcc','cccgttgtat']
  y = [85,65,93,90,60,77,67]
  print(adaboost(X,y,['ccggttgtct','gcgtgactca']))