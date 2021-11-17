# author: epsilon-638
import os
import sys
import requests as req
from itertools import cycle
from bs4 import BeautifulSoup


PROXY_PROVIDER = "https://free-proxy-list.net/"


class Proxy:

    def __init__(self, ip, port, code, country, anon, google, https, lifetime):

        self.ip = ip
        self.port = port
        self.code = code
        self.country = country
        self.anon = anon
        self.google = google
        self.https = https
        self.lifetime = lifetime

    def return_proxy(self):
        proxy = f'http://{self.ip}:{self.port}'
        return {
            "http": proxy,
            "https": proxy,
        }

    def get(self, url, timeout=3):
        try:
            print(f"Fetching: {url}")
            r = req.get(url, proxies=self.return_proxy(), timeout=timeout)
            return r.content
        except:
            print(f"Failed to get resource: {url}")
            self.lifetime -= 1
            return 0



class ProxyList:

    def __init__(self, 
                 anon_levels=None, 
                 https=True, 
                 countries=None,
                 google=False,
                 ports=None,
                 codes=None,
                 refresh=10000,
                 proxy_lifetime=1):

        self.anon_levels = anon_levels
        self.https = https
        self.countries = countries
        self.google = google
        self.ports = ports
        self.codes = codes
        self.refresh = refresh
        self.proxy_lifetime = proxy_lifetime

        self.proxies = []
        self.rotate_proxies = None 


    def validate_proxy(self, anon, port, code, country, google, https):
        if self.anon_levels is not None:
            if anon not in self.anon_levels:
                return False
        if self.ports != None:
            if port not in self.ports:
                return False
        if self.codes != None:
            if code not in self.code:
                return False
        if self.countries != None:
            if country not in self.countries:
                return False
        if self.google != False:
            if google != self.google:
                return False
        if self.https != False:
            if https != self.https:
                return False
        return True


    def fetch_proxies(self):
        print("Fetching proxies...")
        proxies = []
        r = req.get(PROXY_PROVIDER)
        soup = BeautifulSoup(r.content, 'html.parser')
        proxy_rows = soup.find('tbody').find_all('tr')
        bool_map = {"yes": True, "no": False}
        for row in proxy_rows:
            try:
                data = BeautifulSoup(str(row), 'html.parser').find_all('td')
                ip = BeautifulSoup(str(data[0]), 'html.parser').get_text()
                port = BeautifulSoup(str(data[1]), 'html.parser').get_text()
                code = BeautifulSoup(str(data[2]), 'html.parser').get_text()
                country = BeautifulSoup(str(data[3]), 'html.parser').get_text()
                anon = BeautifulSoup(str(data[4]), 'html.parser').get_text()
                google = bool_map[BeautifulSoup(str(data[5]), 'html.parser').get_text()]
                https = bool_map[BeautifulSoup(str(data[6]), 'html.parser').get_text()]
                if self.validate_proxy(anon, str(port), code, country, google, https):
                    proxies.append(Proxy(ip, port, code, country, anon, google, https, self.proxy_lifetime)) 
            except:
                pass
        self.proxies = proxies
        self.rotate_proxies = cycle(proxies)
        print(f"Proxies fetched: {len(proxies)}")


    def get(self, url, timeout=3):

        try:
            while True:
                print("getting next proxy...")
                proxy = next(self.rotate_proxies)
                print(f"Using: {proxy.return_proxy()['http']}")
                content = proxy.get(url, timeout)
                print("Fetched")
                if content != 0:
                    return content
            
                print(f"Proxy failed: {proxy.return_proxy()['http']}")
                proxy.lifetime -= 1
                if proxy.lifetime == 0:
                    self.proxies = self.proxies.remove(proxy)
                    self.rotate_proxies = cycle(self.proxies)
                    print("proxy killed")
                    if len(self.proxies) == 0:
                        self.fetch_proxies()
                        print("refetch")
        except KeyboardInterrupt:
            print("Interrupted")
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)

    def return_proxies(self):
        for p in self.proxies:
            try:
                print(p.return_proxy()["http"])
            except:
                continue
