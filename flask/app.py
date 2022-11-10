import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)


def getDB():
    return psycopg2.connect(host='172.17.0.2', database='db', user='postgres', password='mysecretpassword', port=5432)


@app.route('/')
def index():
    return '<h3>flask works</h3>'


@app.route('/cars', methods=['GET'])
def getCars():
    db = getDB()
    year = request.args.get('year')

    if year is None:
        query = "SELECT * FROM Car"
    else:
        query = "SELECT * FROM Car WHERE year = " + year

    cur = db.cursor()
    cur.execute(query)
    output_json = cur.fetchall()
    db.close()

    return jsonify(output_json)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
