#!/usr/bin/env python

import click

from pyproject import templatebuilder
from pyproject import versionhandler


@click.group()
@click.pass_context
def entrypoint(helpflag):
    """Create and manage Python CLI projects.
    """
    pass


@click.group()
@click.pass_context
def create(name):
    """Create a project skeleton.
    """
    pass


@click.command()
@click.argument('name')
def cli(name):
    """Create a cli project skeleton.

    Args:
        name (string): Name of the project to be created
    """
    projectskel = templatebuilder.skelbuilder(name, "cli")
    projectskel.createskel()


@click.command()
@click.argument('name')
def curses(name):
    """Create a curses project skeleton.

    Args:
        name (string): Name of the project to be created
    """
    projectskel = templatebuilder.skelbuilder(name, "curses")
    projectskel.createskel()


@click.group()
@click.pass_context
def version(number):
    """Handle versioning of the project.
    """
    pass


@click.command()
@click.argument('number')
def update(number):
    """Set the new project version.

    Args:
        number (float): Number to set the project version to
    """
    vhobject = versionhandler.versionhandler()
    vhobject.update(number)


@click.command()
def get():
    """Print the project version information.
    """
    vhobject = versionhandler.versionhandler()
    print("setup.py version: \t" + vhobject.setupversion)


entrypoint.add_command(create)
entrypoint.add_command(version)

create.add_command(cli)
create.add_command(curses)

version.add_command(get)
version.add_command(update)
