def reverse_string(s):
    """
    Reverses the input string and returns it.
    """
    return s[::-1]


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Reverse input text.")
    parser.add_argument("text", type=str, help="Text to reverse")
    args = parser.parse_args()
    print(reverse_string(args.text))


if __name__ == "__main__":
    main()
