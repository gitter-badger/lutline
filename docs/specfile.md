Command-line interface specification
## Structure

The *specfile* is a simple text file divided in three parts:

* a Command-Line Interface (CLI) specification
* (optional) a usage message
* (optional) a description message

The CLI specification is the core of the *specfile* and is where the developer
provides the pattern that is to be implemented by the CLI parser. This part of
the *specfile* describes a tree where each leaf is an *element* and each
branch is a *relation*.

The *lutline* parser assumes that the *specfile* first describes the CLI
specification and then, optionally, describes the usage and description
messages, where the first line of that block starts with the sub-string
`usage:`. This search operation is not sensible to the capitalization
(e.g. `Usage` and `USAGE` also match).

If no line in the *specfile* verifies
`line.lower().startswith('usage:')`, than the entire file's
contents are identified as the CLI specification. On the contrary, if one
line verifies that condition, than the contents starting from that line are
considered to describe the usage and description messages.

The optional description message starts from the first line without any
indentation after the `usage:` line.

## Elements

Currently, there are two elements supported by *lutline*:

| *specfile* | Pattern representation | Received in `argv` | Type |
|------------|------------------------|--------------------|------|
| `explicit {label}` | `"%s" % label` | label | Boolean |
| `implicit {label}` | `"<%s>" % label` | value | String |

An explicit element is represented in `argv` with its label. On the contrary,
an implicit element is not directly recognizable in `argv`, since
the user places a string value in there, instead of its label.

## Relations

Currently, there are four relations supported by *lutline*:

| *specfile* | Pattern representation |
|------------|------------------------|
| `required` | `"( children[0] children[1] (...) children[n] )"` |
| `optional` | `"[ children[0] children[1] (...) children[n] ]` |
| `exclusive` | `( children[0] `&verbar;` children[1] `&verbar;` (...)`&verbar;` children[n] )` |
| `unordered` | `{ children[0] children[1] (...) children[n] }` |

As you can see, these relations are common, except for `unordered`.

<span class="label label-success">Required</span> Defines an ordered set of
branches or elements. This relation has one embodiment: its children in the
same order they appear in the pattern representation. For example, the
following CLI specification:

    required:
        explicit -f
        implicit input_file

    Usage: app.py (-f <input_file>)

has the following embodiment:

1. `app.py -f <input_file>`

<span class="label label-success">Optional</span> Equivalent to a `required`
branch with two possible embodiments: either with the normal `required`
embodiment, OR by not existing in the parent branch. For example, the
following CLI specification:

    optional:
        explicit -f
        implicit input_file

    Usage: app.py [-f <input_file>]

has the following embodiments:

1. `app.py -f <input_file>`
2. `app.py`

<span class="label label-success">Exclusive</span> Defines a set of branches
or elements that is embodied one child at a time. For example, the following
CLI specification:

    exclusive:
        explicit -f
        implicit input_file

    Usage: app.py (-f | <input_file>)

has the following embodiments:

1. `app.py -f`
2. `app.py <input_file>`

<span class="label label-success">Unordered</span> Defines a set of branches
or elements that is embodied by each permutation of the children. For
example, the following CLI specification:

    unordered:
        explicit -f
        implicit input_file

    Usage: app.py {-f | <input_file>}

has the following embodiments:

1. `app.py -f <input_file>`
2. `app.py <input_file> -f`

## Example 1 - docker commit

In this first example, a simplified version of the `docker commit` command
will be transcribed to a *lutline*'s *specfile*.

    required:
        explicit commit
        unordered:
            optional:
                required:
                    exclusive:
                        explicit -a
                        explicit --author
                    implicit author
            optional:
                required:
                    exclusive:
                        explicit -c
                        explicit --change
                    implicit changes
            optional:
                explicit --help
            optional:
                required:
                    exclusive:
                        explicit -m
                        explicit --message
                    implicit message
            optional:
                exclusive:
                    explicit -p
                    explicit --pause
        implicit container
        optional:
            implicit repository_tag

    Usage:  docker commit [OPTIONS] <container> [<repository>]

    Create a new image from a container's changes
      (-a | --author) <author>    Author (e.g., "John Hannibal Smith <hannibal@a-team.com>")
      (-c | --change) <changes>   Apply Dockerfile instruction to the created image
      --help                      Print usage
      (-m | --message) <message>  Commit message
      (-p | --pause)              Pause container during commit

The `Usage:` marker shows a simplified pattern using the `[OPTIONS]`
representation. This pattern code entails that any of the options can be
optionally placed at that location in any order. This type of relation
greatly increases the number of embodiments.

## Future plans

<span class="label label-primary">TODO</span>
In the future, the plans are to support a third element where explicit and
implicit elements are *mixed* in the same index of `argv`. For example,
the pattern `--time=<time>` can be defined in the *specfile* as:

    element:
        explicit --time=
        implicit time

For example, the pattern `(-t | --time)=<clock>` can be defined in the
*specfile* as:

    element:
        exclusive:
            explicit -t=
            explicit --time=
        implicit clock

<span class="label label-primary">TODO</span>
Also, in the future the plans are to support aliases. For example when the
following element appears on the *specfile*:

    flag time

it is converted to:

    exclusive:
        explicit -t
        explicit --time

Or, for example, when the following element appears on the *specfile*:

    option time

it is converted to:

    exclusive:
        element:
            exclusive:
                explicit -t=
                explicit --time=
            implicit time
        required:
            flag time
            implicit time

<span class="label label-primary">TODO</span>
Further, in the future the plans are to support the `atleastone` ("at least
one") relation. In order to accomplish this objective it will be important
find a way of changing the look-up table (LUT) parser code that will allow to
perform this functionality. A possibility is to create a different LUT for
each `atleastone` branch.
