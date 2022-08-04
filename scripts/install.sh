port=55555
password=$(< /dev/urandom tr -dc A-Za-z0-9 | head -c 16)

apt update && apt upgrade -y

apt install -y git apt-transport-https ca-certificates curl gnupg lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

apt update

apt install -y docker-ce docker-ce-cli containerd.io

docker pull teddysun/shadowsocks-rust

mkdir /etc/shadowsocks-rust

cat > /etc/shadowsocks-rust/config.json <<EOF
{
    "server": "0.0.0.0",
    "server_port": $port,
    "password": "$password",
    "timeout": 300,
    "method": "chacha20-ietf-poly1305",
    "nameserver" :"8.8.8.8",
    "mode": "tcp_and_udp"
}
EOF

# the first time there is an installation error (my solution is to download a second time)

apt update && apt upgrade -y

apt install -y git apt-transport-https ca-certificates curl gnupg lsb-release

echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

apt update

apt install -y docker-ce docker-ce-cli containerd.io