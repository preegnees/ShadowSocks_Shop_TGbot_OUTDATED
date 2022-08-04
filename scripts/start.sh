port=55555

ufw allow $port/tcp

ufw allow $port/udp

# Do not forget to allow your ip to connect via ssh

ufw enable

ufw status

docker run -d -p $port:$port -p $port:$port/udp --name ss-rust --restart=always -v /etc/shadowsocks-rust:/etc/shadowsocks-rust teddysun/shadowsocks-rust