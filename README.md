# raumd v0.0.1
### (de) raumdeuter - (en) space interpreter.
#
```
for shell users who don't like to remember sequences of commands, raumd is a helper tool that customizes the interaction with the shell. 
unlike other shell tools it is a hybrid between the on-premise nature of shell and the accessibility of a web based definition provided through https://airlocks.xyz. 
```

## why?
the aim with **raumd** is to create an intuitive, portable and robust shell tool. when using raumd you are be able to:
- write complex set of shell commands only once and then call it by a operation name you decide 
- organize your commands with nested sublists 
- run the same commands on multiple machines 
- share the sequence with your collaborators
- standardize commands across your projects
- use it as a cli interface for tools without one
- replace your scripts with a json definition

## how?
### prerequisites
raumd is a python script, so the prerequisite for using raumd is python, the programming language for running, and pip the package installer for installation. (version>=3) 

### airlocks.xyz
the sequences are defined and downloaded from https://airlocks.xyz, that is a platform for defining sequences of things, developed by yours truly. raumd consumes and runs those sequences. 

### sequence.json
the sequences you download are aggregated into the **sequence.json** file. 
the file can be configured to a relative path or a global path. 
the relative filepath will result in raumd creating a file wherever it is ran from while the global file path will make the sequences available from wherever you run raumd in your computer. for both versions the filepath must exist a priori. 

### json file structure
```
{
  "samplesequence": {
    "id": "samplesequence",
    "title": "samplesequence",
    "parent_id": null,
    "seq": [
      {
        "name": "Print something ",
        "command": "echo \"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.""
      },
      {
        "name": "Sleep a little bit",
        "command": "sleep 10"
      },
      {
        "id": "9hl8k",
        "title": "sublist",
        "parent_id": null,
        "seq": [
          {
            "name": "sub_command_a",
            "command": "ping -t 10 www.google.com"
          },
          {
            "name": "whereas",
            "command": "pwd"
          },
          {
            "name": "whatishere",
            "command": "ls -l"
          },
          {
            "name": "disk usage",
            "command": "du -s"
          }
        ],
        "lastAutoSave": "03/04/2022, 17:03:39",
        "lock": null
      }
    ],
    "lastAutoSave": "03/04/2022, 16:54:07",
    "lock": null
  },
  "anothersequence": {...}
  ...
}
``` 

### install
install the pre-built version from the official python artifactory, using pip:
```
pip install raumd
```

install via **setup.py** from source code: 
```
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

## plans for 1.0.0
- refactor code
- execution server
- conditions for execution
- website
- authentication and authorization
- commands with inputs
- local imports
- edit sequences in cli mode
- add new operations (remove..)
- upload sequence from raumd to airlocks
- command alternatives for different OSs
- git integration
- local airlocks

## contribute
get in touch if you're interested in contributing.

## contact me
romanbotnari@me.com

## license
Apache License, Version 2.0
