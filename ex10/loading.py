from time import sleep
from tqdm import tqdm

def ft_progress(lst):
    return tqdm(
        iterable=lst,
        ncols=80,
        smoothing=1,
        ascii=" >=",
        bar_format="ETA {remaining} [{percentage:2.0f}%] [{bar}] {n_fmt}/{total_fmt} | elapsed time {elapsed}s"
    )

    




listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)


listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    sleep(0.005)
print()
print(ret)