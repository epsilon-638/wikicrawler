use std::time::Duration;
use kafka::consumer::{Consumer, FetchOffset};


fn process(cfg: Config) -> Result<(), &'static str> {
    let mut c = {
        let mut cb = Consumer::from_hosts(cfg.brokers)
            .with_group(cfg.group)
            .with_fallback_offset(cfg.fallback_offset)
            .with_fetch_max_wait_time(Duration::from_secs(1))
            .with_fetch_min_bytes(1_000)
            .with_fetch_max_bytes_per_partition(100_000)
            .with_retry_max_bytes_limit(1_000_000)
            .with_offset_storage(cfg.offset_storage)
            .with_client_id("wiki-graph-1".into());
        for topic in cfg.topics {
            cb = cb.with_topic(topic);
        }
        cb.create().unwrap()
    };

    let mut buf = Vec::with_capacity(1024);

    loop {
        for ms in c.poll().unwrap().iter() {
            for m in ms.messages() {
                unsafe { buf.set_len(0) }
                let _ = writeln!(buf, "{}:{}@{}:", ms.topic(), ms.partition(), m.offset);
                buf.extend_from_slice(m.value);
                buf.push(b'\n');
            }
            let _ = c.consume_messageset(ms);
        }
        if do_commit {
            c.commit_consumed();
        }
    }
}
