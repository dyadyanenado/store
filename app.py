from flask import Flask
from flask import render_template
from sqlalchemy import select
from .core.database import session_maker
from .models.product import Product

app = Flask(__name__)


@app.route('/')
def index():
    with session_maker() as db_session:
        products = db_session.scalars(select(Product))
        return render_template('index.html', products=products)
