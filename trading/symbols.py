# Symbols library functions

def get_asset(symbol):
	return symbol.split("/")[0]

def get_quote(symbol):
	return symbol.split("/")[1]

def get_currencies(symbol):
	return tuple(symbol.split("/"))
	# TODO: I believe split returns a list

def get_symbol(asset, quote):
	return "{0}/{1}".format(asset, quote)
