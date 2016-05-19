from app import db,orm

class User(db.Entity):
	name = orm.Required(str)
	email = orm.Required(str)
	position = orm.Required(str)
	age = orm.Required(int)