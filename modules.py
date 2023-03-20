from typing import List, Set, Union
from requests import get
from re import search
from time import perf_counter
import csv


class Lottery:
    def __init__(self, draw: int) -> None:
        self.draw: int = draw
        self.results: List[int] = Lottery.collect(self, timer=False)

    def __repr__(self) -> str:
        return f'Lottery({self.draw})'

    def __str__(self) -> str:
        return f'self.draw = {self.draw}\nself.results = {self.results}'

    def collect(self, timer: bool = False) -> List[int]:
        Timer().start()
        url: str = f'https://www.indexoflebanon.com/lottery/loto/draw/{str(self.draw)}'
        source: str = get(url, 'html.parser', timeout=15).text

        results: List[int] = sorted([j for i in range(1, 7) for j in range(1, 43)
                                     if search(f'<div class="loto_no_r bbb{str(i)}'
                                               f'">{j:02}</div>', source)])

        if len(results) != 6:
            raise ValueError('Length error')
        elif timer:
            Timer().stop()

        return results

    def to_csv(self) -> None:
        FILE_NAME = 'Data/data.csv'
        with open(FILE_NAME, 'a', encoding='UTF-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.results)


class Review:
    def __init__(self, prediction: List[int], target: List[int]) -> None:
        self.prediction = prediction
        self.target = target

        if len(self.prediction) != len(self.target):
            raise ValueError('List indexes out of range')

    def show(self) -> None:
        print('Prediction: ', end='')
        print(*self.prediction, sep=', ')

        print('Target: ', end='')
        print(*self.target, sep=', ')

    def precision(self, show: bool = False, percentage: bool = False) -> Union[int, str]:
        exact_match = list(filter(lambda x: x in self.prediction, self.target))
        predictions: Union[Set[int], List[int]] = sorted([item for item in self.prediction if item not in exact_match])
        targets: Union[Set[int], List[int]] = sorted([item for item in self.target if item not in exact_match])

        accuracy: int = 0

        print(exact_match)
        print(targets)
        print(predictions)

        for i, _ in enumerate(predictions):
            for j, _ in enumerate(targets):
                pass

        if show:
            print('Exact Match: ', end='')
            print(*exact_match, sep=', ')
        elif percentage:
            return f'{accuracy * 100}%'
        else:
            return accuracy


class Timer:
    def __init__(self) -> None:
        self.start_time = None
        self.end_time = None

    def start(self) -> None:
        if self.start_time is not None:
            raise Exception('Timer is running')
        else:
            self.start_time = perf_counter()

    def stop(self) -> None:
        if self.start_time is None:
            raise Exception('Timer not running')
        else:
            self.end_time = round(perf_counter() - self.start_time, 3)
            self.start_time = None
            print(f'Time taken: {self.end_time}')
            return self.end_time
