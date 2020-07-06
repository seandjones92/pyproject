#!/usr/bin/env python3

from string import Template


def createTemplates(name):
    """Return a list of file templates used for cli projects.

    Pass `name` as string to help construct file paths and for use with
    template variables.

    Returns a list of lists, the first element of each embedded list is the
    path the resulting file should be written to, the second element is the
    file content.
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
click = "*"

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
    install_requires=[ # Add dependencies as a list here
        'Click',
    ],
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

import click

@click.command()
def entrypoint():
    """Prints 'Hello World!'

    Replace this with your $project logic.
    """
    print("Hello World!")
''').substitute({'project': name})
    templatelist.append([pythonpath, pythoncontent])

    requirementspath = "requirements.txt"
    requirementscontent = Template('''\
-i https://pypi.python.org/simple
click==7.1.2
''').substitute({'project': name})
    templatelist.append([requirementspath, requirementscontent])

    return templatelist
