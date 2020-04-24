from itertools import count
from store_app import NoSuchUserError, NoSuchStoreError


class FakeStorage:
    def __init__(self):
        self._users = FakeUsers()
        self._goods = FakeGoods()
        self._stores = FakeStores()

    @property
    def users(self):
        return self._users

    @property
    def goods(self):
        return self._goods

    @property
    def stores(self):
        return self._stores


class FakeUsers:
    def __init__(self):
        self._users = {}
        self._id_counter = count(1)

    def add(self, user: dict):
        user_id = next(self._id_counter)
        self._users[user_id] = user
        return user_id

    def get_user_by_id(self, user_id: int):
        try:
            return self._users[user_id]
        except KeyError:
            raise NoSuchUserError(user_id)

    def update_user_by_id(self, user_id: int, user: dict):
        if user_id in self._users:
            self._users[user_id] = user
        else:
            raise NoSuchUserError(user_id)


class FakeGoods:
    def __init__(self):
        self._goods = {}
        self._id_counter = count(1)

    def add(self, goods: list):
        for good in goods:
            good_id = next(self._id_counter)
            good['id'] = good_id
            self._goods[good['id']] = good
        return len(goods)

    def get_all_goods(self):
        return [self._goods[good] for good in self._goods]

    def update_goods(self, new_goods: list):
        success_counter = 0
        errors_id = []
        for good in new_goods:
            if good['id'] in self._goods:
                success_counter += 1
                self._goods[good['id']] = good
            else:
                errors_id.append(good['id'])
        return success_counter, errors_id


class FakeStores:
    def __init__(self):
        self._stores = {}
        self._id_counter = count(1)

    def add(self, store: dict):
        store_id = next(self._id_counter)
        self._stores[store_id] = store
        return store_id

    def get_store_by_id(self, store_id: int):
        try:
            return self._stores[store_id]
        except KeyError:
            raise NoSuchStoreError(store_id)

    def update_store_by_id(self, store_id: int, store: dict):
        if store_id in self._stores:
            self._stores[store_id] = store
        else:
            raise NoSuchStoreError(store_id)
