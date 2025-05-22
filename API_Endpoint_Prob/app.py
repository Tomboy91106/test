from flask import Flask, request, jsonify
from db_config import get_connection

app = Flask(__name__)

@app.route('/reminders', methods=['POST'])
def create_reminder():
    data = request.get_json()

    required_fields = ['message', 'date', 'time', 'reminder_type']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing fields'}), 400

    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        insert_query = """
            INSERT INTO reminders (message, date, time, reminder_type)
            VALUES (%s, %s, %s, %s)
        """
        values = (
            data['message'],
            data['date'],
            data['time'],
            data['reminder_type']
        )
        cursor.execute(insert_query, values)
        conn.commit()

        return jsonify({'message': 'Reminder saved!', 'id': cursor.lastrowid}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

if __name__ == '__main__':
    app.run(debug=True)
