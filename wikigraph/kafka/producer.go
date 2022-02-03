package kafka

import (
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

/*
func Produce(event map[string]interface{}, topic string) error {
	b, err := json.Marshal(event)
	if err != nil {
		return err
	}
	eventObject := createEventObject(b, topic)
}
*/
