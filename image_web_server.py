#!/usr/bin/env python

from flask import Flask, jsonify, render_template, Response, request
import json
import pexpect
import os
import pymysql.cursors
import pymysql
from random import randint


app = Flask(__name__)


#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
app.debug = True


def get_image_from_db():
    ''' 
        Get image path from mysql images are stored on NFS mount 
        images will randomized from a list of paths held in a DB table
    '''

        # Connect to the database
    conn = connection = pymysql.connect(host='10.8.29.11',
                                 user='root',
                                 password='cisco123',
                                 db='images',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    cur = conn.cursor()

    random_number = randint(1,15)
    #print (random_number)

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT *  FROM imagestable where id = %d " % (random_number)
        #sql = "SELECT *  FROM imagestable where id = 3"
        cursor.execute(sql)
        result = cursor.fetchone()
        imagelocation = (result.get('imagefile'))

        #os.system('open {}'.format(imagelocation))

    #print('you are here!!!!!', imagelocation)

    
    return imagelocation


@app.route('/')
def main_page():
    return render_template("index.html")

@app.route('/randomimage', methods=['POST'])
def randomize_image():

    print('You are here!!')
    payload = request.form
    print(payload)

    action = payload['action']
    if action == "start-ranimage":
        #image_path = "//path_to_image"
        image_path = get_image_from_db()
    else:
        print('Hell Fire!')

    print(image_path)

    returnmessage =  {'message' : image_path}
    	

    print (returnmessage)
    resp = json.dumps(returnmessage)
    return Response(resp, status=200, mimetype='application/json')


app.run(host='10.8.253.109', port=8082)

