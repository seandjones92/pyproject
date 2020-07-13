#!/usr/bin/env python


import unittest
from unittest.mock import patch, call
from pyproject import templates, templatebuilder


class test_templates(unittest.TestCase):

    def test_common(self):
        controlgroup = []

        gitignorepath = ".gitignore"
        with open('./tests/templates/common/gitignorecontent') as workingfile:
            gitignorecontent = workingfile.read()

        controlgroup.append([gitignorepath, gitignorecontent])

        binpath = "bin/testproject"
        with open('./tests/templates/common/bincontent') as workingfile:
            bincontent = workingfile.read()

        controlgroup.append([binpath, bincontent])

        dockerignorepath = ".dockerignore"
        with open('./tests/templates/common/dockerignorecontent') as workingfile:
            dockerignorecontent = workingfile.read()

        controlgroup.append([dockerignorepath, dockerignorecontent])

        dockerfilepath = "Dockerfile"
        with open('./tests/templates/common/dockerfilecontent') as workingfile:
            dockerfilecontent = workingfile.read()

        controlgroup.append([dockerfilepath, dockerfilecontent])

        testgroup = templates.common.createTemplates('testproject')

        self.assertListEqual(controlgroup, testgroup,
                             msg="Control and Test templates should match")

    def test_cli(self):
        controlgroup = []

        pipenvpath = "Pipfile"
        with open('./tests/templates/cli/pipenvcontent') as workingfile:
            pipenvcontent = workingfile.read()

        controlgroup.append([pipenvpath, pipenvcontent])

        setuppath = "setup.py"
        with open('./tests/templates/cli/setupcontent') as workingfile:
            setupcontent = workingfile.read()

        controlgroup.append([setuppath, setupcontent])

        pythonpath = "testproject/__init__.py"
        with open('./tests/templates/cli/pythoncontent') as workingfile:
            pythoncontent = workingfile.read()

        controlgroup.append([pythonpath, pythoncontent])

        requirementspath = "requirements.txt"
        with open('./tests/templates/cli/requirementscontent') as workingfile:
            requirementscontent = workingfile.read()

        controlgroup.append([requirementspath, requirementscontent])

        testgroup = templates.cli.createTemplates('testproject')

        self.assertListEqual(controlgroup, testgroup,
                             msg="Control and Test templates should match")

    def test_curses(self):
        controlgroup = []

        pipenvpath = "Pipfile"
        with open('./tests/templates/curses/pipenvcontent') as workingfile:
            pipenvcontent = workingfile.read()

        controlgroup.append([pipenvpath, pipenvcontent])

        setuppath = "setup.py"
        with open('./tests/templates/curses/setupcontent') as workingfile:
            setupcontent = workingfile.read()

        controlgroup.append([setuppath, setupcontent])

        pythonpath = "testproject/__init__.py"
        with open('./tests/templates/curses/pythoncontent') as workingfile:
            pythoncontent = workingfile.read()

        controlgroup.append([pythonpath, pythoncontent])

        requirementspath = "requirements.txt"
        with open('./tests/templates/curses/requirementscontent') as workingfile:
            requirementscontent = workingfile.read()

        controlgroup.append([requirementspath, requirementscontent])

        testgroup = templates.curses.createTemplates('testproject')

        self.assertListEqual(controlgroup, testgroup,
                             msg="Control and Test templates should match")

    @patch('pyproject.templatebuilder.os')
    @patch('pyproject.templatebuilder.open')
    def test_skelbuildercli(self, mock_myopen, mock_myos):
        testskel = templatebuilder.skelbuilder('testproject', 'cli')
        testskel.createskel()
        controlarglist = [call('.gitignore', 'w'),
                          call('bin/testproject', 'w'),
                          call('.dockerignore', 'w'),
                          call('Dockerfile', 'w'),
                          call('Pipfile', 'w'),
                          call('setup.py', 'w'),
                          call('testproject/__init__.py', 'w'),
                          call('requirements.txt', 'w')]
        self.assertListEqual(mock_myopen.call_args_list,
                             controlarglist, msg="Lists should be the same")


    @patch('pyproject.templatebuilder.os')
    @patch('pyproject.templatebuilder.open')
    def test_skelbuildercurses(self, mock_myopen, mock_myos):
        testskel = templatebuilder.skelbuilder('testproject', 'curses')
        testskel.createskel()
        controlarglist = [call('.gitignore', 'w'),
                          call('bin/testproject', 'w'),
                          call('.dockerignore', 'w'),
                          call('Dockerfile', 'w'),
                          call('Pipfile', 'w'),
                          call('setup.py', 'w'),
                          call('testproject/__init__.py', 'w'),
                          call('requirements.txt', 'w')]
        self.assertListEqual(mock_myopen.call_args_list,
                             controlarglist, msg="Lists should be the same")