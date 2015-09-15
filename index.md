Every command-line application starts by matching the command-line arguments
against a pattern. In case of failure, the application presents an error
message and aborts its execution. Otherwise, its only a matter of routing the
correct command-line values to the right variables and move on with the
application execution.

*lutline* is a tool to generate a look-up table and the code to access
it while looping through `argv`, based on a command-line interface
specification. By accessing the LUT the application solves both the pattern
and the routing problems in a simple, efficient and elegant embodiment.
