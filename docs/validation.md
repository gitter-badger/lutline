Validating the non-ambiguoty of a pattern
## Generating all of the embodiments

> This sub-problem is dealt with in the module [lutline.embodiments](https://github.com/ffunenga/lutline/blob/master/lutline/embodiments.py).

The at least one embodiment related to a pattern can be generated with, for
example, the
[Depth-First Search](http://en.wikipedia.org/wiki/Depth-first_search)
method. If a tree structure is used where each node is a pattern, and its
children is the resulting pattern after a single expansion, than the leaf
nodes are the embodiments of the pattern. For example, the following
pattern `app.py (-i [-t] <input_file>) | <output_file>` can be decomposed in the
following tree.

|  Node | Pattern                                          | Children |
|-------|--------------------------------------------------|----------|
| 0     | `app.py (-i [-t] <input_file>) `&verbar;` <output_file>`  | `[1, 2]` |
| 1     | `app.py -i [-t] <input_file>`                    | `[3, 4]` |
| 2     | `app.py <output_file>`                           | `None`   |
| 3     | `app.py -i -t <input_file>`                      | `None`   |
| 4     | `app.py -i <input_file>`                         | `None`   |

As you can see, the leaf nodes, corresponding to the rows 2, 3 and 4, list
out all the possible embodiments of the pattern.

## Validating the ambiguity of a list of embodiments

> This sub-problem is dealt with in the module [lutline.validate](https://github.com/ffunenga/lutline/blob/master/lutline/validate.py).

In order to identify pairs of ambiguous embodiments, the position of
explicit elements, such as flags and commands, and the position of implicit
elements, such as arguments, should be analyzed and compared. A basic
solution for this analysis involves a (N^2)/2 complexity, where N is the
number of embodiments to analyze.
