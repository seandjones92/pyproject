#!/usr/bin/env python3

import os

from pyproject import templates


class skelbuilder(object):
    """Build out the skeleton for the project type given"""

    def __init__(self, name, projtype):
        """build the skeleton files"""
        
        self.name = name
        self.projtype = projtype
        self.commonfiles = templates.common.createTemplates(name)

        if projtype == "cli":
            self.typefiles = templates.cli.createTemplates(name)

    def filewriter(self, filelist):
        """write the files to disk"""

        for i in filelist:
            filelocation = i[0]
            filecontent = i[1]
            with open(filelocation, "w") as skelfile:
                skelfile.write(filecontent)

    def createskel(self):
        """high level create function"""

        os.mkdir(self.name)
        os.chdir(self.name)
        os.mkdir(self.name)
        os.mkdir('bin')
        os.mkdir('snap')

        self.filewriter(self.commonfiles)
        self.filewriter(self.typefiles)