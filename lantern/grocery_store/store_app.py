from flask import Flask, jsonify, request

import inject


app = Flask(__name__)


@app.route('/users', methods=['POST'])
def create_user():
    db = inject.instance('DB')
    user_id = db.users.add(request.json)
    return jsonify({'user_id': 1})
