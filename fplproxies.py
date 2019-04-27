'''fplproxies.py

python3 fplproxies.py > proxies.txt

scrapes 600 http(s) proxies to ip:port

https://free-proxy-list.net 300
https://www.us-proxy.org 200
https://www.sslproxies.org 100

now async! like half a second faster! wow!'''

from requests_html import AsyncHTMLSession

a = AsyncHTMLSession()  # session appears to be currently required for a single get request with this library?

async def 一(): return await a.get('https://free-proxy-list.net')

async def 二(): return await a.get('https://www.us-proxy.org')

async def 三(): return await a.get('https://www.sslproxies.org')

results = a.run(一, 二, 三)

for result in results:

	cells = result.html.find('td')

	p = ''  # string as data stream for proxies

	for cell in cells:

		c = cell.text 

		if not c.lower().islower():  # lowercase all letters and then check if islower to determine if the cell contains letters (only ip and port cells will remain)
			
			if '.' in c:

				c = '\n' + c + ':'  # ip will have "." then add newline in front of ip to separate proxies \nip:port\nip:port 
			
			p += c  # string together 

	print(p)
