"""Solutions to the n queens problem with generators"""

from collections.abc import Iterator


def queens(n: int) -> Iterator[list[int]]:
    """
    Generator yielding solutions of the n queens problem, where n is the size of the
    chess board (indexed by pairs of integers < n). A solution is a list of n integers
    [a_0,...,a_(n-1)] such that a queen can be placed in row i and column a_i for all i.

    Arguments:
        n: size of the chess board

    Returns:
        Generator yielding complete solutions of the n queens problem
    """
    return partial_queens(n, 0, [], [], [])


def partial_queens(
    n: int, row: int, columns: list[int], sums: list[int], diffs: list[int]
) -> Iterator[list[int]]:
    """
    Generator yielding partial solutions of the n queens problem, where n is the size
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
        Generator yielding partial solutions of the n queens problem
    """
    if row < n:
        for col in range(n):
            valid_pos = (
                col not in columns and row + col not in sums and row - col not in diffs
            )
            if valid_pos:
                yield from partial_queens(
                    n, row + 1, columns + [col], sums + [row + col], diffs + [row - col]
                )
    else:
        yield columns


def solution_as_string(solution: list[int]) -> str:
    """
    Prints a solution of the n queens problem in a nice way

    Arguments:
        solution: any list of column positions
    """
    n = len(solution)
    output: str = " " + "_" * (2 * n - 1) + "\n"
    for row in range(n):
        output += "|"
        for col in range(n):
            output += "Q" if solution[row] == col else "*"
            if col < n - 1:
                output += " "
        output += "|\n"
    output += " " + chr(8254) * (2 * n - 1)
    return output


def main() -> None:
    """Prints all solutions of the n queens problem and their amount"""
    print("\nQueens problem")
    number_solutions = 0
    while True:
        size_input = input("\nInput the size of the board: ")
        if size_input.isnumeric() and size_input != "0":
            break
        print("Invalid number")

    n = int(size_input)
    solutions = queens(n)
    print("\nPress Enter to always create the next solution")
    while True:
        try:
            solution = next(solutions)
            number_solutions += 1
            print(solution_as_string(solution))
            input("")
        except StopIteration:
            print(f"{number_solutions} solutions have been found")
            break


if __name__ == "__main__":
    main()
