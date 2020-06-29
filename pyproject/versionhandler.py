#!/usr/bin/env python

import re


class versionhandler(object):

    def __init__(self):
        with open('setup.py') as workingfile:
            self.setupversion = re.findall(
                r'[0-9]*\.[0-9]*', workingfile.read())[0]
        with open('snap/snapcraft.yaml') as workingfile:
            self.snapversion = re.findall(
                r'[0-9]*\.[0-9]*', workingfile.read())[0]

    def update(self, number):
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

    def get(self):
        print("setup.py version: \t" + self.setupversion)
        print("snapcraft version: \t" + self.snapversion)
