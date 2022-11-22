#!/bin/sh

cd proxy-list-1
git pull
cd ..
python check.py -i proxy-list-1/online-proxies/txt/proxies-socks4.txt -o alive-proxies-socks4.txt -p socks4 -t 10
python converter.py -i alive-proxies-socks4.txt -o proxychains-socks4.txt -p socks4
./add-to-conf.sh /opt/local/etc/proxychains.conf proxychains-socks4.txt