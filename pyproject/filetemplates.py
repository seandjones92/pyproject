from string import Template

def templates(name):
    """Get a list of all the file templates.
    
    Pass the `name` variable to help construct file paths.

    Returns a list of lists, the first element of each embedded list is the
    file content, the second element is the filepath the resulting file should
    be written to.
    """
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

    binpath = "bin/" + name
    bincontent = Template('''\
#!/usr/bin/env python3

"""Entry point for $project."""

import $project
$project.entrypoint()
''').substitute({'project': name})

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

    gitignorepath = ".gitignore"
    gitignorecontent = Template('''\
# Project files for vscode that don't need tracking
.vscode/settings.json
.vscode/.ropeproject/*

# Files built by snapcraft
*.snap

# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class
*.pyc

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
pip-wheel-metadata/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# PEP 582; used by e.g. github.com/David-OConnor/pyflow
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/        
''').substitute({'project': name})


    templatelist.append([bincontent, binpath])
    templatelist.append([pipenvcontent, pipenvpath])
    templatelist.append([pythoncontent, pythonpath])
    templatelist.append([setupcontent, setuppath])
    templatelist.append([snapcraftcontent, snapcraftpath])
    
    return templatelist