"""Solutions to the n queens problem with lists and top-down computation"""


def queens(n: int) -> list[list[tuple[int, int]]]:
    """
    List of all solutions of the n queens problem, where n is the size of the
    chess board (indexed by pairs of integers < n). A solution is a list of n integers
    [a_0,...,a_(n-1)] such that a queen can be placed in row i and column a_i for all i.

    Arguments:
        n: size of the chess board

    Returns:
        List of complete solutions of the n queens problem
    """
    return partial_queens(n, n - 1)


def partial_queens(n: int, row: int) -> list[list[tuple[int, int]]]:
    """
    List of partial solutions of the n queens problem, where n is the size
    of the chess board (indexed by pairs of integers < n). A solution is a list of n integers
    [a_0,...,a_(n-1)] such that a queen can be placed in row i and column a_i for all i.
    The solutions are built recursively up from previously placed queens.

    Arguments:
        n: size of the chess board
        row: the current row for which a new position will be found

    Returns:
        List of all partial solutions of the n queens problem
    """
    if row >= 0:
        solutions = []
        previous_solutions = partial_queens(n, row - 1)
        for solution in previous_solutions:
            for col in range(n):
                if all(
                    y != col and row + col != x + y and row - col != x - y
                    for [x, y] in solution
                ):
                    new_solution = solution + [(row, col)]
                    solutions.append(new_solution)
        return solutions
    else:
        return [[]]
