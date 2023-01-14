from re import search
import random
import requests


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

    average_precision: int = round(average(result_))
    print(f'Precision = {average_precision}%')

    print('\nPrediction:')
    print(*prediction_, sep=' - ')

    print('\nTarget:')
    print(*target_, sep=' - ')

    return average_precision/100


def average(args: list) -> int:
    return sum(args)/len(args)


def string_value(value: int) -> str:
    return f'{value:02}'


def collect(draw_number: int) -> list:
    url: str = f'https://www.indexoflebanon.com/lottery/loto/draw/{str(draw_number)}'
    source: str = requests.get(url, 'html.parser', timeout=10).text

    results = [j for i in range(1, 7) for j in range(1, 43)
               if search(f'<div class="loto_no_r bbb{str(i)}">'
                         f'{string_value(j)}</div>', source)]

    return results


def dg(range_min: int, range_max: int, count: int) -> tuple:        # dg: debug_generator
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

    predictions, targets = proximity_sort(predictions, targets)

    print(f'\n{predictions=}\n{targets=}')


def main() -> None:
    # p = [6, 12, 18, 23, 30, 36]
    # t = [14, 21, 26, 23, 30, 35]

    p, t = dg(1, 1000, 200)

    for i in range(100):
        p.pop(random.randint(1, 100))
        t.pop(random.randint(1, 100))

    precision(p, t)


if __name__ == '__main__':
    main()
