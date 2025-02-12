FROM ubuntu:latest

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y \
        wget \
        git \
        nano \
        build-essential \
        hwloc \
        libhwloc-dev \
        libevent-dev \
        gfortran \
        iozone3 \
        iperf3 \
        sysbench \
        htop 

CMD ["bash"]