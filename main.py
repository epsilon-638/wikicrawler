import proxy

if __name__=="__main__":
	proxy_list = proxy.ProxyList().fetch_proxies()
	proxy_list.return_proxies()
