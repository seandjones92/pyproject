#!/usr/bin/env python3

from string import Template


def createTemplates(name):
    """Return a list of file templates used for ncurses projects.

    Pass `name` as string to help construct file paths and for use with
    template variables.

    Returns a list of lists, the first element of each embedded list is the path
    the resulting file should be written to, the second element is the file
    content.
    """

    # Create empty list to hold nested lists
    templatelist = []

    pipenvpath = "Pipfile"
    pipenvcontent = Template('''\
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"

[packages]

[dev-packages]
pylint = "*"
rope = "*"
autopep8 = "*"
bpython = "*"

[requires]
python_version = "3.7"
''').substitute({'project': name})
    templatelist.append([pipenvpath, pipenvcontent])

    setuppath = "setup.py"
    setupcontent = Template('''\
#!/usr/bin/env python3
from setuptools import setup, find_packages
setup(
    name="$project",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    entry_points=\'\'\'
        [console_scripts]
        $project=$project:entrypoint
    \'\'\'
)
''').substitute({'project': name})
    templatelist.append([setuppath, setupcontent])

    pythonpath = name + "/__init__.py"
    pythoncontent = Template('''\
#!/usr/bin/env python

import curses


def entrypoint():
    """Prints 'Hello World!'

    Replace this with your cursesexample logic.
    """
    screen = curses.initscr()
    screen.clear()
    screen.border(0)
    screen.addstr(10, 30, "Hello World!")

    screen.refresh()
    opt = screen.getch()
    curses.endwin()
''').substitute({'project': name})
    templatelist.append([pythonpath, pythoncontent])

    return templatelist