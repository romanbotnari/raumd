# raumd v0.0.2

## what?
### (de) raumdeuter - (en) space interpreter.
#
```
for shell users who don't like to remember sequences of commands, 
raumd is a helper tool that customizes the interaction with the terminal. 
unlike other tools it is a hybrid between the on-premise nature of shell 
and the accessibility of a web based definition provided through https://airlocks.xyz. 
```

## why?

the aim of raumd is to have a pleasant interaction with the terminal, one that feels personal and doesn't involve writing complex commands, and even when it gets to it, raumd makes it possible to save them in a structured manner and easy to access afterwards, on other machines, or by interested colleagues. another option is running sequences of commands which should help with things like downloading sets of prerequisites, complex builds, or other things similar in nature. the relative sequences file would help in having say three commands that are repeatable across projects.

## how?

### airlocks.xyz
the sequences are defined and downloaded from https://airlocks.xyz, that is a platform for defining sequences(or even trees) of things, developed by yours truly. raumd consumes and runs those sequences. 
the plan is to enhance the tool with the possibility of creating, modifying and uploading the sequences directly with raumd.

### sequence.json
the sequences you download are aggregated into the **sequence.json** file. 
the file can be configured to a relative path or a global path. 
the relative filepath will result in raumd creating a file wherever it is ran from while the global file path will make the sequences available from wherever you run raumd in your computer. for both versions the filepath must exist a priori.

### run
```raumd run command -p param1=some_value param2=some_other_value```
as simple as that. also check the doc for examples and a full intro.

### where?
any os with a python3.