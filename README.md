# Pyproject

Pyproject is a commandline utility for creating cli and curses based Python
projects. The resulting skeletons are already configured with base dependencies
and preconfigued Dockerfiles. 

## Getting Started

### Prerequisites

Ensure you have an [OCI](https://opencontainers.org/) compatible runtime installed.

> **NOTE: I'm using [Podman](https://podman.io) instead of docker for running my images locally. If you are using Docker just swap out "podman" for "docker" in the following commands. I am not currently testing functionality for Docker.**

### Quick Start

The fastest way to get started is to set the following alias:

```
alias pyproject='podman run --rm --userns keep-id -v $PWD:/tmp/project:Z --security-opt label=disable sdj92/pyproject:latest python /usr/local/bin/pyproject'
```

Once the alias is set start using pyproject:

```
$ pyproject --help
```

## Project Skeletons

The pyproject command can be used to create project skeletons using the following
examples.

To make a cli project:

```
$ pyproject create cli testcli
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

```
$ pyproject create cli testcurses
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

## Building the created project

Once the skeleton is created you can create the initial "Hello, World!" package
with: 

```
$ cd testcli
$ podman build -t testcli:latest .
```

## Version management

The pyproject command also allows you to get and set the version information in 
the project. Currently this is just a quick way to set the version in `setup.py`
but can easily be expanded to handle other files that might hold project version 
such as the Dockerfile.

```
$ pyproject version get
setup.py version: 	0.1
$ pyproject version update 2.3
setup.py version: 	2.3
```

## Testing

I'm using unittest for my testing. Currently the tests are not on the master 
branch, they are still a work in progress. Since I am using the built in
unittest module the only dependency for testing is [pipenv](https://pipenv.pypa.io/en/latest/).

```
$ pipenv run python -m unittest discover tests "test_*.py"
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

## My Todo
- [ ] create tests for this project
- [ ] project skeletons should have a dummy test added
- [ ] write a legit readme
