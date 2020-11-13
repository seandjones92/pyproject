# Pyproject

Pyproject is a commandline utility for creating cli and curses based Python projects. The resulting skeletons are already configured with base dependencies and preconfigued Dockerfiles.

## Getting Started

### Prerequisites

python click package

```
apt install python3-click # Ubuntu
dnf install python3-click # Fedora
```

### Quick Start

```shell
pyproject --help
```

## Project Skeletons

The pyproject command can be used to create project skeletons using the following
examples.

To make a cli project:

```shell
$ pyproject cli testcli
$ tree testcli
testcli
├── bin
│   └── testcli
├── Dockerfile
├── Pipfile
├── requirements.txt
├── setup.py
└── testcli
    └── __init__.py

2 directories, 6 files
```

To make an ncurses project:

```shell
$ pyproject cli testcurses
$ tree testcurses
testcurses
├── bin
│   └── testcurses
├── Dockerfile
├── Pipfile
├── requirements.txt
├── setup.py
└── testcurses
    └── __init__.py

2 directories, 6 files
```
