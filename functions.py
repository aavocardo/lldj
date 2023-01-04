from re import search
import requests


def collect(draw_number: int) -> list:
    base_host: str = "https://www.indexoflebanon.com/lottery/loto/draw/"
    url: str = f'{base_host}{str(draw_number)}'

    response = requests.get(url, 'html.parser', timeout=10)
    response.raise_for_status()
    source: str = response.text

    string_value = lambda value: f'{value:02}'  # NOQA E731

    results: list = [j for i in range(1, 7) for j in range(1, 43)
                     if search(f'<div class="loto_no_r bbb{str(i)}">'
                               f'{string_value(j)}</div>', source)]

    return results


def precision(predictions: list, targets: list):
    for i in range(len(predictions)):
        for j in range(len(targets)):
            print('ligma')


def main() -> None:
    print(collect(2050))

    prediction_ = [5, 10, 15, 20, 25, 30]
    target_ = [50, 100, 150, 200, 250, 300]

    precision(prediction_, target_)


if __name__ == '__main__':
    main()
