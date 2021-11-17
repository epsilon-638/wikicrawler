# WikiCrawler
---
### Reimplementation of a weekend project from 2 years ago
## ProxyList
```python3
import proxy

proxy_list = proxy.ProxyList()
proxy_list.fetch_proxies()
proxy_list.return_proxies()
res = proxy_list.get("https://google.com")
```
