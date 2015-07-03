import celery
from sklearn import svm
from sklearn.externals import joblib
from sklearn.datasets import load_iris
import os

app = celery.Celery("ml")
app.config_from_object('celeryconfig')

@app.task
def compute_model():
    data = load_iris()
    model = svm.SVC()
    model.fit(data.data, data.target)
    joblib.dump(model, '../svmmodel.pkl', compress=9)


@app.task(serializer='json')
def get_result(data):
    if not os.path.exists('../svmmodel.pkl'):
        return {'result':'', 'error': 'File with model is not found'}
    model = joblib.load('../svmmodel.pkl')
    return {'result': model.predict(data), 'error': ''}
