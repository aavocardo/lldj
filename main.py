from modules import Lottery


for i in range(2094, 2097):
    x = Lottery(i)
    x.to_csv()
