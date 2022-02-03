package kafka

import (
	ckafka "github.com/confluentinc/confluent-kafka-go/kafka"
)

func returnConsumerConfigMap() *ckafka.ConfigMap {
	return &ckafka.ConfigMap{
		"bootstrap.servers": BROKER,
		"group.id":          CONSUMER_GROUP,
	}
}

func returnConsumer() (*ckafka.Consumer, error) {
	configMap := returnConsumerConfigMap()
	consumer, err := ckafka.NewConsumer(configMap)
	if err != nil {
		return nil, err
	}
	return consumer, err
}

func InitConsumer() (*ckafka.Consumer, error) {
	consumer, err := returnConsumer()
	if err != nil {
		return nil, err
	}
	consumer.SubscribeTopics([]string{"queued-urls"}, nil)
	return consumer, err
}
