# app.py for testing

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for time tracking
time_entries = {}

@app.route('/add-time', methods=['POST'])
def add_time():
    data = request.get_json()
    date = data.get('date')
    time_spent = data.get('time_spent')

    if not date or not time_spent:
        return jsonify({"error": "Invalid input. 'date' and 'time_spent' are required."}), 400

    if date not in time_entries:
        time_entries[date] = 0

    time_entries[date] += time_spent
    return jsonify({"message": "Time entry added successfully.", "date": date, "total_time": time_entries[date]}), 200

@app.route('/get-time', methods=['GET'])
def get_time():
    return jsonify(time_entries), 200

if __name__ == '__main__':
    app.run(debug=True)