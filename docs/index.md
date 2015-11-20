Parsing a command-line during runtime is supposed to be as simple as forwarding elements from ```argv``` to a dictionary-like structure.

With *lutline* you achieve that by generating an incredibly simple spaghetti string and the robotic code to read it while looping through `argv`.

The command-line interface specification provided is versatile without compromising the efficiency of the generated parser code.

# Documentation

How to use *lutline*:

*   [Tutorial - Getting started](get_started.html)

Use the following pages to know more about the inner-problems solved by *lutline*:

*   [The problem of parsing a command-line](problem.html)
*   [The *lutline* approach](solution.html)
    *   [Command-line interface specification](specfile.html)
    *   [Validating the non-ambiguoty of a pattern](validation.html)
    *   [The incredible spaghetti string](spaghetti.html)
*   [Efficiency analysis](efficient.html)
