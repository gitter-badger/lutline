Parsing a command-line during run-time is supposed to be as simple as
forwarding elements from ```argv``` to a dictionary-like structure.

With *lutline* you achieve that by antecipating all possible accepted inputs
from your users, and generating the parser code to quickly loop through `argv`.

The pattern customization available in *lutline* provides great versatility
without compromising the efficiency of the generated parser code.

# Documentation

How to use *lutline*:

*   [Tutorial - Getting started](get_started.html)

Use the following pages to know more about the inner-problems solved by *lutline*:

*   [Parsing a command-line](background.html)
*   [Command-line interface specification](specfile.html)
