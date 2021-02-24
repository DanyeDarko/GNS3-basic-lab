FROM debian:buster-slim
ENV user=gns3
LABEL maintainer="danielbrzen@outlook.com"
RUN apt-get update && \ 
apt-get install -y --no-install-recommends \ 
iproute2 \
iputils-ping \ 
openssh-client \
inetutils-telnet \ 
ansible \
&& apt-get clean -y && rm -rf /var/lib/apt/lists/* \
&& adduser --shel /bin/bash --disabled-password ${user}
USER ${user}
