from flask import Blueprint, render_template
from grocery_store.database import db
from flask_login import current_user, login_required

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template(
        'profile.html', 
        user=current_user.name, 
        email=current_user.email
    )

@main.route('/orders')
@login_required
def orders():
    orders_list = []
    for order in current_user.orders:
        order_data = (
            order.store.name,
            order.created_time,
            sum([good.good.price for good in order.order_lines]),
            {good.good.name: good.good.price for good in order.order_lines}
        )
        orders_list.append(order_data)
    return render_template('orders.html', orders=orders_list)
