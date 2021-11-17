import proxy

if __name__=="__main__":
	proxy_list = proxy.ProxyList()
    proxy_list.fetch_proxies()
	proxy_list.return_proxies()
