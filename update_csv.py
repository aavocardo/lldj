from modules import Lottery


START_DRAW: int = 2105
END_DRAW: int = 2105


def main() -> None:
    for i in range(START_DRAW, END_DRAW+1):
        draw: Lottery = Lottery(i)
        draw.to_csv()


if __name__ == '__main__':
    main()
