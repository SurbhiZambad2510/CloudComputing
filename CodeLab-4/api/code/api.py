from random import random
from flask import Flask
import os
import random
import json 

app = Flask(__name__)

meal_plan = {'Baked Lasagna':'$21.95',
            'Chicken Marsala':'$25.95',
            'Fiorillo House Salad':'$8.95',
            'Pasta Romano':'$9.75',
            'Fried Calamari':'$16.95',
            'Sun-dried Tomato and Basil':'$21.95',
            'Cannoli':'$9',
            'Caesar Salad':'$16.90',
            'Cheese Chilly Toast':'$12.55',
            'Penne Pasta':'$15.95',
            'Bruschetta':'$12.95',
            'Tiramisu':'$7.55',
            'Baked Beans on Bread':'$5',
            'Chocolate Cheesecake':'$4.95',
            'Raspberry Cheesecake':'$4.95'}

os.environ["API_ENDPOINT"]='meal'

api_endpoint = os.environ.get("API_ENDPOINT")
@app.route('/'+api_endpoint)
def get_reco():
    return json.dumps(random.choice(list(meal_plan.items())))

if __name__ == '__main__':
    port = os.environ.get('API_PORT',5000)
    app.run(host='0.0.0.0',port=port)
 