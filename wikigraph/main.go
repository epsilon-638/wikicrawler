package main

import (
	"encoding/json"
	"log"

	"github.com/epsilon-638/wikigraph/kafka"
)

type WikiContent struct {
	InternalLinks []string `json:"internal_links"`
	ExternalLinks []string `json:"external_links"`
	InternalMedia []string `json:"internal_media"`
	ExternalMedia []string `json:"external_media"`
	Citations     []string `json:"citations"`
}

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

	consumer.SubscribeTopics([]string{"node-content"}, nil)
	nodeContentChannel := make(chan WikiContent)

	func() {
		for {
			msg, err := consumer.ReadMessage(-1)
			if err != nil {
				log.Fatal(err)
			}
			var node WikiContent

			err := json.Unmarshal(msg.Value, &node)
			if err != nil {
				log.Fatal(err)
			}

			for _, link := range node.InternalLinks {
				err := kafka.ProduceURL(producer, link, "urls", deliveryChan)
				if err != nil {
					log.Fatal(err)
				}
			}

		}
	}()
}
