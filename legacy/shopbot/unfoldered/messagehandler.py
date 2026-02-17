from output import send
from user import User
from modules import modules

def starthandler(id):
	user = User(id)
	send(id, 'usermade'+str(user))

def handle(id, message):
	commands = ['/start']
	methods = {'/start': starthandler, '/product':None, '/buy':None}
	if 'supersingleproduct' in modules:
		def product(id):
			send(id, 'product description')
		def buy(id):
			send(id, 'bought the product')
		commands.append('/product')
		commands.append('/buy')
		methods['/product']= product
		methods['/buy']= buy
	
	
	if message in commands:
		methods[message](id)
		