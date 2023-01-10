from re import search
import requests
import random


def average(args: list) -> int:
    return sum(args)/len(args)


def string_value(value: int) -> str:
    return f'{value:02}'


def collect(draw_number: int) -> list:
    url: str = f'https://www.indexoflebanon.com/lottery/loto/draw/{str(draw_number)}'
    response = requests.get(url, 'html.parser', timeout=10)
    source: str = response.text

    results = [j for i in range(1, 7) for j in range(1, 43)
               if search(f'<div class="loto_no_r bbb{str(i)}">'
                         f'{string_value(j)}</div>', source)]

    return results


# def compare_precision(prediction, target) -> float:     # DEPRECATED
#     prediction_: list = prediction
#     target_: list = target
#     deviation: list = []
#     result_: list = []
#     _result: list = []
#
#     for i in range(len(prediction_)):
#         if prediction_[i] <= target_[i]:
#             temp = str(target_[i] - prediction_[i])
#             deviation.append(f'±{temp}')
#         else:
#             if prediction_[i] >= target_[i]:
#                 temp = str(prediction_[i] - target_[i])
#                 deviation.append(f'±{temp}')
#
#     for j in range(len(prediction_)):
#         precision_ = str(int(abs((((target_[j]-prediction_[j])/target_[j])*100)-100)))
#         _result.append(f'{precision_}%')
#         result_.append(int(precision_))
#
#     average_precision: int = round(average(result_))
#     print(f'Precision = {average_precision}%')
#
#     print('\nPrediction:')
#     print(*prediction_, sep=' - ')
#
#     print('\nTarget:')
#     print(*target_, sep=' - ')
#
#     # print('\nDeviation:')
#     # print(*deviation, sep=' - ')
#
#     # final.append(f'{average_precision}%')
#     final = average_precision/100
#     # final.extend(deviation)
#
#     return final


def debug_generator(range_min: int, range_max: int, count: int) -> tuple:
    x = [random.randint(range_min, range_max) for _ in range(count)]
    y = [random.randint(range_min, range_max) for _ in range(count)]
    return x, y


def proximity_sort(list1: list, list2: list) -> tuple:
    zl = zip(list1, list2)
    zl = sorted(zl, key=lambda x: (abs(x[0] - x[1]), x[0]))
    list1, list2 = zip(*zl)
    return list(list1), list(list2)


def precision(predictions: list, targets: list) -> None:
    exact_match = list(filter(lambda x: x in predictions, targets))
    predictions: list = [item for item in predictions if item not in exact_match]
    targets: list = [item for item in targets if item not in exact_match]

    print(f'{exact_match=}\n\n{predictions=}\n{targets=}')  # NOQA

    predictions, targets = proximity_sort(predictions, targets)

    print(f'\n{predictions=}\n{targets=}')


def main() -> None:
    p1 = [6, 12, 18, 23, 30, 36]
    t1 = [14, 21, 26, 23, 30, 35]

    p, t = proximity_sort(p1, t1)

    print(f'{p=}\n{t=}')


if __name__ == '__main__':
    main()
