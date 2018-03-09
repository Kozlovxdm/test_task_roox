from flask import Flask, jsonify
from flask_restful import reqparse
import psycopg2
from psycopg2.extras import DictCursor



app = Flask(__name__)
parser = reqparse.RequestParser()
parser.add_argument('id', type=int)

@app.route("/user")
def get_user():
    args = parser.parse_args()
    _id = args.get('id')
    if not _id:
        return ("Id is required"), 400
    
    try:
        conn = psycopg2.connect(dbname="dimon", user="dimon", password="dimon", host="localhost")
        cur = conn.cursor(cursor_factory=DictCursor)
        cur.execute("SELECT name, second_name, surname from users where id = %s" % _id)
        result = cur.fetchone()
        if result:
            return jsonify(dict(result)), 200
        else:
            return "Not found", 404
    except Exception as e:
        return jsonify(e), 400
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
