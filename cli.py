import pyperclip
import argparse


# argparsing
def main():
    parser = argparse.ArgumentParser(description="Fibonacci counting")
    parser.add_argument("--count", required=True,
                        help="Count fibonacci until this number.")
    parser.add_argument("--display", required=True,
                        help="Defines how the output is displayed.")
    parser.add_argument("--copy", action="store_true",
                        help="Copy the result.")
    parser.add_argument("--print", action="store_true",
                        help="Print the result in the terminal.")

    args = parser.parse_args()

    valid_displays = ["all", "position"]
    if args.display not in valid_displays:
        print("Invalid display argument! Valid arguments: all, position.")
        exit()
    if args.print:
        print(f"{fibonacci(int(args.count), str(args.display))}")
    if args.copy:
        pyperclip.copy(fibonacci(int(args.count), str(args.display)))
        print("Result copied to clipboard.")
    if not args.print and not args.copy:
        print("You kinda need to tell me a way to copy the output... For me to be of use... Or something.")


def fibonacci(amount, display):
    fibList = [0, 1]
    for i in range(amount):
        fibList.append(fibList[-2] + fibList[-1])
    if display == "all":
        return ' '.join(map(str, fibList[1:]))
    elif display == "position":
        return fibList[-1]


if __name__ == "__main__":
    main()
