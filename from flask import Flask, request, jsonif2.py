from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def returnUserInfo():
    user_id = request.args.get("id")
    users = {
        1: {"name": "Alex", "age": 25},
        2: {"name": "Max", "age": 28},
        3: {"name": "Egor", "age": 15}
    }
    
    if user_id is not None:
        try:
            user_id = int(user_id)
            user = users.get(user_id)
            if user:
                return jsonify(user), 200
        except ValueError:
            pass
    
    return jsonify(users), 200

if __name__ == "__main__":
    app.run(debug=True)