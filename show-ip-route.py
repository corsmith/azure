#!/usr/bin/env python3

import ipaddress, json, operator, pprint, sys

host = False
if len(sys.argv) == 2:
    try:
        host = ipaddress.ip_address(sys.argv[1])
    except:
        sys.exit(f'invalid ip address: {sys.argv[1]}')

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
    if host:
        if host in row['prefix']:
            best = row
    else:
        pprint.pprint(row)

if host:
    pprint.pprint(best)
