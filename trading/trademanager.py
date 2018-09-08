# Trade manager class

from trading.account import Account

class TradeManager:

	def __init__(self):
		self.accounts = dict()
		self.markets = dict()
		self.positions = dict()

		self.exchange_ids = []
		self.symbols = []
		self.ccxt_exchanges = dict()

	# add an account to the manager
	def add_account(self, exchange_id, account_info):
		account = Account(exchange_id, account_info)
		account_id = account.get_id()
		self.accounts[account_id] = account

		for symbol in account.iter_symbols():
			self.add_market(exchange_id, symbol)

		return account_id

	# safely remove an account from the manager (TODO)
	def remove_account(self, account_id):
		pass

	# add a market to the manager
	def add_market(self, exchange_id, symbol):
		market = Market(exchange_id, symbol)
		market_id = market.get_id()

		# overwrite current market instance
		if market_id in self.markets:
			self.remove_market(market_id)
		self.markets[market_id] = market

		# ensure exchange ID and symbol are in lists
		if exchange_id not in self.exchange_ids:
			self.exchange_ids.append(exchange_id)
		if symbol not in self.symbols:
			self.symbols.append(symbol)

		return market_id

	# safely remove a market from the manager
	def remove_market(self, market_id):
		if market_id not in self.markets:
			return
		market = self.get_market(market_id)
		del market
		del self.markets[market_id]

	# --------------------------------------------------------------------------

	def iter_exchanges(self):
		for i in self.exchange_ids.items():
			yield i

	def iter_accounts(self, exchange_id = None):
		for i, account in self.accounts.items():
			if exchange_id is not None and account.get_exchange_id() != exchange_id: continue
			yield i

	def iter_symbols(self, account_id = None):
		for symbol in self.symbols:
			#if exchange_id is not None and account.get_exchange_id() != exchange_id: continue
			yield symbol

	def iter_markets(self, exchange_id = None, account_id = None):
		for i, market in self.markets.items():
			if exchange_id is not None and market.get_exchange_id() != exchange_id: continue
			if account_id is not None and not self.account_has_market(account_id, i): continue
			yield i

	def iter_positions(self, exchange_id = None, account_id = None, symbol = None, status = None):
		for i, position in self.positions.items():
			yield i

	def iter_account_symbols(self):
		for i, account in self.accounts.items():
			for symbol in account.iter_symbols():
				yield i, symbol

	# --------------------------------------------------------------------------

	def get_account(self, account_id):
		if account_id not in self.accounts:
			raise KeyError("Invalid account id: {}".format(account_id))
		return self.accounts[account_id]

	def get_position(self, position_id):
		if position_id not in self.positions:
			raise KeyError("Invalid position id: {}".format(position_id))
		return self.positions[position_id]

	def get_market(self, market_id):
		if market_id not in self.markets:
			raise KeyError("Invalid market id: {}".format(market_id))
		return self.markets[market_id]

	def get_ccxt_exchange(self, exchange_id):
		if exchange_id not in self.ccxt_exchanges:
			raise KeyError("Invalid CCXT exchange instance id: {}".format(exchange_id))
		return self.ccxt_exchanges[exchange_id]

	# --------------------------------------------------------------------------

	def has_exchange(self, exchange_id):
		return exchange_id in self.exchange_ids

	def account_has_market(self, account_id, market_id):
		account = self.get_account(account_id)
		market = self.get_market(market_id)
		return account.get_exchange_id() == market.get_exchange_id() and account.has_symbol(market.get_symbol())
