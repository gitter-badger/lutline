# LUTLINE

Parse `argv` using a look-up table generated from your command-line interface specification.

Checkout [http://ffunenga.github.io/lutline](http://ffunenga.github.io/lutline) for more information.

## Install

Install lutline from PyPI with:

```
$ pip install lutline
```

## Development

### Test

Run lutline command-line tool without `setup.py`:
```
$ python -m lutline.main
```

Run tests:

```
$ python -m unittest -v
```

### Deployment

Deploy to PyPI with:

```
$ python setup.py sdist bdist_wheel
$ twine upload dist/*
```
