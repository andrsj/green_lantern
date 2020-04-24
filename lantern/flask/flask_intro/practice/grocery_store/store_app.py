import inject

from flask import Flask, jsonify, request


class NoSuchUserError(Exception):
    def __init__(self, user_id):
        self.message = f'No such user_id {user_id}'


class NoSuchStoreError(Exception):
    def __init__(self, store_id):
        self.message = f'No such store_id {store_id}'


app = Flask(__name__)


# I dont use Blueprint for nice format structure of project, because it was studied in the next lecture
# Sorry for this view, i know it bad way programming style code

@app.errorhandler(NoSuchUserError)
def error_handler_for_user(e):
    return jsonify({'error': e.message}), 404


@app.errorhandler(NoSuchStoreError)
def error_handler_for_store(e):
    return jsonify({'error': e.message}), 404


@app.route('/users', methods=['POST'])
def create_user():
    db = inject.instance('DB')
    user_id = db.users.add(request.json)
    return jsonify({'user_id': user_id}), 201


@app.route('/user/<int:user_id>')
def get_user(user_id):
    db = inject.instance('DB')
    user = db.users.get_user_by_id(user_id)
    return jsonify(user)


@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    db = inject.instance('DB')
    db.users.update_user_by_id(user_id, request.json)
    return jsonify({'status': 'success'})


@app.route('/goods', methods=['POST'])
def create_goods():
    db = inject.instance('DB')
    count_of_goods_created = db.goods.add(request.json)
    return jsonify({'number of items created': count_of_goods_created}), 201


@app.route('/goods')
def get_goods():
    db = inject.instance('DB')
    goods = db.goods.get_all_goods()
    return jsonify(goods)


@app.route('/goods', methods=['PUT'])
def update_goods():
    db = inject.instance('DB')
    count_of_updated_goods, error_id_unsuccesfull_update = db.goods.update_goods(request.json)
    # I think we need to do custom error for this, but nothing was said about it in the task
    # For pretty view JSON i split the error
    if error_id_unsuccesfull_update:
        return jsonify(
            {
                'successfully_updated': count_of_updated_goods,
                'errors': {
                    'no such id in goods': error_id_unsuccesfull_update
                }
            }
        )
    else:
        return jsonify({'successfully_updated': count_of_updated_goods})


@app.route('/store', methods=['POST'])
def create_new_store():
    db = inject.instance('DB')
    # Checking the user for availability for raise NoSuchUserError
    db.users.get_user_by_id(request.json['manager_id'])
    store_id = db.stores.add(request.json)
    return jsonify({'store_id': store_id}), 201


@app.route('/store/<int:store_id>')
def get_store(store_id):
    db = inject.instance('DB')
    store = db.stores.get_store_by_id(store_id)
    return jsonify(store)


@app.route('/store/<int:store_id>', methods=['PUT'])
def update_store(store_id):
    db = inject.instance('DB')
    # Checking the user for availability for raise NoSuchUserError
    db.users.get_user_by_id(request.json['manager_id'])
    db.stores.update_store_by_id(store_id, request.json)
    return jsonify({'status': 'success'})
