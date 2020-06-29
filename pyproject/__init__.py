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


@click.group()
@click.pass_context
def version(number):
    """Handle versioning of the project."""
    pass

@click.command()
@click.argument('number')
def update(number):
    """Set the new project version

    Pass a number be set as the project version.
    """
    vhobject = versionhandler.versionhandler()
    vhobject.update(number)


@click.command()
def get():
    vhobject = versionhandler.versionhandler()
    vhobject.get()


entrypoint.add_command(create)
entrypoint.add_command(version)

create.add_command(cli)
create.add_command(curses)

version.add_command(get)
version.add_command(update)
