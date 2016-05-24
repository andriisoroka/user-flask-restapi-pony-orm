from app import db,orm

class User(db.Entity):
	
	_type="user"
	_fields = ['name','email','position','age']

	name = orm.Required(str)
	email = orm.Required(str)
	position = orm.Required(str)
	age = orm.Required(int)

