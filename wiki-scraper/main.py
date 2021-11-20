import proxy
import scrape_wiki
#import asyncio
import kafka


BROKER = 'PLAINTEXT://0.0.0.0:9092'
CONSUMER_GROUP = 'wiki-scraper-1'


if __name__ == "__main__":

    ports = ["8080", "80"]
    proxy_list = proxy.ProxyList(https=False, ports=ports)
    proxy_list.fetch_proxies()

    #content = proxy_list.get("https://google.com")

    producer = kafka.init_producer()
    producer.flush()
    kafka.produce(producer, "Hello, world!")

    consumer = kafka.init_consumer()
    consumer

    while True:
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print(f"Consumer error: {msg.error()}")
            continue

        print(f'Received message: {msg.value().decode("utf-8")}')

    c.close()
