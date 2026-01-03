package main

import (
	"context"
	"io"
	"log"

	"github.com/segmentio/kafka-go"
)

type KafkaProducer struct {
	writer *kafka.Writer
}

func NewKafkaProducer() *KafkaProducer {
	w := &kafka.Writer{
		Addr:     kafka.TCP("localhost:9092"),
		Topic:    "incidents",
		Balancer: &kafka.LeastBytes{},
	}

	return &KafkaProducer{writer: w}
}

func (p *KafkaProducer) Publish(body io.Reader) {
	data, err := io.ReadAll(body)
	if err != nil {
		log.Println("read error:", err)
		return
	}

	err = p.writer.WriteMessages(context.Background(),
		kafka.Message{Value: data},
	)

	if err != nil {
		log.Println("kafka write error:", err)
	}
}
