#!/bin/sh

# TODO: check if arguments are provided
# TODO: test for OS and adapt the commands accordingly.

proxyconfpath="$1"
proxylist="$2"

sudo sed -i'.bak' -e '/\[ProxyList\]/,$d' $proxyconfpath
echo "[ProxyList]" | sudo tee -a $proxyconfpath
cat $proxylist | sudo tee -a $proxyconfpath
