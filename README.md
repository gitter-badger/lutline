# LUTLINE

Provides a method of generating a look-up table (LUT) based on a CLI
specification and a method of accessing said LUT when parsing an array
of strings (in most programming languages, this array is known as "argv").

## Install

Install lutline from PyPI with:

```
$ pip install lutline
```

## Development

### Test
Test lutline using:

```
$ python -m tests
```

### Deployment

Deploy to PyPI with:

```
$ python setup.py sdist bdist_wheel
$ twine upload dist/*
```
