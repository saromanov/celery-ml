import requests

#Example of sending test data
def send_data_for_predict(data):
    r = requests.get('http://127.0.0.1:8080', params={'data': data})
    print("DATA: ", r)

send_data_for_predict([0.4,0.5,0.7,0.1])
