import psycopg2
from flask import Flask , jsonify , request

app = Flask(__name__)   


hostname = 'localhost'
database  = 'test_erp'
username = 'postgres'
pwd = 'cupersell'
port_id = 5432
# conn = None
# cur = None

def get_db_connection():
    conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd,
            port = port_id
            )
    return conn

@app.route('/product_id/<id>' , methods = ['GET'])
def get_data_by_id(id):
    try:
        conn = get_db_connection ()
        cur = conn.cursor()
        cur.execute( '''select sum(quantity) from order_details
                            where product_id  =  %s;''',(id,))
        row = cur.fetchall()
        if row is None:
            return jsonify({'error':'data not found'}), 404
        data = {
            'id': row[0]
            #  'name' : row[1]
            # 'conname': row[2]
        }
        
        cur.close()
        conn.close()

        return jsonify(data)
    except Exception as e:
        return jsonify({'error' : str(e)}) , 500
if __name__ == '__main__':
    app.run(debug=True , port=4700)


