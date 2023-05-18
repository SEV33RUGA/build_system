# Build system

## Description
This is a Python CLI utility for determining the sequence of tasks in the build.

### Task
The task is what needs to be done.
For example:
- collect game resources
- compile .exe
- package the game, and so on.

The task is described by a unique name (`name`) and its dependencies (`dependencies`) on other tasks. A task cannot be completed before its dependencies. 
Task descriptions are given in .yaml file [tasks.yaml](https://github.com/SEV33RUGA/build_system/blob/af6cfffb3578aa82e3277e44da2f1461b3cfc369/tasks.yaml)

### Build
A build is a group of tasks combined functionally.
For example:
- "Build a game" with tasks: "collect game resources", "compile .exe", "pack the game".
- "Run tests" with tasks: "collect game resources", "compile .exe" etc.
