from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
le.fit(['a', 'c', 'g', 't'])


def Knn(data,target,test):
  try:
    '''data=['gctattgaaa','tgaacttcac','atacataccg','cagcatgcaa','gcgtgactca','agaggagtcc','cccgttgtat']

    target=[1,1,3,3,2,1,2]'''
    i=0
    while i<len(data):
      v=list(data[i])
      data[i]=v
      i+=1

    for iq in data:
      iter=0
      while iter<len(iq):
        if iq[iter]=='a':
          iq[iter]=0
        if iq[iter]=='c':
          iq[iter]=1
        if iq[iter]=='g':
          iq[iter]=2
        if iq[iter]=='t':
          iq[iter]=3
        iter+=1

    datanp=np.array(data)
    targetnp=np.array(target)

    print(datanp)
    print(targetnp)

    X_train, X_test, y_train, y_test = train_test_split(datanp, targetnp, random_state=0)


    kn = KNeighborsClassifier(n_neighbors=1)
    kn.fit(X_train, y_train)

    #valtocheck = list('ctcggacttc')
    diff=[]
    for asdf in test:
        diff.append(le.transform(list(asdf)))
    '''valtocheck = test
    print(valtocheck)
    for idx, item in enumerate(valtocheck):
        if item == 'a':
            valtocheck[idx] = 0
        if item == 'c':
            valtocheck[idx] = 1
        if item == 'g':
            valtocheck[idx] = 2
        if item == 't':
            valtocheck[idx] = 3
    x_new = np.array([valtocheck])'''
    #x_new = np.array([['catggacttc']])



    prediction = kn.predict(diff)

    print("Predicted target value: {}\n".format(list(prediction)))
    print("Test score: {:.2f}".format(kn.score(X_test, y_test)))
    return list(prediction)
  except Exception as e:
    return 'Error,Check your input. For more details the error is ' + str(e)

if __name__=="__main__":
    X = ['gctattgaaa','tgaacttcac','atacattccg','cagcatgcaa','gcgtgactca','agaggagtcc','cccgttgtat']
    y = [85,65,93,90,60,77,67]
    print(Knn(X,y,['ccggttgtct','gcgtgactca']))