from app import app,api
from app.user.route import Users,UserItem


@app.route('/')
def index():
	return 'Simple example flask app'


api.add_resource(Users, '/api/users/')
api.add_resource(UserItem,'/api/users/<int:id>')