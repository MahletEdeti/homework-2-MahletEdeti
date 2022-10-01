import mysql.connector
from mysql.connector import Error
import flask
from sql import create_connection
from sql import execute_query
from sql import execute_read_query
from flask import jsonify
from flask import request
import creds

app = flask.Flask(__name__)  # sets up the application
app.config["DEBUG"] = True  # allow to show errors in browser

myCreds = creds.Creds()
conn = create_connection(myCreds.constring, myCreds.username, myCreds.password, myCreds.dbName)


@app.route('/api/gem', methods=['GET'])
def get_gem():
    sql = "SELECT * FROM gem"
    users = execute_read_query(conn, sql)
    return users


@app.route('/api/gem', methods=['POST'])
def post_gem():
    request_data = request.get_json()
    newtype = request_data['gemtype']
    newcolor = request_data['gemcolor']
    newcarat = request_data['carat']
    newprice = request_data['price']
    sql = "INSERT INTO gem(gemtype, gemcolor, carat, price) VALUES ('%s','%s',%s,%s)" % (
    newtype, newcolor, newcarat, newprice)
    execute_query(conn, sql)
    return "added sucessfully"


@app.route('/api/gem', methods=['PUT'])
def put_gem():
    id = int(request.args['id'])
    request_data = request.get_json()
    newtype = request_data['gemtype']
    newcolor = request_data['gemcolor']
    newcarat = request_data['carat']
    newprice = request_data['price']
    sql = "UPDATE gem SET gemtype = '%s', gemcolor = '%s', carat = %s, price = %s WHERE id = %s" % (
    newtype, newcolor, newcarat, newprice, id)
    execute_query(conn, sql)
    return "updated sucessfully"


@app.route('/api/gem', methods=['DELETE'])
def delete_gem():
    id = int(request.args['id'])
    sql = "DELETE FROM gem WHERE id = %s" % (id)
    execute_query(conn, sql)
    return "Delete request successful"


app.run()

