from connection import request

# Example Request
# request(action="/orderBook/L2",method="GET",params={"symbol":"XBT"})

# Executions
def get_execution():
	pass
def get_execution_tradeHistory():
	pass

# Instruments
def get_instrument_active():
	pass

# Orders
def get_orders():
	pass
def change_order():
	pass
def new_order():
	pass
def delete_orders():
	pass

# Orderbook
def get_orderbook(session, symbol="XBT",depth=1):
	return request(session=session, action="/orderBook/L2",method="GET",params={"symbol":symbol,"depth":depth})

# Account Positions
def get_positions():
	pass

# Quotes
def get_quotes():
	pass
def get_quotes_bucketed():
	pass

# Exchange Statistics
def get_stats():
	pass
def get_stats_history():
	pass

# Account Trades
def get_trades():
	pass
def get_trades_bucketed():
	pass

# User Data
def get_user():
	pass
def get_wallet():
	pass
def get_wallet_history():
	pass
def get_wallet_summary():
	pass
def get_margin():
	pass