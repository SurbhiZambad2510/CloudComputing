import requests
from flask import Flask,render_template
from flask import request
import os

app = Flask(__name__)

@app.route('/')
def get_reco():
    apihost = os.environ.get('API_HOST','api')
    apiport = os.environ.get('API_PORT',5000)
    url="http://" + apihost + ":" + apiport + "/"
    r =requests.get(url)
    food_item = r.text
    return render_template('food.html',food=food_item)
    
if __name__ == '__main__':
    port = os.environ.get('CONSUMER_PORT',81)
    app.run(host='0.0.0.0',port=port)
