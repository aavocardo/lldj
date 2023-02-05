import csv
import time
import requests
import mysql.connector
from re import search
from typing import List, Union, Set
from dataclasses import dataclass


@dataclass
class Lottery:
    def __init__(self, draw: int):
        self.draw = draw
        self.results = Lottery.collect(self, timer=False)

    def collect(self, timer: bool = False) -> List[int]:
        st: float = time.time()
        url: str = f'https://www.indexoflebanon.com/lottery/loto/draw/{str(self.draw)}'
        source: str = requests.get(url, 'html.parser', timeout=30).text

        results: List[int] = [j for i in range(1, 7) for j in range(1, 43)
                              if search(f'<div class="loto_no_r bbb{str(i)}">'
                                        f'{j:02}</div>', source)]

        if timer:
            print(f'Time taken: {round(time.time() - st, 3)}s\n')

        return results

    @staticmethod
    def to_mysql(input_data: List[int]) -> None:
        local_db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='lldj'
        )

        results: List[int] = input_data
        query = 'INSERT INTO Results (B1, B2, B3, B4, B5, B6) VALUES (%s, %s, %s, %s, %s, %s)'
        values = (results[0], results[1], results[2], results[3], results[4], results[5])

        db = local_db.cursor()
        db.execute(query, values)
        local_db.commit()

        print(f'{db.rowcount} record inserted')

    @staticmethod
    def to_csv(input_data: List[int]) -> None:
        FILE_NAME = 'data.csv'
        with open(FILE_NAME, 'a', encoding='UTF-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(input_data)


@dataclass
class Review:
    def __init__(self, prediction: List[int], target: List[int]) -> None:
        self.prediction = prediction
        self.target = target

    def show(self) -> None:
        print('Prediction: ', end='')
        print(*self.prediction, sep=', ')

        print('Target: ', end='')
        print(*self.target, sep=', ')

    def precision(self, show: bool = False, percentage: bool = False) -> Union[int, str]:
        if len(self.prediction) != len(self.target):
            raise ValueError('List indexes out of range')

        exact_match = list(filter(lambda x: x in self.prediction, self.target))
        predictions: Union[Set[int], List[int]] = [item for item in self.prediction if item not in exact_match]
        targets: Union[Set[int], List[int]] = [item for item in self.target if item not in exact_match]
        predictions.sort(), targets.sort()

        print(predictions)
        print(targets)

        accuracy = 0

        if show:
            print('Exact Match: ', end='')
            print(*exact_match, sep=', ')
        elif percentage:
            return f'{accuracy * 100}%'
        else:
            return accuracy

    @staticmethod
    def get_closest(x, y):      # GPT3 TRASH
        result = []
        for i, _ in enumerate(x):
            closest_diff = float('inf')
            closest_pair = (None, None)
            for j, _ in enumerate(y):
                diff = abs(x[i] - y[j])
                if diff < closest_diff:
                    closest_diff = diff
                    closest_pair = (x[i], y[j])

            if closest_diff > 5:
                y.append(y.pop(y.index(closest_pair[1])))

            result.append(closest_pair)

        return result

    def try_again(self) -> None:
        for i, _ in enumerate(self.prediction):
            for j, _ in enumerate(self.target):
                pass


class Timer:
    def __init__(self) -> None:
        self.start_time = None

    def start(self) -> None:
        if self.start_time is not None:
            raise Exception('Timer is running')

        self.start_time = time.perf_counter()

    def stop(self) -> None:
        if self.start_time is None:
            raise Exception('Timer not running')

        time_taken = time.perf_counter() - self.start_time
        self.start_time = None

        print(f'Time taken: {round(time_taken, 3)}s')
