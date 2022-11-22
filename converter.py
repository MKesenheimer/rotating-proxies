import os
import sys
import argparse

def main(args):
    with open(args.input_file, "r+") as file:
        line = file.readline()
        print(line)

        while line:
            line = args.proxy_type + " 	 " + line.replace(":", " ")

            with open(args.output_file, 'a+') as out:
                out.write(line)
                print(line)

            line = file.readline()


# main program
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('-i', '--in', dest='input_file', type=str, required=True, help='Path to input file.')
    parser.add_argument('-o', '--out', dest='output_file', type=str, required=True, help='Path to output file.')
    parser.add_argument('-p', '--proxy-type', dest='proxy_type', type=str, required=True, help='Type of proxy, for example socks4, socks5 or http')
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