# Generator for solutions to the n queens problem

These Python programs generate solutions to the [n queens problem](https://en.wikipedia.org/wiki/Eight_queens_puzzle). They uses different recursive algorithms and compares them with a benchmark. No backtracking is used, as we don't need it.

-   `queens_gen.py` provides a generator function that generates the solution. This is the fastest solution, in particular when one is interested to see a first solution quickly, and one does not need all solutions directly. Check the docstrings there for more information, as they explain exactly how it is done.
-   `queens_list.py` has the same algorithm, but uses a list instead. The computation of all solutions takes about the same amount of time. But since this is not a generator, one does not see the first solution before the computation of all solutions is done, which is not what you might want.
-   `queens_naive.py` is perhaps the most naive recursive implementation, because it does not remember the already taken columns and diagonals, which makes it quite slow.

Related repository (a web app that visualizes the solutions): https://github.com/ScriptRaccoon/queens-problem-svelte
