#!/usr/bin/env python

import click
import os
from string import Template

from pyproject import filetemplates


@click.group()
@click.pass_context
def cli(versionflag):
    """Create and manage Python CLI projects."""
    pass


@click.command()
@click.option('-n', '--name', prompt='Project name',
              help="Name used for project and executable")
def create(name):
    """Create a project skeleton."""

    os.mkdir(name)
    os.chdir(name)
    os.mkdir(name)
    os.mkdir('bin')
    os.mkdir('snap')

    templatelist = filetemplates.templates(name)

    for i in templatelist:
        filecontent = i[0].substitute({'project': name})
        filelocation = i[1]
        with open(filelocation, "w") as skelfile:
            skelfile.write(filecontent)


@click.command()
def version():
    """Set the version of the current project."""
    print('''
    This will eventually set the version in both the "setup.py" and "snapcraft.yaml" files.
    ''')


cli.add_command(create)
cli.add_command(version)
