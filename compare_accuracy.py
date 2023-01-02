from statistics import mean


def precision(predictions: list, targets: list) -> None:
    for prediction in range(len(predictions)):
        for target in range(len(targets)):
            print(f'{target=}')
        print(f'{prediction=}')

















def main() -> None:         # NOQA

    prediction_: list = [7, 15, 19, 26, 32, 40]
    target_: list = [14, 21, 26, 35, 37, 40]

    precision(prediction_, target_)

    print(mean(prediction_))


if __name__ == '__main__':
    main()
