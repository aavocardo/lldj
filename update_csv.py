from modules import Lottery

DRAW_NUMBER: int = 2097

x: Lottery = Lottery(DRAW_NUMBER)
x.to_csv()
