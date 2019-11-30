# pyproject

TODO:
- refactor so that the `cli` function in `__init__.py` is something like `commandentry`
- breakout create command for different types of apps (e.g pyproject create cli/gui/ncurses projectname)
- pyproject should create a `.gitignore`
- create tests for this project
- create initial test for projects that pyproject creates
- create debug config for vscode
- create debug config for ts created by pyproject
- get the application to work without --devmode when installed as a snap
    - this will mean that snap interfaces will need to be configured
    - since this will need access to potentially any location of the users home directory it may need "classic" confinement, see if we can avoid s