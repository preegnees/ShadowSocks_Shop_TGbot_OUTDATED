port=55555
password=$(< /dev/urandom tr -dc A-Za-z0-9 | head -c 16)

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