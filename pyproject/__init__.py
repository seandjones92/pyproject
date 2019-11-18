#!/usr/bin/env python

import click
import os
from string import Template

@click.command()
@click.option('-n', '--name', prompt='Project name')
def cli(name):
    """Setup a python project."""
    os.mkdir(name)
    os.chdir(name)

    pipenvtemplate = Template('''\
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
''')

    setuptemplate = Template('''\
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
        $project=$project:cli
    \'\'\'
)
''')

    snapcrafttemplate = Template('''\
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

''')

    bintemplate = Template('''\
#!/usr/bin/env python3

import $project
$project.cli()
''')

    pythontemplate = Template('''\
#!/usr/bin/env python

import click

@click.command()
def cli(name):
    print("Hello World!")
''')

    os.mkdir('bin')
    binfilelocation = "bin/" + name
    with open(binfilelocation, "w") as binfile:
      binfilecontent = bintemplate.substitute({'project': name})
      binfile.write(binfilecontent)

    os.mkdir(name)
    pythonfilelocation = name + "/__init__.py"
    with open(pythonfilelocation, "w") as pythonfile:
      pythonfilecontent = pythontemplate.template
      pythonfile.write(pythonfilecontent)

    with open("Pipfile", "w") as pipenvfile:
        pipenvcontent = pipenvtemplate.template
        pipenvfile.write(pipenvcontent)

    with open("setup.py", 'w') as setupfile:
        setupcontent = setuptemplate.substitute({'project': name})
        setupfile.write(setupcontent)

    os.mkdir('snap')
    with open("snap/snapcraft.yaml", 'w') as snapcraftfile:
        snapcraftcontent = snapcrafttemplate.substitute({'project': name})
        snapcraftfile.write(snapcraftcontent)