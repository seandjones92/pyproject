#!/usr/bin/env python

import click
import os
import re
from string import Template

from pyproject import filetemplates


@click.group()
@click.pass_context
def cli(helpflag):
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
        filecontent = i[0].substitute({'project': name}) # TODO: this should be in the filetemplates.py file
        filelocation = i[1]
        with open(filelocation, "w") as skelfile:
            skelfile.write(filecontent)


@click.command()
@click.option('-n', '--number', prompt='Set project to this version number',
              help='Number to set the project version to. I.E. "1.0"')
def version(number):
    """Set the version of the current project."""

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

cli.add_command(create)
cli.add_command(version)
