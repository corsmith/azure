# azure
misc azure tools

## usage

usage: show-ip-route.py [-h] [ip]

positional arguments:
  ip

optional arguments:
  -h, --help  show this help message and exit

## howto

Launch the Azure Cloud Shell -> Bash

```
$ wget https://raw.githubusercontent.com/corsmith/azure/main/show-ip-route.py
$ chmod 755 show-ip-route.py
$ az network nic show-effective-route-table  --resource-group RESOURCEGROUP --name NICNAME | ./show-ip-route.py
```

## sample output

```
addressPrefix       destinationServiceTags    disableBgpRoutePropagation    hasBgpOverride    name    nextHopIpAddress    nextHopType    source    state    tagMap
------------------  ------------------------  ----------------------------  ----------------  ------  ------------------  -------------  --------  -------  --------
['0.0.0.0/0']       []                        False                         False             None    []                  Internet       Default   Active   {}
['8.8.8.8/32']      []                        False                         False             google  ['10.1.3.4']        None           User      Active   {}
['10.0.0.0/8']      []                        False                         False             None    []                  None           Default   Active   {}
['10.1.0.0/16']     []                        False                         False             None    []                  VnetLocal      Default   Active   {}
['25.33.80.0/20']   []                        False                         False             None    []                  None           Default   Active   {}
['25.41.3.0/25']    []                        False                         False             None    []                  None           Default   Active   {}
['100.64.0.0/10']   []                        False                         False             None    []                  None           Default   Active   {}
['192.168.0.0/16']  []                        False                         False             None    []                  None           Default   Active   {}
```
