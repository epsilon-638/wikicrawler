FROM golang:alpine

RUN apk update && apk add gcc librdkafka-dev openssl-libs-static zlib-static zstd-libs libsasl librdkafka-static lz4-dev lz4-static zstd-static libc-dev musl-dev

WORKDIR /app

COPY go.mod ./
COPY go.sum ./
COPY kafka/* ./kafka/

RUN go mod download

COPY *.go ./

RUN go build -tags musl -ldflags '-w -extldflags "-static"' -o /main

CMD ["/main"]
