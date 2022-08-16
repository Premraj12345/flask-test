import proxlist
from proxy_checking import ProxyChecker
from time import sleep

checker = ProxyChecker()

proxies = proxlist.list_proxies()

valid_proxies = []
valid_proxies2 = []

while True:
    for a in proxies:
        checking = checker.check_proxy(a)
	if checking['status'] == True:
	    valid_proxies.append(a)
	else:
	    continue
    sleep(100)
    valid_proxies2 = valid_proxies
    valid_proxies.clear()
    
