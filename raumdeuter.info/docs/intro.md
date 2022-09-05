---
sidebar_position: 1
---

# intro

### prerequisites
raumd is a python script, so the prerequisite for using raumd is python, the programming language for running, and pip the package installer for installation. (version>=3) 

as far as module goes these are the current requirements:

```
argcomplete==2.0.0
colorama==0.4.4
commonmark==0.9.1
psutil==5.9.0
Pygments==2.11.2
rich==11.0.0
python-json-logger==2.0.2

```


### install
install the pre-built version from the official python artifactory, using pip:
```
pip install raumd
```

install via **setup.py** from source code: 

```
git clone https://github.com/romanbotnari/raumd.git
cd raumd
python3 setup.py install  
```

### configure
there is a default configuration that one can change at any time (*using administrative rights*).

```sh
raumd configure -show    

url      : https://airlocks.xyz
path     : sequence.json
timeout  : 
localssl : No
failearly: Yes
```

### create a sequence
visit https://airlocks.xyz to create a sequence of commands.
there's also **samplesequence** for linux based OSs you can try out.

### download the sequnce
```sh
raumd download samplesequence             
```

### run the sequence
```sh
raumd run samplesequence
```

A sequence of commands looks like this:
```json
{
    'id': 'samplesequence',
    'title': 'samplesequence',
    'parent_id': None,
    'seq': [
        {
            'name': 'Print something ',
            'command': 'echo "Lorem Ipsum is .."'
        },
        {'name': 'Sleep a little bit', 'command': 'sleep 10'},
        {'name': 'Print a json file ', 'command': 'echo 
        "{\n  "squadName": "Super hero squad",\n  
        "homeTown": "Metro City",\n  
        "formed": 2016,\n  
        "secretBase": "Super tower",\n  
        "active": true\n}"'},
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

