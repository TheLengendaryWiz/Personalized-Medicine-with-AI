from flask import Flask
from flask import request
from adaboost import adaboost
from KNN import Knn
from DTR import dtr
from linear_regression import linear
from logistic_regression import logistic
from SVC import svc
from flask_cors import CORS
app = Flask('app')
CORS(app)
@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/adaboost')
def get_adaboost():
  try:
    train = request.args.get('train')
    traintarget = request.args.get('train_target')
    test_strings=request.args.get('test_strings')
    train=train.lower().split(',')
    test_strings=test_strings.lower().split(',')
    traintarget=traintarget.lower().split(',')
    tobereturned=adaboost(train,traintarget,test_strings)
    integer_map = map(float, tobereturned)
    integer_list = list(integer_map)
    return str(integer_list)
  except Exception as e:
    return 'Error,Check your input. For more details the error is ' + str(e)
    
  #return f'{traintarget} is train target and train in {train} and test strigns are {test_strings}'

@app.route('/dtr')
def get_dtr():
  try:
    train = request.args.get('train')
    traintarget = request.args.get('train_target')
    test_strings=request.args.get('test_strings')
    train=train.lower().split(',')
    traintarget=traintarget.lower().split(',')
    test_strings=test_strings.lower().split(',')
    tobereturned=dtr(train,traintarget,test_strings)
    integer_map = map(float, tobereturned)
    integer_list = list(integer_map)
    return str(integer_list)
  except Exception as e:
    return 'Error,Check your input. For more details the error is ' + str(e)

@app.route('/knn')
def get_knn():
  try:
    train = request.args.get('train')
    traintarget = request.args.get('train_target')
    test_strings=request.args.get('test_strings')
    traintarget=traintarget.lower().split(',')
    train=train.lower().split(',')
    test_strings=test_strings.lower().split(',')
    tobereturned=Knn(train,traintarget,test_strings)
    integer_map = map(float, tobereturned)
    integer_list = list(integer_map)
    return str(integer_list)
  except Exception as e:
    return 'Error,Check your input. For more details the error is ' + str(e)


@app.route('/linear')
def get_linear():
  try:
    train = request.args.get('train')
    test_strings=request.args.get('test_strings')
    traintarget = request.args.get('train_target')
    train=train.lower().split(',')
    test_strings=test_strings.lower().split(',')
    traintarget=traintarget.lower().split(',')
    tobereturned=linear(train,traintarget,test_strings)
    integer_map = map(float, tobereturned)
    integer_list = list(integer_map)
    return str(integer_list)
  except Exception as e:
    return 'Error,Check your input. For more details the error is ' + str(e)
    

@app.route('/logistic')
def get_logistic():
  try:
    train = request.args.get('train')
    test_strings=request.args.get('test_strings')
    traintarget = request.args.get('train_target')
    train=train.lower().split(',')
    test_strings=test_strings.lower().split(',')
    traintarget=traintarget.lower().split(',')
    tobereturned=logistic(train,traintarget,test_strings)
    integer_map = map(float, tobereturned)
    integer_list = list(integer_map)
    return str(integer_list)
  except Exception as e:
    return 'Error,Check your input. For more details the error is ' + str(e)
    

@app.route('/svc')
def get_svc():
  try:
    train = request.args.get('train')
    test_strings=request.args.get('test_strings')
    traintarget = request.args.get('train_target')
    train=train.lower().split(',')
    traintarget=traintarget.lower().split(',')
    test_strings=test_strings.lower().split(',')
    tobereturned=svc(train,traintarget,test_strings)
    integer_map = map(float, tobereturned)
    integer_list = list(integer_map)
    return str(integer_list)
  except Exception as e:
    return 'Error,Check your input. For more details the error is ' + str(e)




from waitress import serve
serve(app, host="0.0.0.0", port=8080)