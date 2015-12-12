Parsing a command-line
Nowadays, most programming languages provide Command-Line Interface (CLI)
parser modules that allow the developer to implement a CLI specification
in the beginning of a program's run-time. Besides the standard modules
that come pre-bundled with the programming language, there are many other
known third-party modules. Some try to expand the possibilities and options
available to the developer. Others try to simplify the process of
developing a CLI specification.

Every time an application configured with other CLI parsers is executed by a
user, it requires the CLI specification to be parsed, instantiated and, only
then, matched against `argv`. These operations happen over and over again,
each time a user executes your application. For example, see
[argparse](http://docs.python.org/3/library/argparse.html) where the CLI
parser is fully instantiated each time you run your application.

*Lutline* solves this problem by antecipating all possible accepted inputs
from your users, and generating the parser code to quickly loop through
`argv`. As such, when a user runs your application making use of the
generated parser, only one step occurs: matching the input from `argv` with
your pattern. This is a different approach to the common CLI parsing:

* separate concerns: one thing is converting your pattern into code, another is
  matching `argv` as quickly as possible
* when a user runs your application, only the absolutely necessary source
  code will be executed

## CLI Specification &hArr; Pattern description

A CLI specification is merely a description of a pattern. For example, the
specification `./app [-f] <input>` has one optional flag followed by a
mandatory argument. This pattern matches the following two embodiments:

1. `./app <input>`
2. `./app -f <input>`

This type of decomposition is a great tool to look at CLI specifications
from a different perspective. If you try out this pen and paper approach
with other examples, you will see that there are some inner problems that
need to be taken care of. The following sections give a brief description of
some of those problems.

## Ambiguity

Let's take a look at the following CLI specification: `./app [<filein>]
[<fileout>]`. This pattern matches the following embodiments:

1. `./app`
2. `./app <filein> <fileout>`
3. `./app <filein>` &nbsp;&nbsp;&larr; <span class="glyphicon glyphicon-eye-open"></span>
4. `./app <fileout>` &nbsp;&nbsp;&larr; <span class="glyphicon glyphicon-eye-open"></span>

If we take a closer look at these embodiments, we see a problem happening
with numbers 3 and 4: on `argv` they are not distinguishable from each other.
A strict parser cannot correctly guess if `./app file.txt` should set
`file.txt` to `filein` or to `fileout`. Hence, in these circumstances, the
method should consider that this scenario results from an ambiguous pattern,
which allows different embodiments to match the same input.

This problem relates, mainly, to the fact that arguments, such as `<fin>` or
`<fout>`, are not explicit when parsed from `argv`.

## Order in a CLI specification

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
expanded in an unordered fashion. In some contexts this behaviour might be
nice, but not in all. The default should be to always respect the order of
the elements in the pattern, unless the developer specifies otherwise.

## Permutations in a CLI specification

Many CLIs nowadays, are specified with the usage message `./app_name
[OPTIONS] <argument>` and then list some options in the description that can
be used in that middle part `[OPTIONS]`. Something like this:

    $ ./app --help
    Usage: ./app_name [OPTIONS] <argument>
           ./app_name --help

    Options:
        --option1  This is option 1
        --option2  This is option 2
        --option3  This is option 3
        --help     Prints this message and exits

Using the above-mentioned decomposition for this CLI specification, we see
that the `[OPTIONS]` part expands into all possible k-permutions of the set
of options. The following embodiments apply:

1. `./app --help`
2. `./app <argument>`
3. `./app --option1 <argument>`
4. `./app --option2 <argument>`
5. `./app --option3 <argument>`
6. `./app --option1 --option2 <argument>`
7. `./app --option1 --option3 <argument>`
8. `./app --option2 --option1 <argument>`
9. `./app --option2 --option3 <argument>`
10. `./app --option3 --option1 <argument>`
11. `./app --option3 --option2 <argument>`
12. &nbsp;&nbsp;&larr; <span class="glyphicon glyphicon-eye-open"></span> `./app --option1 --option2 --option3 <argument>`

It is important to see that something tiny and simple on your usage message
explodes the number of possible embodiments.

<br>

* Next: [The *lutline* approach](solution.html)

<br>
