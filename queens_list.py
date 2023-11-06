"""Solutions to the n queens problem with lists"""


def queens(n: int) -> list[list[int]]:
    """
    List of all solutions of the n queens problem, where n is the size of the
    chess board (indexed by pairs of integers < n). A solution is a list of n integers
    [a_0,...,a_(n-1)] such that a queen can be placed in row i and column a_i for all i.

    Arguments:
        n: size of the chess board

    Returns:
        List of complete solutions of the n queens problem
    """
    return partial_queens(n, 0, [], [], [])


def partial_queens(
    n: int, row: int, columns: list[int], sums: list[int], diffs: list[int]
) -> list[list[int]]:
    """
    List of partial solutions of the n queens problem, where n is the size
    of the chess board (indexed by pairs of integers < n). A solution is a list of n integers
    [a_0,...,a_(n-1)] such that a queen can be placed in row i and column a_i for all i.
    The solutions are built recursively up from previously placed queens.

    A position (row, col) can only be added when
        1. col is not the column of a previous position
        2. row + col is not in the sum of coordinates of a previous position
            since this would be on the diagonal going down left
        3. row - col is not in the differences of coordinates of a previous position,
            since this would be on the diagonal going down right

    Arguments:
        n: size of the chess board
        row: the current row for which a new position will be found if possible
        columns: the list of all (col) of previous positions
        sums: the list of all (row + col) of previous solutions
        diffs: the list of all (row - col) of previous solutions

    Returns:
        List of all partial solutions of the n queens problem
    """
    if row == n:
        return [columns]
    solutions = []
    for col in range(n):
        ok = col not in columns and row + col not in sums and row - col not in diffs
        if ok:
            next_solutions = partial_queens(
                n, row + 1, columns + [col], sums + [row + col], diffs + [row - col]
            )
            solutions += next_solutions
    return solutions
