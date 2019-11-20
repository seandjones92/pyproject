#!/usr/bin/env python

import click
import os
import re
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
@click.option('-v', '--ver', prompt='Set project to this version number',
              help='Number to set the project version to. I.E. "1.0"')
def version(ver):
    """Set the version of the current project."""
    fin = open('setup.py', 'rt')
    setupdata = fin.read()
    fin.close()
    setupversion = 'version="' + ver + '"'
    setupdata = re.sub('version=".*"', setupversion, setupdata)
    fin = open('setup.py', 'wt')
    fin.write(setupdata)
    fin.close()


cli.add_command(create)
cli.add_command(version)
