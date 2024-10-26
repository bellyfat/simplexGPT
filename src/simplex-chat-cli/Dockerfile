FROM debian:latest

RUN apt-get update && apt-get install -y curl libssl1.1

# Download and install SimpleX Chat CLI
RUN curl -LO https://github.com/simplex-chat/simplex-chat/releases/download/v6.1.0.9/simplex-chat-cli-linux-amd64.tar.gz \
    && tar -xzf simplex-chat-cli-linux-amd64.tar.gz -C /usr/local/bin \
    && rm simplex-chat-cli-linux-amd64.tar.gz

WORKDIR /app

CMD ["simplex-chat"]
