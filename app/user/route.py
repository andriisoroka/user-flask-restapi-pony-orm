from flask.ext.restful import Resource
from flask import request
import json
from app.models.user import User
from app import orm,db
from app.libs.jsonapi import JSONAPI
class Users(Resource):
	def get(self):
		with orm.db_session:
			users = User.select()
			return {"data":JSONAPI.parse(User,[item.to_dict() for item in users])}		

	def post(self):
		info = json.loads(request.data)
		parse = info['data']
		with orm.db_session:
			User(
				name=parse['attributes']['name'],
				email=parse['attributes']['email'],
				position=parse['attributes']['position'],
				age=parse['attributes']['age'],
			)
			return info
		return {"status":False}

class UserItem(Resource):
	
	def get(self,id):	
		with orm.db_session:
			res = User.get(id = int(id))
			if res:
				return {"data":JSONAPI.parse(User,[res.to_dict()])}
			else:
				return {"data":[]}
			#User(name="Max Shnaile",email="max@gmail.com",position="senior developer",age=28)
			#User(name="Silvia Luchia",email="silvia@gmail.com",position="UX designer",age=25)
			#res = db.select('SELECT * FROM user')
			#print(res)

		

	def put(self,id):
		pass

	def delete(self,id):
		pass