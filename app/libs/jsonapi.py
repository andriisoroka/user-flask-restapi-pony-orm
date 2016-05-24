class JSONAPI:

	@staticmethod
	def parse(cls,data):
		result = [];
		for item in data:
			temp = {
				"id":item['id'],
				"type":cls._type,
				"attributes":{key:item[key] for key in cls._fields}
			}
			result.append(temp)
		return result