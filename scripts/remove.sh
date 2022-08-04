docker stop /ss-rust

docker rm /ss-rust

apt remove -y git apt-transport-https ca-certificates curl gnupg lsb-release && apt purge -y git apt-transport-https ca-certificates curl gnupg lsb-release

rm /usr/share/keyrings/docker-archive-keyring.gpg

apt remove -y docker-ce docker-ce-cli containerd.io && apt purge -y docker-ce docker-ce-cli containerd.io

rm -r /etc/shadowsocks-rust