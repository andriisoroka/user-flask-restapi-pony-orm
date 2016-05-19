from flask.ext.restful import Resource
from app.models.user import User
from app import orm,db

class Users(Resource):
	def get(self):
		with orm.db_session:
			users = [{"id":item.id,"name":item.name} for item in User.select()]
			return {"data":users}		

	def post(self):
		return {"name":"post"}

class UserItem(Resource):
	
	def get(self,id):
			
		with orm.db_session:
			#User(name="Uliana Soroka",email="starosta_7@mail.ru",position="senior developer",age=28)
			#res = db.select('SELECT * FROM user')
			#print(res)
			for user in User.select():
				print(user.name)

		return {"name":'test single %s'%(id)}

	def put(self,id):
		pass

	def delete(self,id):
		pass