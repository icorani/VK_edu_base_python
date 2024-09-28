

def average_from_string(s: str) -> float:
    return sum(map(int, s.split())) / len(s.split())


def read_input() -> str:
    return input()


def main():
    in_str = read_input()
    while in_str:
        print(f"{round(average_from_string(in_str),2)}")
        in_str = read_input()


if __name__ == "__main__":

    main()
