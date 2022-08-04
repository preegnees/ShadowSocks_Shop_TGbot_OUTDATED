port=55555

ufw deny $port/tcp

ufw deny $port/udp

ufw enable

ufw status

docker stop /ss-rust

docker rm /ss-rust