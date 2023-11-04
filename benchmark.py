from timeit import timeit

FILES = ["queens_gen", "queens_list", "queens_naive"]


def main():
    for n in range(4, 12):
        print(f"\nbenchmark for n={n}")
        cmd = f"list(queens({n}))"
        for file in FILES:
            setup = f"from {file} import queens"
            print(file, timeit(cmd, number=10, setup=setup), sep=": ")


if __name__ == "__main__":
    main()
