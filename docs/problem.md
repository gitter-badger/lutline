## Background

Nowadays, most programming languages provide Command-Line Interface (CLI)
parser modules that allow the developer to implement a CLI specification
near the beginning of a program's runtime. Besides the standard modules
that come pre-bundled with the programming language, there are many other
known third-party modules. Some try to expand the possibilities and options
available to the developer. Others try to simplify the process for
developing a CLI specification. Further solutions try to find a balance
between these two dimensions.

None of the known prior solutions achieves a complexity `O(argc)`, where
`argc` is the lenght of `argv`, and at the same time enables CLI
customization of relations between elements. Every time an application
configured with any of the prior CLI parsers is executed by a user, it
requires the CLI specification to be parsed and allocated over and over
again, and only then interpreted. For example, see
[argparse](http://docs.python.org/3/library/argparse.html) where the CLI
parser is fully instantiated each time you run your application.

## CLI Specification &hArr; Pattern description

A CLI specification is merely a description of a pattern. For example, the
pattern `./app [-f] <input>` has one optional flag followed by a mandatory
argument. This pattern only matches the following two embodiments:

1. `./app <input>`
2. `./app -f <input>`

This type of decompostion is a great tool to look at CLI specifications from a
different prespective and find new sub-problems, such as ambiguity or
order.

## Ambiguity

Any CLI specification with a finite number of embodiments can be decomposed
in a fashion similar to the previous list. A more complex example can be
achieved with the following pattern: `./app [<filein>] [<fileout>]`.
This pattern matches the following embodiments:

1. `./app`
2. `./app <filein> <fileout>`
3. `./app <filein>`
4. `./app <fileout>`

If you take a closer look to these embodiments, you might be see what is
happening with numbers 3 and 4. As you can see, they are not different from
each other and a strict parser cannot correctly guess if `./app file.txt`
should set `file.txt` to `filein` or to `fileout`. Hence, in these
circumstances, the method should consider that this scenario results from
an ambiguos pattern, and immediately exit with an error message printed for
the developer's eyes.

This problem relates, mainly, to the fact that arguments are not explicit
when parsed from `argv`, as opposed to an option, a flag or a command.

## Order

Another problem relates to the order in which the elements appear in a pattern.
Take look a this simples example: `./app [-t] [-o]`. Many third party
modules automaticly ___dictate___ that this pattern should be embodied in any of
the following:

1. `./app`
2. `./app -t`
3. `./app -o`
4. `./app -t -o`
5. `./app -o -t` &rarr; Uops!

Embodiment number 5 seems a little bit unexpected. In this case, both
optional branches `[-t]` and `[-o]` where expanded in an unordered fashion.

Lets look at another example, and recall one of the above exemplary
patterns: `./app [-f] <input>`. If the unsorted behaviour would be the
default one, than it would be forcibly possible to embody the pattern
with: `./app <input> -f`. There are cases where the developer does not want
this at all. As a matter of fact, it seems a little counterintuitive to provide your
`argv` array like that, when the pattern represented in front of you clearly places
the optional flag before the mandatory argument.

So, the problem that is presented here can be posed in the following question:

> Should the order of the elements presented in a pattern be respected
> by default or not?

The answer defined in this project to this sneaky (but extermely important)
detail is yes. As you will see on the next pages, the default in *lutline*
is to always respect the order of the elements in the pattern, unless the
developer makes use of a specific operator that defines an unordered set of
elements in the pattern.

<br>

* Next: [The *lutline* approach](solution.html)

<br>
