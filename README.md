# Pyproject

Pyproject is a commandline utility for creating cli and curses based Python projects. The resulting skeletons are already configured with base dependencies and preconfigued Dockerfiles.

I started working on this when I found myself spending more time than I wanted starting up projects than working on them. I'd get an idea for something then quickly get lost in the weeds of "how do I set up Click for a project?" or "how did I contianerize that before?". Now I can build out a project template in about 2 seconds that is ready to be packaged and has some basic functionality out of the box. 

I chose to deliver this as a contianer image for portability, the project skeletons this creates are also configured to be delivered as container images. 

## Getting Started

### Prerequisites

Ensure you have an [OCI](https://opencontainers.org/) compatible runtime installed.

> **NOTE: I'm using [Podman](https://podman.io) instead of docker for running my images locally. The alias for Podman below has some extra options as the container is run rootless so SELinux tends to get in the way when writing files to the host.**

### Quick Start

The fastest way to get started is to set the following alias:

```shell
alias pyproject='podman run --rm --userns keep-id -v $PWD:/tmp/project:Z --security-opt label=disable sdj92/pyproject:latest python /usr/local/bin/pyproject'
```

Or, if you are using Docker the following should work:

```shell
alias pyproject='docker run --rm -v $PWD:/tmp/project:Z sdj92/pyproject:latest python /usr/local/bin/pyproject'
```

Once the alias is set start using pyproject:

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

## Building and running the created project

Once the skeleton is created you can create the initial "Hello, World!" package
with:

```shell
$ cd testcli
$ podman build -t localhost/testcli:latest .
STEP 1: FROM python:3.8-slim-buster
STEP 2: ENV PYTHONDONTWRITEBYTECODE 1
--> e35548bc808
STEP 3: ENV PYTHONUNBUFFERED 1
--> 7dfa9bbf0d5
STEP 4: ADD requirements.txt .
--> f73dd038ef6
STEP 5: RUN python -m pip install -r requirements.txt
Looking in indexes: https://pypi.python.org/simple
Collecting click==7.1.2
  Downloading click-7.1.2-py2.py3-none-any.whl (82 kB)
     |████████████████████████████████| 82 kB 139 kB/s
Installing collected packages: click
Successfully installed click-7.1.2
```

To run the "Hello, World!" package created in the example above you would use the following command. This is something you'll likely want to alias:
```shell
podman run --rm localhost/testcli:latest python /usr/local/bin/testcli
```

## Testing

I'm using unittest. The only dependency for testing is [pipenv](https://pipenv.pypa.io/en/latest/).

```shell
$ pipenv run python -m unittest discover tests "test_*.py"
.....
----------------------------------------------------------------------
Ran 5 tests in 0.012s

OK
```
