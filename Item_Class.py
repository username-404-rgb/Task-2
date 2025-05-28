class Item:
	def __init__(self, name, collected):
		self.name = name
		self.collected = collected

	def get_collected(self):
		return self.collected

	def set_collected(self, new_name):
		if isinstance(new_name, str):
			self.collected = new_name
		else:
			raise ValueError("Name must be a string.")


