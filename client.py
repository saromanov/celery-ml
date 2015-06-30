import requests


def send_data_for_predict(data):
    r = requests.get('http://127.0.0.1:8080', params={'data': data})
    print(r)

