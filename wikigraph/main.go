package main

import (
	"log"

	"github.com/epsilon-638/wikigraph/kafka"
)

func main() {

	producer, err := kafka.InitProducer()
	if err != nil {
		log.Fatal(err)
	}
	defer producer.Close()

	consumer, err := kafka.InitConsumer()
	if err != nil {
		log.Fatal(err)
	}

	defer consumer.Close()

	consumer.SubscribeTopics([]string{"node-content"})

	go func() {
		for {
			msg, err := consumer.ReadMessage(-1)
			if err != nil {
				log.Fatal(err)
			}
			log.Print(msg)
		}
	}()

	func() {
		for {

		}
	}()

}
