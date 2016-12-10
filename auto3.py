from urllib.request import Request, urlopen
import time

def move( move, heading ) :
	values = """
	{
		"move": """+move+""",
		"heading": """+str(heading)+"""
	}
	"""
	binary_data = values.encode('ascii')
	headers = {
	'Content-Type': 'application/json'
	}
	request = Request('http://hackdbz.win/api/993afc24119206d7c9b61ca0cf1b51a3/control', data=binary_data, headers=headers)

	response_body = urlopen(request).read()


def radar() :

	request = Request('http://hackdbz.win/api/993afc24119206d7c9b61ca0cf1b51a3/radar')
	response_body = urlopen(request).read().decode('ascii')
	closest = response_body[-5:]
	import re
	closest_num = int(re.sub("[^0-9]", "", closest))
	closest_num = closest_num
	print(closest_num)
	return(closest_num)
	
movimento = 'false'
ultimo_movimento = 0
x = 0
while radar() > 0:
	ultimo_movimento = radar()
	move ( 'true', x )
	
	while movimento == 'false':
		radar()
		if ultimo_movimento >= radar():
			ultimo_movimento = radar()
			continue
		else :
			
			move ( 'false', x )
			movimento = 'false'
			x = x+45
			break
	continue
