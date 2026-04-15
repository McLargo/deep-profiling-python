import time


def sleeping(n):
    time.sleep(n)


def create_int_list(n):
    return list(range(n * 1000000))


if __name__ == "__main__":
    for fn in [sleeping, create_int_list]:
        start_perf_counter = time.perf_counter()
        start_process_time = time.process_time()
        fn(2)
        end_perf_counter = time.perf_counter()
        end_process_time = time.process_time()
        print(f"{fn.__name__} took {end_perf_counter - start_perf_counter:.4f} seconds (perf_counter)")
        print(f"{fn.__name__} CPU time {end_process_time - start_process_time:.4f} seconds (process_time)")
