package main


import (
"log"
"net/http"
)


func main() {
producer := NewKafkaProducer()
limiter := NewRateLimiter(100)


http.HandleFunc("/ingest", func(w http.ResponseWriter, r *http.Request) {
if !limiter.Allow() {
http.Error(w, "Rate limit exceeded", http.StatusTooManyRequests)
return
}
producer.Publish(r.Body)
w.WriteHeader(http.StatusAccepted)
})


log.Fatal(http.ListenAndServe(":8080", nil))
}