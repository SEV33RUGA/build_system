# Build system

## Description
This is a Python CLI utility for determining the sequence of tasks in the build.

### Task
The task is what needs to be done.
For example:
- collect game resources
- compile .exe
- package the game, and so on.

### Build
A build is a group of tasks combined functionally.
For example:
- "Build a game" with tasks: "collect game resources", "compile .exe", "pack the game".
- "Run tests" with tasks: "collect game resources", "compile .exe" etc.
