#!/bin/sh

# TODO: test for OS and adapt the commands accordingly.

# Colors
NOCOLOR='\033[0m'
RED='\033[0;31m'
GREEN='\033[0;32m'
ORANGE='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
LIGHTGRAY='\033[0;37m'
DARKGRAY='\033[1;30m'
LIGHTRED='\033[1;31m'
LIGHTGREEN='\033[1;32m'
YELLOW='\033[1;33m'
LIGHTBLUE='\033[1;34m'
LIGHTPURPLE='\033[1;35m'
LIGHTCYAN='\033[1;36m'
WHITE='\033[1;37m'

usage() {
  echo -e $NOCOLOR
  echo "usage: $0 <path to proxychains.conf> <list of proxies to add>"
  echo "Note: Previous proxies defined in proxychains.conf will be deleted! Make a backup!"
}

if [ "$#" -lt 2 ]; then
    echo "Illegal number of parameters."
    usage
    exit -1
fi

proxyconfpath="$1"
proxylist="$2"

sudo sed -i'.bak' -e '/\[ProxyList\]/,$d' $proxyconfpath
echo "[ProxyList]" | sudo tee -a $proxyconfpath
cat $proxylist | sudo tee -a $proxyconfpath
