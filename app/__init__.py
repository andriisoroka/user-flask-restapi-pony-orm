from flask import Flask
from flask.ext.restful import Api
from pony import orm
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)

api = Api(app)
db = orm.Database()
db.bind('sqlite', 'test_db.sqlite',create_db=True)
from app.models.user import User
orm.sql_debug(True)
db.generate_mapping(create_tables=True)


from app.views import app
