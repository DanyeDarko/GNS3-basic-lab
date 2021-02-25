ARG BASEIMAGE=ubuntu:18.04
ARG BUILD_DATE
FROM ${BASEIMAGE}
LABEL maintainer="Daniel Brito danielbrzen@outlook.com" \
org.label-schema.build-date=$BUILD_DATE \
org.label-schema.name="Samba"
ENV smbuser=prueba pass=12345 uid=1200 CONFIG_FILE="/etc/samba/smb.conf"
WORKDIR /home/sambashare
RUN apt-get update && apt-get install -y  --no-install-recommends \
samba-common samba \
&& apt-get -y clean \
&& rm -rf /var/lib/apt/lists/* \
&& useradd -u ${uid} -c "testing user for samba" -s /bin/bash -p ${pass} ${smbuser} \
&& (echo $pass; echo $pass) | smbpasswd -a $smbuser  -s 
COPY smb.conf /etc/samba/smb.conf
RUN sed -i "s|valid users = .*|valid users = $smbuser|" /etc/samba/smb.conf
EXPOSE 138/udp 137/udp 139 445
HEALTHCHECK --interval=60s --timeout=15s CMD smbclient -L localhost -U $smbuser -W WORKGROUP