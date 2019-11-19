from string import Template

def templates(name):
    """Get a list of all the file templates.
    
    Pass the `name` variable to help construct file paths.
    """
    templatelist = []

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

"""Entry point for $project."""

import $project
$project.cli()
''')

    pythontemplate = Template('''\
#!/usr/bin/env python

import click

@click.command()
def cli():
    """Prints 'Hello World!'
    
    Replace this with your $project logic.
    """
    print("Hello World!")
''')

    templatelist.append([bintemplate, str("bin/" + name)])
    templatelist.append([pipenvtemplate, "Pipenv"])
    templatelist.append([pythontemplate, str(name + "/__init__.py")])
    templatelist.append([setuptemplate, "setup.py"])
    templatelist.append([snapcrafttemplate, "snap/snapcraft.yaml"])
    
    return templatelist