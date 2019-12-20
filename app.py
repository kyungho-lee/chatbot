from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world!'

api_url = 'https://api.telegram.org'
token = '998908682:AAEYcmyM_5cdp_F_9q6lojui1ji8G6wGhNo'
chat_id = '1017433374'

@app.route('/send/<text>')
def send(text):
    res = requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return 'ok!'



app.run(debug=True)