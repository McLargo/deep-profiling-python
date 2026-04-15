from timeit import timeit

def sum_big_range(n):
    return sum(range(n * 1000000))

if __name__ == "__main__":
    iterations = 1000
    total_time = timeit('sum_big_range(2)', globals=globals(), number=iterations)

    print(f"sum_big_range took {total_time:.4f} seconds")
    print(f"sum_big_range average took {total_time/iterations:.4f} seconds")
