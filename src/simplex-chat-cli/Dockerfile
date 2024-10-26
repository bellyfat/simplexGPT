FROM debian:latest

# Install dependencies to build OpenSSL
RUN apt-get update && apt-get install -y \
    curl \
    build-essential \
    checkinstall \
    zlib1g-dev \
    wget

# Download, build, and install OpenSSL 1.1.1k
RUN wget https://www.openssl.org/source/openssl-1.1.1k.tar.gz \
    && tar -xzvf openssl-1.1.1k.tar.gz \
    && cd openssl-1.1.1k \
    && ./config \
    && make \
    && make install \
    && cd .. \
    && rm -rf openssl-1.1.1k openssl-1.1.1k.tar.gz

# Download and install SimpleX Chat CLI
RUN curl -o- https://raw.githubusercontent.com/simplex-chat/simplex-chat/stable/install.sh | bash

WORKDIR /app


# Run SimpleX Chat CLI with WebSocket enabled on port 5225
CMD ["simplex-chat", "-p", "5225"]
