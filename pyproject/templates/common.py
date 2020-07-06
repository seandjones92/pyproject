#!/usr/bin/env python3

from string import Template


def createTemplates(name):
    """Return a list of file templates common to all project types.

    Pass `name` as string to help construct file paths and for use with
    template variables.

    Returns a list of lists, the first element of each embedded list is the
    path the resulting file should be written to, the second element is the
    file content.
    """

    # Create empty list to hold nested lists
    templatelist = []

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
*py.class
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
    templatelist.append([gitignorepath, gitignorecontent])

    binpath = "bin/" + name
    bincontent = Template('''\
#!/usr/bin/env python3

"""Entry point for $project."""

import $project
$project.entrypoint()
''').substitute({'project': name})
    templatelist.append([binpath, bincontent])

    dockerignorepath = ".dockerignore"
    dockerignorecontent = Template('''\
**/__pycache__
**/.classpath
**/.dockerignore
**/.env
**/.git
**/.gitignore
**/.project
**/.settings
**/.toolstarget
**/.vs
**/.vscode
**/*.*proj.user
**/*.dbmdl
**/*.jfm
**/azds.yaml
**/charts
**/docker-compose*
**/Dockerfile*
**/node_modules
**/npm-debug.log
**/obj
**/secrets.dev.yaml
**/values.dev.yaml
README.md
''').substitute({'project': name})
    templatelist.append([dockerignorepath, dockerignorecontent])

    dockerfilepath = "Dockerfile"
    dockerfilecontent = Template('''\
# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install pip requirements
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
ADD . /app
RUN pip install -e . 

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "bin/$project"]
''').substitute({'project': name})
    templatelist.append([dockerfilepath, dockerfilecontent])


    return templatelist
