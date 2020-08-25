package main

import (
	"github.com/gin-gonic/gin"
	"time"
)

func main() {
	r := gin.Default()
	r.GET("/test", func(c *gin.Context) {
		// 为了更好的看出效果，在服务端刻意延迟了2 秒返回数据。
		time.Sleep(time.Second * 2)
		c.JSON(200, gin.H{
			"msg": "Got it",
		})
	})
	r.Run()
}