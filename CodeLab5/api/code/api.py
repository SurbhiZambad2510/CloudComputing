from random import random
from flask import Flask, jsonify
import os
import random
import psycopg2
import json

app = Flask(__name__)

def get_db_connect():

    conn_string = psycopg2.connect( 
    database = os.environ.get('PG_DB'), 
    user = os.environ.get('PG_USER'), 
    password ='pass', 
    host = os.environ.get('DB_HOST'),   
    port = os.environ.get('PG_PORT')  
    )
    return psycopg2.connect(conn_string)

def get_rec_from_db():
    q=('SELECT ProductName, ProductPrice FROM meals ORDER BY RANDOM() LIMIT 1;')

    conn= get_db_connect()
    cursor= conn.cursor()
    cursor.execute(q)
    ml = cursor.fetchall()

    conn.close()
    return ml

def getVersion():
    conn = psycopg2.connect(
        database="web", user='root', password='pass', host='db', port= '5432'
    )

    cursor = conn.cursor()


    cursor.execute("SELECT mealname, mealprice FROM meals ORDER BY RANDOM() LIMIT 1")

    data = cursor.fetchone()
    print("Connection established to: ",data)

    return json.dumps(data)

    conn.close()
    return data



@app.route('/')
def get_reco():
    return getVersion()



if __name__ == '__main__':
    port = os.environ.get('API_PORT', 5000)
    app.run(host='0.0.0.0',port=port)
 
 