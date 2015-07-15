import celery
from sklearn import svm
from sklearn.externals import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import os
import datetime

app = celery.Celery("ml")
app.config_from_object('celeryconfig')

@app.task
def compute_model(params):
    data = load_iris()
    username = params['username']
    strtime = getStrTime()
    model = svm.SVC()
    model.fit(data.data, data.target)
    joblib.dump(model, '../{0}_{1}_svmmodel.pkl'.format(username, strtime), compress=9)
    return 1


@app.task
def compute_rfmodel(params, data):
    '''
    Args:
        params - contain dict of username and other params
    '''
    username = params['username']
    strtime = getStrTime()
    model = RandomForestClassifier()
    model.fit(data)
    joblib.dump(model, '../{0}_{1}_rfmodel.pkl'.format(username, strtime), compress=9)

@app.task()
def get_result(data):
    if not os.path.exists('../svmmodel.pkl'):
        return {'result':'', 'error': 'File with model is not found'}
    model = joblib.load('../svmmodel.pkl')
    return {'result': str(model.predict(data)[0]), 'error': ''}


def getStrTime():
    ''' Return current time in str format
    '''
    return datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%M_%S')

