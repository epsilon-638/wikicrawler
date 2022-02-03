from confluent_kafka import Producer, Consumer


BROKER = 'PLAINTEXT://0.0.0.0:9092'
CONSUMER_GROUP = 'wiki-scraper-1'


def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

def init_producer():
    return Producer({
        'bootstrap.servers': BROKER
    })

def init_consumer():
    consumer = Consumer({
        'bootstrap.servers': BROKER, 
        'group.id': CONSUMER_GROUP,
        'auto.offset.reset': 'earliest'
    })
    consumer.subscribe(['urls'])
    return consumer

def produce(p, msg):
    p.poll(0)
    p.produce(
        'node-content',
        msg.to_json(),
        callback=delivery_report,
    )

def consume(c):
    msg = consumer.poll(1.0)
    if not msg:
        continue

    if msg.error():
        print(f'Error: {msg.error()}')
        continue
    print(f'Message: {msg.value().decode('utf-8')})
    return msg.value().decode('utf-8')

