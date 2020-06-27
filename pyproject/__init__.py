#!/usr/bin/env python

import click

from pyproject import templatebuilder
from pyproject import versionhandler


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
    vhobject = versionhandler.versionhandler()
    vhobject.update(number)


entrypoint.add_command(create)
entrypoint.add_command(version)

create.add_command(cli)
create.add_command(curses)
create.add_command(gui)
