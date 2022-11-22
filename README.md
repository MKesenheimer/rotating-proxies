# rotating-proxies helper scripts
Converts any common proxy list (IP:PORT) into a proxychains-compatible list (PROTOCOL  	 IP PORT) automatically.
Additionally, the script `check.py` can be used to check if the proxy is alive.

Proxy lists added from:

https://github.com/jetkai/proxy-list

https://github.com/TheSpeedX/PROXY-List

## Setup
Run this command to clone this repository:
```
git clone --depth 1 --recurse-submodules https://github.com/MKesenheimer/rotating-proxies.git
```

## Usage
Run, for example,
```
python converter.py -i proxies-socks5.txt -o proxychains-socks5.txt -p socks5
```
to convert a proxy list to the proxychains format.

Run
```
 python check.py -i proxies-socks5.txt -o alive-proxies-socks5.txt -p socks5 -t 10
```
to check which proxy is alive. Store the results in the file `alive-proxies-socks5.txt`.
