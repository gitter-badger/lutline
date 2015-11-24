The lutline approach
*Lutline* filters out any wasteful clock cycle from your application.
Anything that goes besides "_forwarding elements from `argv` to a
dictionary-like structure_" was carefully analyzed and limited.

By generating a Look-Up Table (LUT), which comprises all the possible
embodiments of a pattern in a static, readable manner, *lutline* removes the
redundant initial stages of parsing and heavy instantiating the pattern all
together.

## Workflow

A workflow of the present solution to generate a LUT is divided in the
following stages:

1. Parsing a Command-Line Interface (CLI) specification
2. Processing a list of all possible embodiments
3. Generating the LUT
4. Validating the non-ambiguity of the LUT

After these, you can import the generated parser to your application which,
when executed, only performs one operation: matching the input from `argv` with
your pattern. After that, the elements provided by the user through `argv` are
returned in a dictionary.

As you can see, this workflow separates concerns. A first hard task is
parsing and structuring a pattern from your brain into a data structure.
Another different hard task, is matching a user generated `argv` against
your pattern. *Lutine* focuses on making the second one as lightweight as
possible.

<br>

* Next: [Command-line interface specification](specfile.html)

<br>
