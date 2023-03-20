from modules import Lottery


for i in range(1, 2093):
    Lottery(i).to_csv()
    print(f'Draw {i} appended')
