from flask import Blueprint, render_template
from grocery_store.models import Good
from flask_login import current_user, login_required

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user.name, email=current_user.email)


@main.route('/goods-page')
def goods_list():
    return render_template('goods.html', goods=Good.query.all())
