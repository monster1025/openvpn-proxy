FROM ventz/openvpn

ENV _3PROXY_VERSION 0.8.12
ENV _3PROXY_DOWNLOAD_URL https://github.com/z3APA3A/3proxy/archive/0.8.12.tar.gz
ENV _3PROXY_DOWNLOAD_SHA1 c669a9af27cf1c4178f73216ee74777d200e03fb

RUN set -ex \
	\
	&& apk add --no-cache --virtual .build-deps \
		gcc \
		linux-headers \
		make \
		musl-dev \
		tar \
		openssl \
	\
	&& wget -O 3proxy.tar.gz "$_3PROXY_DOWNLOAD_URL" \
	&& echo "$_3PROXY_DOWNLOAD_SHA1 *3proxy.tar.gz" | sha1sum -c - \
	&& mkdir -p /usr/src/3proxy \
	&& tar -xzf 3proxy.tar.gz -C /usr/src/3proxy --strip-components=1 \
	&& rm 3proxy.tar.gz \
	\
	&& make -C /usr/src/3proxy -f Makefile.Linux \
	&& make -C /usr/src/3proxy -f Makefile.Linux install \
	\
	&& rm -r /usr/src/3proxy \
	\
	&& apk del .build-deps

RUN apk update && apk upgrade && apk add python3 curl && pip3 install pyotp
ADD run.sh /run.sh
ADD generate.py /generate.py
ADD nserver.py /nserver.py
ADD 3pr.cfg /3pr.cfg
RUN chmod +x /run.sh

ENTRYPOINT "/run.sh"
