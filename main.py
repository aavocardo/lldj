from re import search
import statistics
import requests
import random
import time


def string_value(value: int) -> str:
    return f'{value:02}'


def collect(draw_number: int) -> list:
    url: str = f'https://www.indexoflebanon.com/lottery/loto/draw/{str(draw_number)}'
    source: str = requests.get(url, 'html.parser', timeout=10).text

    results = [j for i in range(1, 7) for j in range(1, 43)
               if search(f'<div class="loto_no_r bbb{str(i)}">'
                         f'{string_value(j)}</div>', source)]

    return results


def dg(range_min: int, range_max: int, count: int) -> tuple:    # dg: debug_generator
    x = [random.randint(range_min, range_max) for _ in range(1, count)]
    y = [random.randint(range_min, range_max) for _ in range(1, count)]
    return x, y


def proximity_sort(list1: list, list2: list) -> tuple:
    zl = zip(list1, list2)
    zl = sorted(zl, key=lambda x: (abs(x[0] - x[1]), x[0]))
    list1, list2 = zip(*zl)
    return list1, list2


def precision(predictions: list, targets: list):
    exact_match = list(filter(lambda x: x in predictions, targets))
    predictions: list = [item for item in predictions if item not in exact_match]
    targets: list = [item for item in targets if item not in exact_match]

    print(f'{exact_match=}\n\n{predictions=}\n{targets=}')  # NOQA

    sorted_predictions, sorted_targets = proximity_sort(predictions, targets)

    print(f'\n{sorted_predictions=}\n{sorted_targets=}')


def compare_precision(prediction, target) -> float:     # DEPRECATED
    prediction_: list = prediction
    target_: list = target
    deviation: list = []
    result_: list = []
    _result: list = []

    for i, value in enumerate(prediction_):
        if value <= target_[i]:
            temp = str(target_[i] - value)
            deviation.append(f'±{temp}')
        else:
            if value >= target_[i]:
                temp = str(value - target_[i])
                deviation.append(f'±{temp}')

    for _, value in enumerate(prediction_):
        precision_ = str(int(abs((((target_[_]-value)/target_[_])*100)-100)))
        _result.append(f'{precision_}%')
        result_.append(int(precision_))

    average_precision: int = round(statistics.mean(result_))
    print(f'Precision = {average_precision}%')

    print('\nPrediction:')
    print(*prediction_, sep=' - ')

    print('\nTarget:')
    print(*target_, sep=' - ')

    return average_precision/100


def main() -> None:
    x = [random.randint(1, 2074) for _ in range(3)]
    st: float = time.time()
    for i, j in enumerate(x):
        print(f'Draw {j}: ', end='')
        temp: list = collect(j)
        print(*temp, sep=', ')

    print(f'\nTime taken: {round(time.time()-st, 3)}s')


if __name__ == '__main__':
    main()
