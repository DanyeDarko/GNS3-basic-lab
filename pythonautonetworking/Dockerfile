ARG BASE_IMAGE=python:3.7-slim-stretch
FROM ${BASE_IMAGE} as builder
WORKDIR /dependencies
RUN pip install --no-warn-script-location \
   --prefix=/dependencies napalm netmiko

FROM python:3.7-slim-stretch as prod
ARG USERNAPALM=
ARG BUILD_DATE=
LABEL maintainer="Daniel Brito danielbrzen@outlook.com" \
org.label-schema.build-date=$BUILD_DATE \
org.label-schema.name="Networking Automation python tools"
COPY --from=builder /dependencies /usr/local
ENV username=${USERNAPALM} 
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y --no-install-recommends \
libssl-dev \
libffi-dev \
python-dev \
python-cffi \
nano \
&& apt-get clean -y \
&& rm -rf /var/lib/apt/lists/* \
&& useradd -m -s /bin/bash --uid 1200  ${username}  \
&& chown -R ${username}:${username} /home/${username}
USER ${username}
