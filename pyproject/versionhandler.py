#!/usr/bin/env python

import os
import re


class versionhandler(object):
    """Provide methods for interacting with project version.
    """

    def __init__(self):
        """Get the currently set versions from the existing config.
        """
        os.chdir('/tmp/project')
        with open('setup.py') as workingfile:
            self.setupversion = re.findall(
                r'[0-9]*\.[0-9]*', workingfile.read())[0]

    def update(self, number):
        """Update the project version in all configuration files.

        Args:
            number (number): Version number to set in config files.
        """
        os.chdir('/tmp/project')
        # setup regex patterns and version strings for files to change
        setuplocation = 'setup.py'
        setupversion = 'version="' + number + '"'
        setuppattern = 'version=".*"'

        # build a list of the above information to make iteration easier
        versionlisting = []
        versionlisting.append([setuplocation, setupversion, setuppattern])

        # iterate through the above list and apply the version change
        for i in versionlisting:
            workingfile = open(i[0], 'rt')
            filedata = workingfile.read()
            workingfile.close()
            filedata = re.sub(i[2], i[1], filedata)
            workingfile = open(i[0], 'wt')
            workingfile.write(filedata)
            workingfile.close()
