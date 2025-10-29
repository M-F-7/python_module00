from curses.ascii import isalnum
import sys
import string

msg_error = "ERROR"


def main() -> None:
    try:
        args: list = sys.argv[1:]
        assert len(args) == 2
        assert args[0].isdigit() == False
        assert args[1].isdigit()
        tab: list = args[0].split()
        final_tab: list = []

        for word in tab:
            filtered_chars = filter(str.isalpha, word) #FORBIDDEN
            word = "".join(filtered_chars)
            if len(word) > int(args[1]):
                final_tab.append(word)

        print(final_tab)
    except (ValueError, AssertionError):
        print(msg_error)


if __name__ == "__main__":
    main()
