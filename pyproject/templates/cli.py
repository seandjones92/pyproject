#!/usr/bin/env python3

from string import Template

def createTemplates(name):
    """Return a list of file templates used for cli projects.

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

    snapcraftpath = "snap/snapcraft.yaml"
    snapcraftcontent = Template('''\
name: $project # you probably want to 'snapcraft register <name>'
base: core18 # the base snap is the execution environment for this snap
version: '0.1' # just for humans, typically '1.2+git' or '1.3.2'
summary: Single-line elevator pitch for your amazing snap # 79 char long summary
description: |
  This is my-snap's description. You have a paragraph or two to tell the
  most important story about your snap. Keep it under 100 words though,
  we live in tweetspace and your description wants to look good in the snap
  store.

grade: devel # must be 'stable' to release into candidate/stable channels
confinement: devmode # use 'strict' once you have the right plugs and slots

parts:
  my-part:
    # See 'snapcraft plugins'
    plugin: python
    python-version: python3
    source: .

apps:
  $project:
    environment:
      LC_ALL: C.UTF-8
      LANG: C.UTF-8
    command: bin/$project

''').substitute({'project': name})
    templatelist.append([snapcraftpath, snapcraftcontent])

    binpath = "bin/" + name
    bincontent = Template('''\
#!/usr/bin/env python3

"""Entry point for $project."""

import $project
$project.entrypoint()
''').substitute({'project': name})
    templatelist.append([binpath, bincontent])

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
