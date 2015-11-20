## Structure

The *specfile* is a simple text file divided in three parts:

* a Commad-Line Interface (CLI) specification
* (optional) a usage message
* (optional) a description of the usage message

The CLI specification is the core of the *specfile* and is where the developer
provides the pattern that is to be implemented by the CLI parser. This part of
the *specfile* describes a tree where each leaf is an *element* and each
branch is a *relation*.

## Elements

Currently, there are two elements supported by *lutline*:

| *specfile* | Pattern representation | Received in `argv` | Type |
|------------|------------------------|--------------------|------|
| `explicit {label}` | `"%s" % label` | label | Boolean |
| `implicit {label}` | `"<%s>" % label` | value | String |

The explicit element is a boolean variable that appears in the dictionary
like structure returned from the CLI parsing operation, with a key equal to
its label. True means that the elements exists in `argv`.

The implicit element is a string variable that appears in the dictionary
like structure returned from the CLI parsing operation, with a key equal to
its label. This element is not directly recognizable from `argv` since
the user places a string value in there, instead of the label.

## Relations

Currently, there are four relations supported by *lutline*:

| *specfile* | Pattern representation |
|------------|------------------------|
| `required` | `"( children[0] children[1] (...) children[n] )"` |
| `optional` | `"[ children[0] children[1] (...) children[n] ]` |
| `exclusive` | `children[0] `&verbar;` children[1] `&verbar;` (...)`&verbar;` children[n]` |
| `unordered` | `{ children[0] children[1] (...) children[n] }` |

As you can see, these relations are similar to the ones provided by
[docopt](http://docopt.org), except for `unordered`.

## Example 1 - docker commit

In this first example, a simplified version of the `docker commit` command
will be transcribed to a *lutline*'s *specfile*.

    SPEC
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

    USAGE
    Usage:  docker commit [OPTIONS] <container> [<repository>]

    DESCRIPTION
    Create a new image from a container's changes
      (-a | --author) <author>    Author (e.g., "John Hannibal Smith <hannibal@a-team.com>")
      (-c | --change) <changes>   Apply Dockerfile instruction to the created image
      --help                      Print usage
      (-m | --message) <message>  Commit message
      (-p | --pause)              Pause container during commit

## Future plans

In the future, the plans are to support a third element where explicit and
implicit elements are *mixed* in the same index of `argv`. For example,
the pattern `--time=<time>` can be defined in the *specfile* as:

    mixed:
        explicit --time=
        implicit time

For example, the pattern `(-t | --time)=<clock>` can be defined in the
*specfile* as:

    mixed:
        exclusive:
            explicit -t=
            explicit --time=
        implicit clock

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
        mixed:
            exclusive:
                explicit -t=
                explicit --time=
            implicit time
        required:
            flag time
            implicit time

Further, in the future the plans are to support the `atleastone` (at least
one) relation. In order to accomplish this objective it will be important
find a way of changing the look-up table (LUT) parser code that will allow to
perform this functionallity. A possibility is to create a different LUT for
each `atleastone` branch.

<br>

* Next: [Validating the non-ambiguoty of a pattern](validation.html)

<br>
