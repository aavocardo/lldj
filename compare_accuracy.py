from statistics import mean

# READABLE:
# prediction = [7, 39, 20, 30]
# target = [35, 37, 40, 21]


def precision(predictions: list, targets: list) -> None:
    a, b = set(predictions), set(targets)
    exact_match: set = a.intersection(b)






    print(f'{exact_match=}\n{predictions=}\n{targets=}')        # NOQA


def main() -> None:  # NOQA
    prediction_: list = [7, 14, 20, 26, 30, 39]
    target_: list = [14, 21, 26, 35, 37, 40]

    precision(prediction_, target_)

    print(round(mean(prediction_)))


if __name__ == '__main__':
    main()
