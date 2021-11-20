package kafka

import (
	ckafka "github.com/confluentinc/confluent-kafka-go/kafka"
)

const BROKER = "PLAINTEXT://0.0.0.0:9092"

func returnProducerConfigMap() *ckafka.ConfigMap {
	return &ckafka.ConfigMap{
		"bootstrap.servers": BROKER,
	}
}

func returnProducer() (*ckafka.Producer, error) {
	configMap := returnProducerConfigMap()
	producer, err := ckafka.NewProducer(configMap)
	if err != nil {
		return nil, err
	}
	return producer, nil
}
