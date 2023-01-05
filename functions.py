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
    for i in range(len(predictions)):
        for j in range(len(targets)):
            print(f'{j=}-{i=}')


def main() -> None:
    prediction_ = [5, 10, 15, 20, 25, 30]
    target_ = [50, 100, 150, 200, 250, 300]

    precision(prediction_, target_)


if __name__ == '__main__':
    main()
