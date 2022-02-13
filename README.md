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
## WikiContent
```python3
import proxy
import scrape_wiki

proxy_list = proxy.ProxyList()
proxy_list.fetch_proxies()
res = proxy_list.get("https://en.wikipedia.org/wiki/Wikipedia")

content = scrape_wiki.scrap_wiki(res.content)
```
## WIP: Will try to revisit this
