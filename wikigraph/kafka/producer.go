package kafka

import (
	"encoding/json"

	ckafka "github.com/confluentinc/confluent-kafka-go/kafka"
)

func returnProducerConfigMap() *ckafka.ConfigMap {
	return &ckafka.ConfigMap{
		"bootstrap.servers": BROKER,
	}
}

func InitProducer() (*ckafka.Producer, error) {
	configMap := returnProducerConfigMap()
	producer, err := ckafka.NewProducer(configMap)
	if err != nil {
		return nil, err
	}
	return producer, nil
}

func createEventObject(event []byte, topic string) *ckafka.Message {
	return &ckafka.Message{
		TopicPartition: ckafka.TopicPartition{
			Topic:     &topic,
			Partition: ckafka.PartitionAny},
		Value: event,
	}
}

func Produce(producer *ckafka.Producer, event map[string]interface{}, topic string, deliverChan chan ckafk.Event) error {
	b, err := json.Marshal(event)
	if err != nil {
		return err
	}
	eventObject := createEventObject(b, topic)
	return producer.Produce(eventObject, deliveryChan)
}

func ProduceURL(producer *ckafka.Producer, url string, topic string, deliveryChan chan ckafka.Event) error {
	b := []byte(url)
	eventObject := createEventObject(b, topic)
	return producer.Produce(eventObject, deliveryChan)
}
