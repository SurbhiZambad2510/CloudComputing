#!/usr/bin/python
from random import random
from flask import Flask, jsonify
import os
import random
import psycopg2
import json

app = Flask(__name__)

# def get_db_connect():
#     # conn_string = "host='db' port= '5432' dbname='web' user='root' password='pass'"
#     # return psycopg2.connect(conn_string)

#     conn_string = psycopg2.connect( 
#     database = os.environ.get('PG_DB'), #"db",
#     user = os.environ.get('PG_USER'), #"root",
#     password ='pass', #os.environ.get('PG_PASS'),
#     host = os.environ.get('DB_HOST'),   #"db", 
#     port = os.environ.get('PG_PORT')   #"5432" 
#     )
    # return psycopg2.connect(conn_string)
    # return psycopg2.connect(host=os.environ.get(database="web", user='root', password='pass', host='127.0.0.1', port= '5432'))

# def get_rec_from_db():
#     q=('SELECT ProductName, ProductPrice FROM meals ORDER BY RANDOM() LIMIT 1;')

#     conn= get_db_connect()
#     cursor= conn.cursor()
#     cursor.execute(q)
#     ml = cursor.fetchall()

#     conn.close()
#     return ml

def getVersion():
    conn = psycopg2.connect(
        database="web", user='root', password='pass', host='db', port= '5432'
    )
#Creating a cursor object using the cursor() method
    cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
    cursor.execute("SELECT mealname, mealprice FROM meals ORDER BY RANDOM() LIMIT 1")

# Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    # print("Connection established to: ",data)

    return json.dumps(data)

#Closing the connection
    conn.close()
    return data


# def get_db_connect():

#     # return psycopg2.connect(host=os.environ.get('DB_HOST')
#     # return psycopg2.connect(port=os.environ.get('DB_PORT')
#     # return psycopg2.connect(user=os.environ.get('PG_USER')
#     # return psycopg2.connect(pass=os.environ.get('PG_PASS')
#     # return psycopg2.connect(host=os.environ.get('DB_HOST'), port, database, user, password)


# def get_rec_from_db():
#     q = SELECT MealName, MealPrice FROM meals
    

#     conn = get_db_connect()
#     cursor = conn.cursor()
#     cursor.execute(q)
#     mr = cursor.fetchall()

#     conn.close()
#     return mr

# meals = [
#         {
#             'name' : 'Paneer Tikka Masala',
#             'Cuisine' : 'Indian',
#             'Price' : '$19.99'
#         },
#         {
#             'name' : 'Chole Bhature',
#             'Cuisine' : 'Indian',
#             'Price' : '$16.99'
#         },
#         {
#             'name' : 'Rajma Chawal',
#             'Cuisine' : 'Indian',
#             'Price' : '$14.99'
#         },
#         {
#             'name' : 'Aloo Muter',
#             'Cuisine' : 'Indian',
#             'Price' : '$15.99'
#         },
#         {
#             'name' : 'Dal Tadka',
#             'Cuisine' : 'Indian',
#             'Price' : '$10.99'
#         },
#         {
#             'name' : 'Shahi Paneer',
#             'Cuisine' : 'Indian',
#             'Price' : '$19.99'
#         },
#         {
#             'name' : 'Arrabiatta Pasta',
#             'Cuisine' : 'Italian',
#             'Price' : '$17.99'
#         },
#         {
#             'name' : 'Alfredo Pasta',
#             'Cuisine' : 'Italian',
#             'Price' : '$14.99'
#         },
#         {
#             'name' : 'Enchiladas',
#             'Cuisine' : 'Mexican',
#             'Price' : '$10.99'
#         },
#         {
#             'name' : 'Tacos',
#             'Cuisine' : 'Mexican',
#             'Price' : '$4.99'
#         },
#         {
#             'name' : 'Burritos',
#             'Cuisine' : 'Mexican',
#             'Price' : '$4.99'
#         },
#         {
#             'name' : 'Nachos',
#             'Cuisine' : 'Mexican',
#             'Price' : '$3.99'
#         },
#         {
#             'name' : 'Italian Cheese Pizza',
#             'Cuisine' : 'Italian',
#             'Price' : '$14.99'
#         },
#         {
#             'name' : 'Cheese Burger',
#             'Cuisine' : 'American',
#             'Price' : '$6.99'
#         },
#         {
#             'name' : 'Fries',
#             'Cuisine' : 'American',
#             'Price' : '$3.99'
#         }
#     ]


# os.environ["API_ENDPOINT"]='meal'
# api_endpoint = os.environ.get("API_ENDPOINT")

@app.route('/')
def get_reco():
    # return get_rec_from_db()
    # random_choice = random.randint(0,15)
    # return meals[random_choice]
    return getVersion()



if __name__ == '__main__':
    port = os.environ.get('API_PORT', 5000)
    app.run(host='0.0.0.0',port=port)
 
 #Amey Darwhekar
 