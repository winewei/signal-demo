package main

import (
	"github.com/gin-gonic/gin"
	"time"
)

func main() {
	r := gin.Default()
	r.GET("/test", func(c *gin.Context) {
		time.Sleep(time.Second * 2)
		c.JSON(200, gin.H{
			"msg": "Got it",
		})
	})
	r.Run()
}