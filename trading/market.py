# Market class 

import ccxt
from itertools import count

class Market:

	def __init__(self, exchange_id, symbol):
		self.exchange_id = exchange_id
		self.symbol = symbol

	# --------------------------------------------------------------------------

	def get_id(self):
		return (self.get_exchange_id(), self.get_symbol())

	def get_exchange_id(self):
		return self.exchange_id

	def get_symbol(self):
		return self.symbol
