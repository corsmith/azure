#!/usr/bin/env python

import ipaddress, json, operator, pprint, sys

host = ipaddress.ip_address(sys.argv[1])

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
    if host in row['prefix']:
        best = row

pprint.pprint(best)
