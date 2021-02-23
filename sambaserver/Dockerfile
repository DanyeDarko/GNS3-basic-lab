FROM  ubuntu:18.04
ENV smbuser=test pass=12345 uid=1200
WORKDIR /home/sambashare
RUN apt-get update && apt-get install -y  --no-install-recommends \
samba-common samba \
&& apt-get -y clean \
&& rm -rf /var/lib/apt/lists/* \
&& useradd -u ${uid} -c "testing user for samba" -s /bin/bash -p ${pass} ${smbuser} \
&& (echo $pass; echo $pass) | smbpasswd -a $smbuser  -s
COPY smb.conf /etc/samba/smb.conf
EXPOSE 445 138 137 139
