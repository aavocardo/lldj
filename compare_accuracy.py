from statistics import mean


def precision(predictions: list, targets: list):
    def proximity_sort(list1: list, list2: list) -> tuple:
        zipped_lists = zip(list1, list2)
        zipped_lists = sorted(zipped_lists, key=lambda x: abs(x[0] - x[1]))
        list1, list2 = zip(*zipped_lists)
        return list1, list2

    exact_match = list(filter(lambda y: y in predictions, targets))
    predictions: list = [item for item in predictions if item not in exact_match]
    targets: list = [item for item in targets if item not in exact_match]

    print(f'{exact_match=}\n{predictions=}\n{targets=}')  # NOQA

    predictions, targets = proximity_sort(predictions, targets)

    print(predictions)
    print(targets)



def main() -> None:  # NOQA
    prediction_: list = [7, 14, 20, 26, 30, 39]
    target_: list = [14, 21, 26, 35, 37, 40]

    precision(prediction_, target_)


if __name__ == '__main__':
    main()
