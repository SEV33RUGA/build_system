# Build system

## Description
This is a Python CLI utility for determining the sequence of tasks in the build.

### Task
The task is what needs to be done.
For example:
- collect game resources
- compile .exe
- package the game, and so on.

The task is described by a unique name ('name') and its dependencies ('dependencies') on other tasks. A task cannot be completed before its dependencies. 
Task descriptions are given in .yaml file [tasks.yaml](tasks.yaml).

### Build
A build is a group of tasks combined functionally.
For example:
- "Build a game" with tasks: "collect game resources", "compile .exe", "pack the game".
- "Run tests" with tasks: "collect game resources", "compile .exe" etc.

The build is described by a unique name ('name') and a list of tasks ('tasks').
Build descriptions are set in the yaml file [builds.yaml](builds.yaml).

## How to use
The program ([build_system.py](build_system.py)) loads [tasks.yaml](tasks.yaml) and [build.yaml](build.yaml), which contain `tasks` and `builds`, respectively, and further operates with them. By default, the path to the files is considered **the current working directory**.

### Command `list`
The `list` command with the `builds` and `tasks` arguments to view the names of uploaded `builds` and `tasks`, respectively.

Examples:
```
python build_system.py list builds
```
Output:
```
List of available builds:
 * approach_important
 * audience_stand
 * time_alone
```
