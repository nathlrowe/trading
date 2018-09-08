# Position class

from itertools import count

class Position:

	id_generator = count()

	def __init__(self, account):
		self.id = Position.id_generator.__next__()
		