import sys
from producer import run_producer
from consumer import run_consumer_single, run_consumer_batch


def print_usage():
    print("Usage: python main.py [producer|single|batch]")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
    mode = sys.argv[1]
    if mode == "producer":
        run_producer()
    elif mode == "single":
        run_consumer_single()
    elif mode == "batch":
        run_consumer_batch()
    else:
        print_usage()
        sys.exit(1)
