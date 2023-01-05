from re import search
import requests


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


def main() -> None:
    p1 = [6, 12, 18, 23, 30, 36]
    t1 = [14, 21, 26, 23, 30, 35]

    p2 = [5, 10, 15, 20, 25, 30]
    t2 = [50, 100, 150, 200, 250, 300]

    precision(p1, t1)
    print('\n')
    precision(p2, t2)


if __name__ == '__main__':
    main()
