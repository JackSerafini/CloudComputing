FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    hpcc \
    iozone3 \
    iperf3 \
    sysbench \
    && rm -rf /var/lib/apt/lists/*

CMD ["bash"]