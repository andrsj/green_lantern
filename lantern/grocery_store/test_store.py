import inject
import pytest
from store_app import app
from fake_storage import FakeStorage


def configure_test(binder):
    db = FakeStorage()
    binder.bind('DB', db)


class Initializer:
    def setup(self):
        inject.clear_and_configure(configure_test)

        app.config['TESTING'] = True
        with app.test_client() as client:
            self.client = client


class TestUsers(Initializer):
    def initial_data(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        return resp

    def test_create_new_user(self):
        resp = self.initial_data()
        assert resp.status_code == 201
        assert resp.json == {'user_id': 1}

        resp = self.client.post(
            '/users',
            json={'name': 'Andrew Derkach'}
        )
        assert resp.json == {'user_id': 2}

    def test_successful_get_user(self):
        resp = self.initial_data()
        user_id = resp.json['user_id']
        resp = self.client.get(f'/user/{user_id}')
        assert resp.status_code == 200
        assert resp.json == {'name': 'John Doe'}

    def test_get_unexistent_user(self):
        resp = self.client.get(f'/user/1')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 1'}

    def test_successful_update_user(self):
        resp = self.initial_data()
        user_id = resp.json['user_id']

        resp = self.client.put(
            f'/user/{user_id}',
            json={'name': 'Johanna Doe'}
        )
        assert resp.status_code == 200
        assert resp.json == {'status': 'success'}

    def test_update_unexistent_user(self):
        resp = self.client.put(f'/user/1')
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 1'}


class TestGoods(Initializer):
    def initial_data(self):
        resp = self.client.post(
            '/goods',
            json=[
                {
                    'name': 'Chockolate bar',
                    'price': 10
                },
                {
                    'name': 'Banana',
                    'price': 20
                }
            ]
        )
        return resp

    def test_create_new_many_goods(self):
        resp = self.initial_data()
        assert resp.status_code == 201
        assert resp.json == {'number of items created': 2}

    def test_create_new_one_good(self):
        resp = self.client.post(
            '/goods',
            json=[
                {
                    'name': 'Chockolate bar',
                    'price': 10
                }
            ]
        )
        assert resp.status_code == 201
        assert resp.json == {'number of items created': 1}

    def test_get_all_goods(self):
        data = [
            {
                'name': 'Chockolate bar',
                'price': 10
            },
            {
                'name': 'Banana',
                'price': 20
            }
        ]
        resp = self.client.post(
            '/goods',
            json=data
        )
        count_of_goods = resp.json['number of items created']
        resp = self.client.get('/goods')
        assert resp.status_code == 200
        assert len(resp.json) == count_of_goods
        excepted_data = [
            {
                'id': id_good,
                'name': good['name'],
                'price': good['price']
            }
            for id_good, good in enumerate(data, start=1)
        ]
        assert resp.json == excepted_data

    def get_unexisted_goods(self):
        resp = self.client.get('/goods')
        assert resp.status_code == 200
        assert len(resp.json) == 0
        assert resp.json == []

    def test_update_many_goods(self):
        self.initial_data()
        resp = self.client.put(
            '/goods',
            json=[
                {
                    'id': 1,
                    'name': 'Apple',
                    'price': 100
                },
                {
                    'id': 2,
                    'name': 'Cookies',
                    'price': 200
                }
            ]
        )
        assert resp.status_code == 200
        assert resp.json == {'successfully_updated': 2}

    def test_update_with_error_id(self):
        self.initial_data()
        resp = self.client.put(
            '/goods',
            json=[
                {
                    'id': 2,
                    'name': 'Apple',
                    'price': 100
                },
                {
                    'id': 3,
                    'name': 'Cookies',
                    'price': 200
                }
            ]
        )
        assert resp.status_code == 200
        assert resp.json == {
            'successfully_updated': 1,
            'errors': {
                'no such id in goods': [3]
            }
        }


class TestStores(Initializer):
    def initial_user_data(self):
        resp = self.client.post(
            '/users',
            json={'name': 'John Doe'}
        )
        return resp

    def initial_store_data(self, user_id):
        resp = self.client.post(
            '/store',
            json={'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': user_id}
        )
        return resp

    def test_create_new_store(self):
        resp = self.initial_user_data()
        user_id = resp.json['user_id']
        resp = self.initial_store_data(user_id)
        assert resp.status_code == 201
        assert resp.json == {'store_id': 1}

    def test_create_new_store_with_wrong_manager(self):
        self.initial_user_data()
        resp = self.initial_store_data(user_id=2)
        assert resp.status_code == 404
        assert resp.json == {'error': 'No such user_id 2'}

    def test_get_store_by_id(self):
        resp = self.initial_user_data()
        user_id = resp.json['user_id']
        self.initial_store_data(user_id)
        resp = self.client.get(f'/store/{user_id}')
        assert resp.status_code == 200
        assert resp.json == {'name': 'Mad Cow', 'location': 'Lviv', 'manager_id': user_id}

    def test_get_store_by_wrong_id(self):
        resp = self.initial_user_data()
        user_id = resp.json['user_id']
        self.initial_store_data(user_id)
        resp = self.client.get(f'/store/{user_id + 1}')
        assert resp.status_code == 404
        assert resp.json == {'error': f'No such store_id {user_id + 1}'}

    def test_update_store(self):
        resp = self.initial_user_data()
        user_id = resp.json['user_id']
        self.initial_store_data(user_id)
        resp = self.client.put(
            f'/store/{user_id}',
            json={'name': 'Peperoni', 'location': 'Lviv', 'manager_id': user_id}
        )
        assert resp.status_code == 200
        assert resp.json == {'status': 'success'}

    def test_update_store_with_wrond_id(self):
        resp = self.initial_user_data()
        user_id = resp.json['user_id']
        resp = self.client.put(
            '/store/1',
            json={'name': 'Peperoni', 'location': 'Lviv', 'manager_id': user_id}
        )
        assert resp.status_code == 404
        assert resp.json == {'error': f'No such store_id {user_id}'}

    def test_update_store_with_wrong_manager_id(self):
        resp = self.initial_user_data()
        user_id = resp.json['user_id']
        self.initial_store_data(user_id)
        resp = self.client.put(
            f'/store/{user_id}',
            json={'name': 'Peperoni', 'location': 'Lviv', 'manager_id': user_id + 1}
        )
        assert resp.status_code == 404
        assert resp.json == {'error': f'No such user_id {user_id + 1}'}
