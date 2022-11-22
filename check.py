#!/usr/bin/env python3
#
# Usage: python check.py --in test.txt --out alive-test.txt --proxy-type "socks4" --timeout 10
#

import socks
import socket
import ssl
from urllib.request import *
import requests
import requests.packages.urllib3.util.connection as urllib3_cn
import argparse
import sys
import os

# force using IPv4
requests.packages.urllib3.util.connection.HAS_IPV6 = False 
def allowed_gai_family():
    family = socket.AF_INET
    return family
urllib3_cn.allowed_gai_family = allowed_gai_family

def main(args):
    file1 = open(args.input_file, 'r')
    lines = file1.readlines()
    typ   = args.proxy_type + "://"
    if typ == "http://":
        typ = "" # no type needed for http proxies
    
    for line in lines:
        address = line.strip()
        print("[INFO] proxy address: {}".format(address))

        proxy = {'http' : typ+address, 'https' : typ+address}
        if args.debug_enabled:
            print("[DEBUG] proxy = {}".format(proxy))

        try:
            resp = requests.get('http://icanhazip.com', 
                        proxies=proxy,
                        headers={},
                        timeout=args.time_out,
                        verify=False)
        except IOError:
            print("Down.")
        else:
            print("OK: {}".format(resp.content))
            file = open(args.output_file, 'a+')
            file.write(address)
            file.write("\n")
            file.close()

# main program
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('-i', '--in', dest='input_file', type=str, required=True, help='Path to input file.')
    parser.add_argument('-o', '--out', dest='output_file', type=str, required=True, help='Path to output file.')
    parser.add_argument('-t', '--timeout', dest='time_out', type=int, default=30, help='Timeout of request.')
    parser.add_argument('-p', '--proxy-type', dest='proxy_type', type=str, default="socks5://", help='Type of proxy, for example socks4, socks5 or http')
    parser.add_argument('-d', '--debug', dest='debug_enabled', action='store_true', help='Enable debug output.')
    args = parser.parse_args()

    try:
        main(args)
    except KeyboardInterrupt:
        print("Exiting.")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)