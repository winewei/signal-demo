FROM golang:1.14-alpine3.12 AS builder

WORKDIR /srv
COPY . .

RUN go build -o app main.go

# final build image
FROM alpine:3.12

WORKDIR /srv

COPY --from=builder /srv/app app

#EXPOSE 8080

CMD ["/srv/app"]