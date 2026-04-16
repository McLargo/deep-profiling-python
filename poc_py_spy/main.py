import math
import os


def cpu_intensive_task(n):
    result = 0
    for i in range(n):
        result += math.sqrt(i) * math.sin(i) * math.cos(i + 0.1)
    return result


if __name__ == "__main__":
    print("Starting CPU intensive task...")
    print("You can attach py-spy to this process using the PID above like:")
    print("  uv run py-spy top --pid", os.getpid())
    result = cpu_intensive_task(100_000_000_000)
    print("Result:", result)
