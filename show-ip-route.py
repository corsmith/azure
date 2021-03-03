#!/usr/bin/env python3

import argparse, ipaddress, json, operator, pprint, sys

parser = argparse.ArgumentParser()
parser.add_argument('ip', nargs='?', default=False)
args = parser.parse_args()

if args.ip:
    try:
        args.ip = ipaddress.ip_address(args.ip)
    except:
        sys.exit(f'invalid ip address: {args.ip}')

data = json.loads(sys.stdin.read())['value']
'''
 {'addressPrefix': ['192.168.0.0/16'],
  'destinationServiceTags': [],
  'disableBgpRoutePropagation': False,
  'hasBgpOverride': False,
  'name': None,
  'nextHopIpAddress': [],
  'nextHopType': 'None',
  'source': 'Default',
  'state': 'Active',
  'tagMap': {}},
'''

for r in data:
    r['prefix'] = ipaddress.ip_network(r['addressPrefix'][0])

best = False
for row in sorted(data, key=lambda r: r['prefix']):
    if args.ip:
        if args.ip in row['prefix']:
            best = row
    else:
        pprint.pprint(row)

if args.ip:
    pprint.pprint(best)
