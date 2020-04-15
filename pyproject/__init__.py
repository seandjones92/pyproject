#!/usr/bin/env python

import click
import re

from pyproject import templatebuilder


@click.group()
@click.pass_context
def entrypoint(helpflag):
    """Create and manage Python CLI projects."""
    pass


@click.group()
@click.pass_context
def create(name):
    """Create a project skeleton."""
    pass


@click.command()
@click.argument('name')
def cli(name):
    """Create a cli project skeleton.

    Pass a string to be the name of the project created.
    """
    projectskel = templatebuilder.skelbuilder(name, "cli")
    projectskel.createskel()


@click.command()
@click.argument('name')
def curses(name):
    """Create an ncurses project skeleton.

    Pass a string to be the name of the project created.
    """
    projectskel = templatebuilder.skelbuilder(name, "curses")
    projectskel.createskel()


@click.command()
@click.argument('name')
def gui(name):
    """Create an ncurses project skeleton.

    Pass a string to be the name of the project created.
    """
    print("Create an gui project named " + name)


@click.command()
@click.argument('number')
def version(number):
    """Set the version of the current project.

    Pass a number to indicate the new version of the project.
    For example: 1.2
    """

    # setup regex patterns and version strings for files to change
    setuplocation = 'setup.py'
    setupversion = 'version="' + number + '"'
    setuppattern = 'version=".*"'

    snaplocation = 'snap/snapcraft.yaml'
    snapversion = 'version: \'' + number + '\''
    snappattern = 'version: \'.*\''

    # build a list of the above information to make iteration easier
    versionlisting = []
    versionlisting.append([setuplocation, setupversion, setuppattern])
    versionlisting.append([snaplocation, snapversion, snappattern])

    # iterate through the above list and apply the version change
    for i in versionlisting:
        workingfile = open(i[0], 'rt')
        filedata = workingfile.read()
        workingfile.close()
        filedata = re.sub(i[2], i[1], filedata)
        workingfile = open(i[0], 'wt')
        workingfile.write(filedata)
        workingfile.close()


entrypoint.add_command(create)
entrypoint.add_command(version)

create.add_command(cli)
create.add_command(curses)
create.add_command(gui)
