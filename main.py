from typing import List, Union, Set
from dataclasses import dataclass
from re import search
import mysql.connector
import requests
import time
import csv


@dataclass
class Lottery:
    def __init__(self, draw: int) -> None:
        self.draw = draw
        self.results = Lottery.collect(self, timer=False)

    def collect(self, timer: bool = False) -> List[int]:
        Timer().start()
        url: str = f'https://www.indexoflebanon.com/lottery/loto/draw/{str(self.draw)}'
        source: str = requests.get(url, 'html.parser', timeout=15).text

        results: List[int] = [j for i in range(1, 7) for j in range(1, 43)
                              if search(f'<div class="loto_no_r bbb{str(i)}">'
                                        f'{j:02}</div>', source)]

        if len(results) != 6:
            raise ValueError('Length error')
        elif timer:
            Timer().stop()

        return results

    def to_mysql(self) -> None:
        local_db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='lldj'
        )

        results: List[int] = self.results
        query = 'INSERT INTO Results (B1, B2, B3, B4, B5, B6) VALUES (%s, %s, %s, %s, %s, %s)'
        values = results[:6]

        db = local_db.cursor()
        db.execute(query, values)
        local_db.commit()

    def to_csv(self) -> None:
        FILE_NAME = 'data.csv'
        with open(FILE_NAME, 'a', encoding='UTF-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.results)


@dataclass
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
        targets: Union[Set[int], List[int]] = sorted([item for item in self.target if item not in exact_match])
        predictions: Union[Set[int], List[int]] = sorted([item for item in self.prediction if item not in exact_match])

        accuracy: int = 0

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
        self.lap = None

    def start(self) -> None:
        if self.start_time is not None:
            raise Exception('Timer is running')
        else:
            self.start_time = time.perf_counter()

    def stop(self) -> None:
        if self.start_time is None:
            raise Exception('Timer not running')
        else:
            self.lap = round(time.perf_counter() - self.start_time, 3)
            self.start_time = None
            print(f'Time taken: {self.lap}')
