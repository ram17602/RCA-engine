package main


import "golang.org/x/time/rate"


type RateLimiter struct {
limiter *rate.Limiter
}


func NewRateLimiter(rps int) *RateLimiter {
return &RateLimiter{rate.NewLimiter(rate.Limit(rps), rps)}
}


func (r *RateLimiter) Allow() bool {
return r.limiter.Allow()
}