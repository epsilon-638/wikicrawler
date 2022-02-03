import proxy
import scrape_wiki
import asyncio
import kafka


BROKER = 'PLAINTEXT://0.0.0.0:9092'
CONSUMER_GROUP = 'wiki-scraper-1'
WORKERS = 50


if __name__ == "__main__":

    ports = ["8080", "80"]
    proxy_list = proxy.ProxyList(https=False, ports=ports)
    proxy_list.fetch_proxies()


    producer = kafka.init_producer()
    consumer = kafka.init_consumer()

    while True:

        url = consume(c)
        content = proxy_list.get(url)

        produce(producer, scrape_wiki.scrape_wiki(content)))

    c.close()
