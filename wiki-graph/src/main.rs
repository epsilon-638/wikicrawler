use kafka::client::{FetchPartition, KafkaClient};
use consumer::process;

fn main() {

    let broker = "localhost:9092";
    let topic = "my-topic";
    let partition = 0;
    let offset = 0;

    let mut client = KafkaClient::new(vec![broker.to_owned()]);
    if let Err(e) = client.load_metadata_all() {
        println!("Failed to load metadata from {}: {}", broker, e);
        return;
    }

    if !client.topics().contains(topic) {
        println!("No such topic at {}: {}", broker, topic);
        return;
    }

    match client.fetch_message(&[FetchPartition::new(topic, partition, offset)]) {
        Err(e) => {
            println!("Failed to fetch messages: {}", e);
        }
        Ok(resps) => {
            for resp in resps {
                for t in resp.topics() {
                    match p.data() {
                        &Err(ref e) => {
                            println!("partition error: {}:{}: {}", t.topic(), p.partition(), e)
                        }
                        &Ok(ref data) => {
                            println!(
                                "Topic: {} / partition: {} / latest available message offset: {}",
                                t.topic(),
                                p.partition(),
                                data.highwatermark_offset());
                            for msg in data.messages() {
                                println!(
                                    "topic: {} / partition: {} / message.offset: {}",
                                    t.topic(),
                                    p.partition(),
                                    msg.offset,
                                    msg.value.len()
                                );
                            }
                        }
                    }
                }
            }
        }
    }


    println!("Hello, world!");
}
