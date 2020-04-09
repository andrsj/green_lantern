from itertools import count

class FakeStorage:
    def __init__(self):
        self._users = FakeUsers()

    @property
    def users(self):
        return self._users

class FakeUsers:
    def __init__(self):
        self._users = {}
        self._id_counter = count()

    def add(self, user):
        user_id = next(self._id_counter)
        self._users[user_id] = user
        return user_id
