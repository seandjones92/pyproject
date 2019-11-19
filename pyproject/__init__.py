#!/usr/bin/env python

import click
import os
from string import Template

from pyproject import filetemplates


@click.group()
@click.pass_context
def cli():
    """Create and manage Python CLI projects."""
    pass


@click.command()
@click.option('-n', '--name', prompt='Project name',
              help="Name used for project and executable")
def create(name):
    """Create a project skeleton."""

    os.mkdir(name)
    os.chdir(name)

    os.mkdir('bin')
    binfilelocation = "bin/" + name
    with open(binfilelocation, "w") as binfile:
        binfilecontent = filetemplates.bintemplate.substitute(
            {'project': name})
        binfile.write(binfilecontent)

    os.mkdir(name)
    pythonfilelocation = name + "/__init__.py"
    with open(pythonfilelocation, "w") as pythonfile:
        pythonfilecontent = filetemplates.pythontemplate.template
        pythonfile.write(pythonfilecontent)

    with open("Pipfile", "w") as pipenvfile:
        pipenvcontent = filetemplates.pipenvtemplate.template
        pipenvfile.write(pipenvcontent)

    with open("setup.py", 'w') as setupfile:
        setupcontent = filetemplates.setuptemplate.substitute(
            {'project': name})
        setupfile.write(setupcontent)

    os.mkdir('snap')
    with open("snap/snapcraft.yaml", 'w') as snapcraftfile:
        snapcraftcontent = filetemplates.snapcrafttemplate.substitute({
                                                                      'project': name})
        snapcraftfile.write(snapcraftcontent)

@click.command()
def version():
    """Set the version of the current project."""
    print('''
    This will eventually set the version in both the "setup.py" and "snapcraft.yaml" files.
    ''')

cli.add_command(create)
cli.add_command(version)
