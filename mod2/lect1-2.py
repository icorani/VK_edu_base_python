exclude_symbols = '!@#%'


def update_string(s: str) -> str:
    res = s.translate(s.maketrans({x: '' for x in exclude_symbols}))
    return res.upper() if s[0] == "!" else res.lower()


def read_input() -> str:
    return input()


def main():
    in_str = read_input()
    while in_str:
        print(update_string(in_str))
        in_str = read_input()


if __name__ == "__main__":
    main()
