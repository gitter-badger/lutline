## Motivation

*Lutline* filters out any wastefull clock cycle from your code. Anything
that goes besides "_forwarding elements from argv to a dictionary-like
structure_" was analysed and limited as much as possible.

By generating a Look-Up Table (LUT), which comprises all the possible
embodiments of a pattern in a static, readable manner, *lutline* removes
the redundant initial stages of parsing and interpreting the developer's
pattern all together.

## Workflow

A workflow of the present solution to generate a LUT is divided in three
stages:

1. Parsing a Command-Line Interface (CLI) specification and processing a list of all possible embodiments
2. Validating the list to assert the ambiguosity of the pattern
3. Generating the LUT and the code to read it

After these, the developer can integrate the generated parser in is code
and execute his/her application, which runs the following intial step:
matching the user provided `argv` with an embodiment in the LUT, and
forwarding elements from `argv` to a dictionary-like structure accordingly.

As you can see, this workflow separates concerns. A first hard task is parsing
and interpreting a pattern from the developers mind. Another hard task, that
does not need to occur at the same time, is matching the pattern with
the user inputs. *Lutine* garantees that the second one is as fast as possible.

In order to achieve this workflow, the following sub-problems are solved:
*   [Command-line interface specification](specfile.html)
*   [Validating the non-ambiguoty of a pattern](validation.html)
*   [The incredible spaghetti string](spaghetti.html)
