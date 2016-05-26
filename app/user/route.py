from flask.ext.restful import Resource
from flask import request
import time
import json
from app.models.user import User
from app import orm,db
from app.libs.jsonapi import JSONAPI
class Users(Resource):
	def get(self):
		time.sleep(5)
		with orm.db_session:
			users = User.select()
			return {"data":JSONAPI.parse(User,[item.to_dict() for item in users])}		

	def post(self):
		info = json.loads(request.data)
		parse = info['data']
		try:
			with orm.db_session:
				User(
					name=parse['attributes']['name'],
					email=parse['attributes']['email'],
					position=parse['attributes']['position'],
					age=parse['attributes']['age'],
				)
				return info
		except Exception as e:
			return 400

class UserItem(Resource):
	
	def get(self,id):	
		with orm.db_session:
			res = User.get(id = int(id))
			if res:
				return {"data":JSONAPI.parse(User,[res.to_dict()])[0]}
			else:
				return {"data":None}

		

	def patch(self,id):
		info = json.loads(request.data)
		parse = info['data']
		print(parse)
		with orm.db_session:
			user = User[int(id)]
			user.set(
				name=parse['attributes']['name'],
				email=parse['attributes']['email'],
				position=parse['attributes']['position'],
				age=parse['attributes']['age']
			)
		return info

	def delete(self,id):
		with orm.db_session:
			res = User[int(id)].delete()
			return {"errors":[{}],"meta":{},"data":[{
				"type":'user'
			}]}, 204
		return {"errors":[],"meta":{},"data":{}}