ARG BASEIMAGE=alpine:3
ARG BUILD_DATE
FROM ${BASEIMAGE}
LABEL maintainer="Daniel Brito danielbrzen@outlook.com" \
org.label-schema.build-date=$BUILD_DATE \
org.label-schema.name="Samba"
ENV smbuser=prueba pass=12345 uid=1200 
WORKDIR /home/sambashare
RUN apk update \
&& apk upgrade \
&& apk add bash samba-common-tools samba tzdata \
&& rm -rf /var/cache/apk/* \
&& adduser -u ${uid} -SDH ${smbuser} \
&& echo "$pass" |tee - |smbpasswd -s -a "$smbuser" 
COPY smb.conf /etc/samba/smb.conf
RUN sed -i "s|valid users = .*|valid users = $smbuser|" /etc/samba/smb.conf
EXPOSE 138/udp 137/udp 139 445
HEALTHCHECK --interval=60s --timeout=15s CMD smbclient -L localhost -U $smbuser -W WORKGROUP