import proxy

ports = ["8080", "80"]

proxy_list = proxy.ProxyList(https=False, ports=ports)
proxy_list.fetch_proxies()
proxy_list.return_proxies()

content = proxy_list.get("https://google.com")
print(content)
