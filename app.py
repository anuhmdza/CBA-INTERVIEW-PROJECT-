from flask import Flask, request, jsonify
import mysql.connector
import pandas as pd

app = Flask(__name__)

# Helper function to query the database
def run_query(query, params=None):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='coconuts',
        database='StoreData'
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query, params or ())
    if query.strip().lower().startswith("select"):
        result = cursor.fetchall()
    else:
        conn.commit()
        result = {"message": "Query executed successfully"}
    cursor.close()
    conn.close()
    return result

# GET endpoint - return JSON, list, and DataFrame
@app.route('/sales', methods=['GET'])
def get_sales():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    if not start_date or not end_date:
        return jsonify({"error": "Please provide start_date and end_date as query parameters."}), 400

    query = """
        SELECT * FROM Sales
        WHERE date BETWEEN %s AND %s
    """
    result = run_query(query, (start_date, end_date))

    if not result:
        return jsonify({'message': 'No records found'}), 404

    data_list = [dict(row) for row in result]
    df = pd.DataFrame(result)
    return jsonify({
        'json': result,
        'list': data_list,
        'dataframe': df.to_dict(orient='records')
    })

# POST endpoint - insert new sales row
@app.route('/sales', methods=['POST'])
def add_sale():
    data = request.get_json()
    required_fields = ['id', 'store_id', 'total_sales', 'date']

    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields."}), 400

    query = """
        INSERT INTO Sales (id, store_id, total_sales, date)
        VALUES (%s, %s, %s, %s)
    """
    try:
        run_query(query, (data['id'], data['store_id'], data['total_sales'], data['date']))
        return jsonify({"message": "New sale record added successfully"}), 201
    except mysql.connector.IntegrityError:
        return jsonify({"error": "A record with this ID already exists."}), 409

if __name__ == '__main__':
    app.run(debug=True)
