import argparse
import cProfile
import os
import random
import time


def main():
    data = read_file()

    for _ in data.splitlines():
        simulate_3pp_call()
        simulate_db_write()


def read_file():
    file = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(file) as f:
        data = f.read().strip()
    return data


def simulate_3pp_call():
    call_delay = random.randint(100, 1000)
    time.sleep(call_delay / 1000)


def simulate_db_write():
    call_delay = random.randint(100, 1000)
    time.sleep(call_delay / 1000)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Poc profiling with cProfile"
    )
    parser.add_argument(
        "--profile-screen",
        action="store_true",
        default=False,
        help="Execute with cProfile.run and display stats on screen",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    print("Running the script...")
    if args.profile_screen:
        cProfile.run("main()")
    else:
        main()
    print("Finished running the script...")
