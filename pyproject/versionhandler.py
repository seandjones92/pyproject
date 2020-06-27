>#!/usr/bin/env python

class versionhandler(object):
    
    def __init__(self):
        pass

    def update(self, number):
        # setup regex patterns and version strings for files to change
        self.setuplocation = 'setup.py'
        self.setupversion = 'version="' + number + '"'
        self.setuppattern = 'version=".*"'

        self.snaplocation = 'snap/snapcraft.yaml'
        self.snapversion = 'version: \'' + number + '\''
        self.snappattern = 'version: \'.*\''

        # build a list of the above information to make iteration easier
        self.versionlisting = []
        self.versionlisting.append([setuplocation, setupversion, setuppattern])
        self.versionlisting.append([snaplocation, snapversion, snappattern])
        # iterate through the above list and apply the version change
        for i in versionlisting:
            workingfile = open(i[0], 'rt')
            filedata = workingfile.read()
            workingfile.close()
            filedata = re.sub(i[2], i[1], filedata)
            workingfile = open(i[0], 'wt')
            workingfile.write(filedata)
            workingfile.close()
