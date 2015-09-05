LUTLINE
*******


Technical Field
===============
The present project provides a method to generate a command-line interface (CLI)
parser.


Background
==========
Nowadays, most programming languages provide CLI parser modules or libraries
that allow the developer to implement a CLI specification at the beginning of
his/her program execution. Besides the standard modules that come pre-bundled
with the programming language, there are many other well-known third-party
modules. Some try to expand the possibilities and options available to the
developer. Others try to simplify the process for developing a CLI
specification. Further solutions try to find a balance between these two
dimensions.

None of the known prior solutions achieves an efficient implementation regarding
processing and memory usage in order to parse the user provided arguments.
Every time the application is executed by a user, it requires the CLI
specification to be recompiled/reconstructed.


General Description
===================
The present project discloses a method of generating a look-up table (LUT) based
on a CLI specification and a method of accessing said LUT when parsing an array
of strings (in most programming languages, this array is known as "argv").

In order to generate a LUT based on a CLI specification, a step comprises
listing all the possible embodiments that can be faced by the parser.
This step allows expanding the search-space intended to be addressed by the
generated LUT.

A CLI specification is a pattern that matches at least one embodiment. For
example, the pattern "./app [-f] <input>" matches the following embodiments:
    1: ./app <input>
    2: ./app -f <input>

The at least one embodiment related to a pattern can be generated with,
for example, the Depth-First Search method. Each node of the tree is a pattern
and the leaf nodes are the embodiments of the pattern.

In the above example, it is simple to devise a way of addressing the two
embodiments. A more complex example can be achieved with the following pattern:
"./app [<filein>] [<fileout>]". This pattern matches the following embodiments:
    1: ./app
    2: ./app <filein> <fileout>
    3: ./app <filein>
    4: ./app <fileout>

Take a closer look at embodiments 3 and 4 in this last example. They are
ambiguous and no parser can correctly guess if "./app file.txt" sets "file.txt"
to "filein" or to "fileout". Hence, in these circumstances, the method should
immediately exit with an error message printed for the developer's eyes.

In order to identify pairs of ambiguous embodiments, the position of explicit
elements, such as flags and commands, and the position of implicit elements,
such as arguments, should be analyzed and compared. A basic solution for this
analysis involves a (N^2)/2 complexity, where N is the number of embodiments
to analyze.

After the at least one embodiments is validated, its time to generate the LUT.
In the present solution, a LUT is disclosed in a heap fashion: each row is a
node of a tree, with reference to child nodes (which are in the subsequent
rows). Each row (node) comprises 3 columns (attributes): embodiments, explicits
and implicits. Lets look at an example.

The pattern "./app [[-f <fout>] <fin>]" matches the following 3 embodiments:
    1: "./app"
    2: "./app <fin>"
    3: "./app -f <fout> <fin>"

The first row (node) of the LUT relates to argv[0]. If argv[0] is empty, than
the embodiment provided by the first column (attribute) should be used to parse
the argv. If argv[0] is not empty, than it can be an explicit or an implicit
element. The possible explicit/implicit elements are indexed in the remaining
two columns (attributes). The first row (node) is implemented as follows:

embodiments |   explicits  | implicits
------------|--------------|-----------
    []      | [('-f', 2)]  |     1

If argv[0] equals "-f" than the current pointer should jump 2 rows down in the
LUT. Otherwise, if argv[0] is both not empty and not recognized, than it means
it is an argument. In that case, the current pointer should jump 1 row down in
the LUT. The entire LUT is implement as follows:

             embodiments                     |   explicits  | implicits
---------------------------------------------|--------------|-----------
  []                                         | [('-f', 2)]  |  1
  [('c', 'fin')],                            |  None        |  None
  None,                                      |  None        |  1
  None,                                      |  None        |  1
  [('f', 'f'), ('a', 'fout'), ('a', 'fin')]  |  None        |  None

And now, it is only a matter of representing the above LUT in a specified format,
not necessarily humanly readable. For example, the following spaghetti string:

  ",-f;2,1_a;fin,,_,,1_,,1_f;f:a;fout:a;fin,,"

Don't waste much time looking at it. The important aspect to note is that the
format makes use of separator characters: "_" separates lines, "," separates
columns, and ":" is used in conjunction with  ";" to represent a list of tuples.
Probably, there are other smaller, better formats to be used here.


Examples
========
In python, a simple CLI parser in the Python programming language, mainly
built using «oneliners», is implemented with the following source-code.

"""
import sys

USAGE = 'usage: ./app [[-f <fout>] <fin>]'

def parse_cli(argv=sys.argv[1:]):
    lut = ",-f;2,1_a;fin,,_,,1_,,1_f;f:a;fout:a;fin,,"
    lst = lambda s: [e.split(";") for e in s.split(":")] if ";" in s else s
    expand = lambda s: None if s == '' else lst(s)
    getline = lambda l: l[:None if -1 == l.find("_") else l.find("_")]
    forward = lambda l: None if -1 == l.find("_") else l[l.find("_") + 1:]
    emb, exs, imp = (expand(e) for e in getline(lut).split(","))
    for arg in argv:
        h = next((e1 for e0, e1 in exs if arg == e0), None) if exs else None
        if not (h or imp):
            sys.exit(USAGE)
        for i in range(int(h if h else imp)):
            lut = forward(lut)
        emb, exs, imp = (expand(e) for e in getline(lut).split(","))
    f = lambda a, t: t != "f" and a[0] == "-" or t == "f" and a[0] != "-"
    if not emb or any(f(a, t) for a, (t, l) in zip(argv, emb)):
        sys.exit(USAGE)
    return {l: argv[i] for i, (t, l) in enumerate(emb)}
"""

It is simple to adapt this code to a new pattern. There are only two lines that
need to be changed: the line that starts with "USAGE = (...)" and the first line
in the body of the function "parse_cli" that starts with "lut = (...)".

Lisbon, September 3, 2015.
