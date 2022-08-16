import proxlist
from proxy_checking import ProxyChecker

checker = ProxyChecker()

proxies = proxlist.list_proxies()

valid_proxies = []

while True:
    for a in proxies:
        checking = checker.check_proxy(a)
	if checking['status'] == True:
	    valid_proxies.append(a)
	else:
	    continue
	
