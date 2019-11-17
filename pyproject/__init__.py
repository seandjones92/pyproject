#!/usr/bin/env python

import click
import os
import subprocess
from string import Template

@click.command()
def cli(name):
    """Setup a python project."""
#     os.mkdir(name)
#     os.chdir(name)

#     subprocess.run(["pipenv", "install", "--dev", "pylint", "rope", "autopep8", "bpython"])
#     subprocess.run(["pipenv", "install", "Click"])

#     setuptemplate = Template('''\
#     #!/usr/bin/env python3
#     from setuptools import setup, find_packages
#     setup(
#         name="$project",
#         version="0.1",
#         packages=find_packages(),
#         include_package_data=True,
#         install_requires=[ # Add dependencies as a list here
#             'Click',
#         ],
#         entry_points=\'\'\'
#             [console_scripts]
#             $project=$project:cli
#         \'\'\'
#     )
#     ''')

#     snapcrafttemplate = Template('''\
# name: $project # you probably want to 'snapcraft register <name>'
# base: core18 # the base snap is the execution environment for this snap
# version: '0.1' # just for humans, typically '1.2+git' or '1.3.2'
# summary: Check all sorts of hosts and services and get reporting.
# description: |
#   This is my-snap's description. You have a paragraph or two to tell the
#   most important story about your snap. Keep it under 100 words though,
#   we live in tweetspace and your description wants to look good in the snap
#   store.

# grade: devel # must be 'stable' to release into candidate/stable channels
# confinement: devmode # use 'strict' once you have the right plugs and slots

# parts:
#   my-part:
#     # See 'snapcraft plugins'
#     plugin: python
#     python-version: python3
#     source: .

# apps:
#   $project:
#     environment:
#       LC_ALL: C.UTF-8
#       LANG: C.UTF-8
#     command: bin/pyproject

#     ''')

#     with open("setup.py", 'w') as setupfile:
#         setupcontent = setuptemplate.substitute({'project': name})
#         setupfile.write(setupcontent)
    
#     os.mkdir('snap')
#     with open("snap/snapcraft.yaml")) as snapcraftfile:
#         snapcraftcontent = snapcrafttemplate.substitute({'project': name})
    print("Hello World")