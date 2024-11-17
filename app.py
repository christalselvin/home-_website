from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api_login", methods=["POST"])
def home():
    if request.method == 'POST':
        try:
            data = request.json
            user_name = data['user_name']
            password = data['password']

            # Simulated database check for demonstration purposes
            # Replace this with your actual database query
            if user_name == "admin" and password == "password123":
                return jsonify({'message': 'Login successful'}), 200
            else:
                return jsonify({'error': 'Invalid username or password'}), 401

        except KeyError:
            return jsonify({'error': 'Missing required fields in request'}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0")

