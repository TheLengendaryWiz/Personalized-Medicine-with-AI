#create a machine learning model with scikit-learn using linear regression
#import the linear regression model
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
le.fit(['a', 'c', 'g', 't'])
#create a linear regression object
regressor = LinearRegression()
#create a feature matrix of the input variables
def linear(X,y,z):
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
    #y = [85,65,95,90,60,77,67]
    #fit the model to the data
    regressor.fit(X, y)
    #create a feature vector of the input variables
    #x_test = [le.transform(z)]
    diff=[]
    for asdf in z:
        diff.append(le.transform(list(asdf)))
    #predict the target vector
    y_pred = regressor.predict(diff)
    #print the predicted target vector
    return list(y_pred)
  except Exception as e:
    return 'Error,Check your input. For more details the error is ' + str(e)