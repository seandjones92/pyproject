## Install

```
alias pyproject="podman run --rm --userns keep-id -v $PWD:/tmp/project:Z --security-opt label=disable localhost/pyproject:latest python /usr/local/bin/pyproject"
```

## My Todo
- [ ] create tests for this project
- [ ] project skeletons should have a dummy test added
- [ ] write a legit readme
