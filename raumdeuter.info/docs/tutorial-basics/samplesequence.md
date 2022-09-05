---
sidebar_position: 2
---

# samplesequence

## Download the sample file
```
raumd download samplesequence 
```

```
{'sub_seq': []}
{
    'id': 'samplesequence',
    'title': 'samplesequence',
    'parent_id': None,
    'seq': [
        {
            'name': 'Print something ',
            'command': 'echo "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industr..m."'
        },
        {'name': 'Sleep a little bit', 'command': 'sleep 10'},
        {'name': 'Print a json file ', 'command': 'echo "{\n  "squadName": "Super hero squad",\n  "homeTown": "Metro City",\n  "formed": 2016,\n  "secretBase": "Super tower",\n  "active": true\n}"'},
        {
            'id': '9hl8k',
            'title': 'sublist',
            'parent_id': None,
            'seq': [
                {'name': 'sub_command_a', 'command': 'ping -t 10 www.google.com'},
                {'name': 'whereas', 'command': 'pwd'},
                {'name': 'whatishere', 'command': 'ls -l'},
                {'name': 'disk usage', 'command': 'du -s'}
            ],
            'lastAutoSave': '03/04/2022, 17:03:39',
            'lock': None
        }
    ],
    'lastAutoSave': '03/04/2022, 16:54:07',
    'lock': None
}

```

## Show sequence
```
raumd show samplesequence 
```

```
name   : Print something 
command: echo "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since .."
name   : Sleep a little bit
command: sleep 10
name   : Print a json file 
command: echo "{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true
}"
subseq: 9hl8k / sublist
```

## Show subsequences
```
raumd show samplesequence 9hl8k
```

```
name   : sub_command_a
command: ping -t 10 www.google.com
name   : whereas
command: pwd
name   : whatishere
command: ls -l
name   : disk usage
command: du -s
```

## Run a subsequence
```
raumd run samplesequence 9hl8k
```

```
name   : sub_command_a
command: ping -t 10 www.google.com
PING www.google.com (142.250.201.196): 56 data bytes
64 bytes from 142.250.201.196: icmp_seq=0 ttl=58 time=22.658 ms
64 bytes from 142.250.201.196: icmp_seq=1 ttl=58 time=30.748 ms
64 bytes from 142.250.201.196: icmp_seq=2 ttl=58 time=30.534 ms
64 bytes from 142.250.201.196: icmp_seq=3 ttl=58 time=30.748 ms
64 bytes from 142.250.201.196: icmp_seq=4 ttl=58 time=28.141 ms
64 bytes from 142.250.201.196: icmp_seq=5 ttl=58 time=28.846 ms
64 bytes from 142.250.201.196: icmp_seq=6 ttl=58 time=22.802 ms
64 bytes from 142.250.201.196: icmp_seq=7 ttl=58 time=29.214 ms
64 bytes from 142.250.201.196: icmp_seq=8 ttl=58 time=28.701 ms
64 bytes from 142.250.201.196: icmp_seq=9 ttl=58 time=29.371 ms

--- www.google.com ping statistics ---
10 packets transmitted, 10 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 22.658/28.176/30.748/2.852 ms
Completed!
name   : whereas
command: pwd
/Users/romanbotnari/Downloads/raumd
Completed!
name   : whatishere
command: ls -l
total 40
-rw-r--r--   1 romanbotnari  staff   581 Jul 10 01:10 LICENSE
-rw-r--r--   1 romanbotnari  staff  4196 Jul 10 01:10 README.md
drwxr-xr-x  13 romanbotnari  staff   416 Jul 10 01:10 main
drwxr-xr-x  12 romanbotnari  staff   384 Jul 10 01:13 raumd
-rw-r--r--   1 romanbotnari  staff  1359 Sep  6 00:05 sequence.json
-rw-r--r--   1 romanbotnari  staff  1214 Jul 10 01:10 setup.py
Completed!
name   : disk usage
command: du -s
1024    .
Completed!

```

---