#!/usr/bin/env python

import os

from pyproject import templates


class skelbuilder(object):
    """Build out the skeleton for the project type given.
    """

    def __init__(self, name, projtype):
        """Create skeleton files from template.
        """

        self.name = name
        self.projtype = projtype
        self.commonfiles = templates.common.createTemplates(name)

        if projtype == "cli":
            self.typefiles = templates.cli.createTemplates(name)
        elif projtype == 'curses':
            self.typefiles = templates.curses.createTemplates(name)

    def filewriter(self, filelist):
        """Write the files to disk.
        """

        for i in filelist:
            filelocation = i[0]
            filecontent = i[1]
            with open(filelocation, "w") as skelfile:
                skelfile.write(filecontent)

    def createskel(self):
        """Write the folder structure to disk.
        """

        os.chdir('/tmp/project')
        os.mkdir(self.name)
        os.chdir(self.name)
        os.mkdir(self.name)
        os.mkdir('bin')

        self.filewriter(self.commonfiles)
        self.filewriter(self.typefiles)
