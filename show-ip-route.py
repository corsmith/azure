#!/usr/bin/env python3

import argparse, ipaddress, json, sys, tabulate

parser = argparse.ArgumentParser()
parser.add_argument('ip', nargs='?', default=False)
args = parser.parse_args()

if args.ip:
    try:
        args.ip = ipaddress.ip_address(args.ip)
    except:
        sys.exit(f'invalid ip address: {args.ip}')

data = json.loads(sys.stdin.read())['value']

headers = [ k for k in data[0].keys() ] # make a copy
rtable = []

for r in data:
    r['prefix'] = ipaddress.ip_network(r['addressPrefix'][0])

for row in sorted(data, key=lambda r: r['prefix']):
    if args.ip:
        if args.ip in row['prefix']:
            rtable = [ row ]
    else:
        rtable.append(row)

cooked = []
for row in rtable:
    cooked.append([ f'{ row[header] }' for header in headers ])

print(tabulate.tabulate(cooked, headers=headers))
