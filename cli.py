import random
import argparse

def check_property(operation1, operation2, repetitions):
    correct_count = 0
    for _ in range(repetitions):
        a = random.random()
        b = random.random()
        c = random.random()

        result1 = eval(operation1)
        result2 = eval(operation2)

        if result1 == result2:
            correct_count += 1

    print(round((correct_count/repetitions)*100, 2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check if two operations are equivalent")
    parser.add_argument("--operation1", type=str, required=True, help="First operation to compare")
    parser.add_argument("--operation2", type=str, required=True, help="Second operation to compare")
    parser.add_argument("--repetitions", type=int, required=True, help="Number of repetitions to check")

    args=parser.parse_args()

    check_property(args.operation1, args.operation2, args.repetitions)