This analysis compares a sample command-line python modules. They can
be found through the following sources:

- [PyPI](https://pypi.python.org/pypi?%3Aaction=search&term=cli&submit=search)
- [Python Guide](http://docs.python-guide.org/en/latest/scenarios/cli/)
- [Github](https://github.com/search?l=Python&q=cli&ref=searchresults&type=Repositories&utf8=%E2%9C%93)


## Number of non-empty lines of code

This indicator shows an approximation of the amount of third party
code that an import statement, such as `import <3rd_party_module>`, pulls
into your application.

| lutline | docopt | compago | Plac | argparse | Click |
| --- | --- | --- | --- | --- | --- | --- |
| 14 | 473 | 639 | 1352 | 1942 | 5745 |

Caution is advised when comparing these numbers. A reference is herein made to
[an Wikipedia article](https://en.wikipedia.org/wiki/Source_lines_of_code#Usage_of_SLOC_measures)
explaining some particularities.

Solutions with a similar amount of non-empty lines of code are difficult to
compare. Oftentimes, there is the possibility to rewrite readable segments
of code occupying more than one line, into a single, but harder to understand,
line of code. As such, it is not reasonable to make a technical comparison
based on these results, when two solutions have the same order of
magnitude, for example *docopt* vs *compago* or *Plac* vs *argparse*.

However, the same cannot be said when different orders of magnitude are
compared, for example *docopt* vs *argparse* (4 times less code) or *compago*
vs *Click* (9 times less code).

Currently, *lutline* uses 14 non-empty lines of Python code.

## Memory pollution

This indicator shows an approximation of the amount of memory (in MBs) that
gets allocated when using third party code.

| CLI specification | lutline | docopt | compago | Plac | argparse | Click |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `[-f <fout>] <fin>` | 0.09 | 0.21 | 4.19 | 11.31 | 3.34 | 1.82 |

## Processing time

This indicator shows an approximation of the time (in ms) it takes to parse
the command-line arguments while using third party code.

| CLI specification | lutline | docopt | compago | Plac | argparse | Click |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `[-f <fout>] <fin>` | 0.87 | 4.59 | 60.61 | 94.81 | 20.16 | 19.90 |

There was some difficulty in implementing the same command-line specification
in all the modules, except for *docopt*. The main problem is the need to
re-learn the programming interface for each solution.

Starting from one simple command-line specification, *lutline* proves to be
the best solution, always showing the lowest levels of resource usage.
