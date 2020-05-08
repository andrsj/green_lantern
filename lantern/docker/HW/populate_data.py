import csv


def get_users():
    with open('app/users.csv', 'r') as f:
        reader = csv.DictReader(f)
        users = [i for i in reader]
    return users


def get_goods():
    with open('app/goods.csv', 'r') as f:
        reader = csv.DictReader(f)
        goods = [good for good in reader]
    return goods


def get_stores():
    with open('app/stores.csv', 'r') as f:
        reader = csv.DictReader(f)
        stores = [store for store in reader]
    return stores