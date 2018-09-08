# Account class

# TODO: centralize the relationship between symbols and currencies
# i.e. put functions which convert symbols to currencies and vice versa somewhere

from itertools import count

class Account:

	id_generator = count()

	def __init__(self, exchange_id, info):
		self.id = Account.id_generator.__next__()

		self.exchange_id = exchange_id
		self.ccxt_exchange = None
		self.symbols = []
		self.balance = dict()

		self.user_id = info.get("user_id", None)
		self.api_key = info.get("api_key", None)
		self.secret = info.get("secret", None)

		self.init_symbols = info.get("symbols", [])

		self.simulate_balance = info.get("simulate_balance", False)
		self.init_balance = info.get("init_balance", 0)
		self.init_balance_dict = info.get("init_balance_dict", dict())

	def add_symbol(self, symbol):
		# TODO: log a warning in the case of adding a symbol that already exists
		if not self.has_symbol(symbol):
			self.symbols.append(symbol)
			(base, quote) = tuple(symbol.split("/"))
			self.add_currency(base)
			self.add_currency(quote)

	def add_currency(self, currency):
		pass

	# TODO: possibly add these methods:
	# account.add_credentials(user_id = None, api_key = None, secret = None)

	# --------------------------------------------------------------------------

	def update_balance(self):
		pass

	# --------------------------------------------------------------------------

	def iter_symbols(self):
		for symbol in self.symbols:
			yield symbol

	def iter_currencies(self):
		for currency in self.balance:
			yield currency

	# --------------------------------------------------------------------------

	def get_id(self):
		return self.id

	def get_exchange_id(self):
		return self.exchange_id

	def get_ccxt_exchange(self):
		return self.ccxt_exchange

	def get_balance(self, currency, update=False):
		if update:
			self.update_balance()
		if currency not in self.balance:
			raise KeyError("Invalid currency: {}".format(currency))
		return self.balance[currency]

	def get_base_balance(self, symbol, update=False):
		currency = symbol.split("/")[0]
		return self.get_balance(currency, update)

	def get_quote_balance(self, symbol, update=False):
		currency = symbol.split("/")[1]
		return self.get_balance(currency, update)

	# --------------------------------------------------------------------------

	def has_symbol(self, symbol):
		return symbol in self.symbols
