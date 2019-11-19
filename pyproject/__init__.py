#!/usr/bin/env python

import click
import os
from string import Template

from pyproject import filetemplates


@click.command()
@click.option('-n', '--name', prompt='Project name',
              help="Name used for project and executable")
def cli(name):
    """Create and manage Python CLI projects."""
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
