#!/usr/bin/env python

import click

from pyproject import templatebuilder


@click.group()
@click.pass_context
def entrypoint(helpflag):
    """Create and manage Python CLI projects.
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


entrypoint.add_command(cli)
entrypoint.add_command(curses)
