from typing import List, Dict
from pandas import DataFrame, read_csv
from datetime import datetime


class Export:
    history: DataFrame = read_csv('./Data/Export.csv')

    epochs: int = None
    batch_size: int = None
    window_size: int = None
    lstm: int = None
    dense: int = None
    dropout: float = None
    prediction: str = None
    target: str = None
    accuracy: int = None
    time_taken: int = None

    def __init__(self) -> None:
        self._date = None
        self._time = None

    def hyper_parameters(self, epochs, batch_size, window_size) -> None:
        self.epochs: int = epochs
        self.batch_size: int = batch_size
        self.window_size: int = window_size

    def model_parameters(self, lstm, dense, dropout) -> None:
        self.lstm = lstm
        self.dense = dense
        self.dropout = dropout

    def compare(self, prediction: List[int], target: List[int], accuracy: int, time_taken: int) -> None:
        self.prediction: str = ' - '.join(map(str, prediction))
        self.target: str = ' - '.join(map(str, target))
        self.accuracy: str = f'{accuracy}%'
        self.time_taken = time_taken

    @property
    def date(self) -> str:
        date = datetime.today()
        return date.strftime('%m/%d/%y')

    @date.setter
    def date(self, value):
        self._date = value

    @property
    def time(self) -> str:
        time = datetime.now()
        return time.strftime('%H:%M')

    @time.setter
    def time(self, value):
        self._time = value

    @property
    def df(self) -> DataFrame:
        return DataFrame(columns=['Prediction', 'Target', 'Accuracy', 'Epochs', 'Window Size',
                                  'Batch Size', 'LSTM', 'Dropout Variance', 'Dense Layers'])

    @property
    def data(self) -> Dict:
        return {'Prediction': self.prediction,
                'Target': self.target,
                'Accuracy': self.accuracy,
                'Epochs': self.epochs,
                'Window Size': self.window_size,
                'Batch Size': self.batch_size,
                'LSTM': self.lstm,
                'Dropout Variance': self.dropout,
                'Dense Layers': self.dense}

    def __repr__(self) -> property:
        return __class__

    def __str__(self) -> str:
        return f'Epochs = {self.epochs}\nBatch Size: {self.batch_size}\nWindow Size: ' \
               f'{self.window_size}\nLSTM Nodes: {self.lstm}\nDense Layers:' \
               f'{self.dense}\nDropout Variance: {self.dropout}\nPrediction: ' \
               f'{self.prediction}\nTarget: {self.target}\nAccuracy: {self.accuracy}\n' \
               f'Time Taken: {self.time_taken}\nDate: {self.date}\nTime: {self.time}'

    def append(self) -> None:
        columns = {self.df.columns[i]: self.data[i] for i in range(len(self.df.columns))}
        print(columns)
        pass


def main() -> None:  # NOQA
    test: Export = Export()

    test.compare([5, 19, 10], [6, 10, 11], 5, 10)

    print(test.__repr__())
    print(test.__str__())

    test.df.to_csv('./Data/Export.csv', index=False)

    print('\n\n')
    print(test.history)




if __name__ == '__main__':  # NOQA
    main()
