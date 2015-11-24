Parsing a command-line
Nowadays, most programming languages provide Command-Line Interface (CLI)
parser modules that allow the developer to implement a CLI specification
in the beginning of a program's run-time. Besides the standard modules
that come pre-bundled with the programming language, there are many other
known third-party modules. Some try to expand the possibilities and options
available to the developer. Others try to simplify the process for
developing a CLI specification.

Every time an application configured with other CLI parsers is executed by a
user, it requires the CLI specification to be parsed, instantiated and, only
then, matched against `argv`. These operations happen over and over again,
each time a user executes your application. For example, see
[argparse](http://docs.python.org/3/library/argparse.html) where the CLI
parser is fully instantiated each time you run your application.

*Lutline* solves this problem by generating a look-up table (LUT) that
anticipates all possible inputs from the user. As such, when a user runs your
application only one step occurs: matching the input from `argv` with your
pattern.

## CLI Specification &hArr; Pattern description

A CLI specification is merely a description of a pattern. For example, the
pattern `./app [-f] <input>` has one optional flag followed by a mandatory
argument. This pattern only matches the following two embodiments:

1. `./app <input>`
2. `./app -f <input>`

This type of decomposition is a great tool to look at CLI specifications from
a different perspective and find new sub-problems, such as ambiguity or
the order of elements in a pattern.

## Ambiguity

Any CLI specification with a finite number of embodiments can be decomposed
in a fashion similar to the previous list. A more complex example can be
achieved with the following pattern: `./app [<filein>] [<fileout>]`.
This pattern matches the following embodiments:

1. `./app`
2. `./app <filein> <fileout>`
3. `./app <filein>` &nbsp;&nbsp;&larr; <span class="glyphicon glyphicon-eye-open"></span>
4. `./app <fileout>` &nbsp;&nbsp;&larr; <span class="glyphicon glyphicon-eye-open"></span>

If we take a closer look to these embodiments, wee see that numbers 3 and 4
are problematic since on `argv` they will not be different from each other.
A strict parser cannot correctly guess if `./app file.txt` should set
`file.txt` to `filein` or to `fileout`. Hence, in these circumstances, the
method should consider that this scenario results from an ambiguous pattern,
which allows different embodiments to match the same input.

This problem relates, mainly, to the fact that arguments, such as `<fin>` or
`<fout>`, are not explicit when parsed from `argv`, as opposed to an option,
a flag or a command.

> *Lutline* warns you about the ambiguity of your CLI specifications

When you run *lutline*, the default behaviour is to print a warning message if
an ambiguous pattern is provided.

## Order of elements in a pattern

Another problem relates to the order in which the elements appear in a pattern.
Take look a this simple example: `./app [-t] [-o]`. Many third party
modules decide that this pattern should be embodied in any of
the following:

1. `./app`
2. `./app -t`
3. `./app -o`
4. `./app -t -o`
5. `./app -o -t` &nbsp;&nbsp;&larr; <span class="glyphicon glyphicon-eye-open"></span>

In embodiment number 5 both optional branches `[-t]` and `[-o]` where
expanded in an unordered fashion. In some contexts this behaviour might
be nice, but not in all.

> *Lutline* respects the order of the elements presented in your pattern by
> default

As you will see on the next pages, the default in *lutline* is to always
respect the order of the elements in the pattern, unless the developer makes
use of a specific operator that defines an unordered set of elements in the
pattern.

<br>

* Next: [The *lutline* approach](solution.html)

<br>
