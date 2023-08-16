from sliding_window import SlidingWindow
import matplotlib.pyplot as plt
import os

def save(csv_filename: str, img_filename: str, win_len: int):
    sw = SlidingWindow(win_len)

    f = open(csv_filename)

    indata = list(map(float, map(lambda x: x[1:len(x)-1].split('","')[0], f.readlines())))

    outdata = []

    for i in indata:
        outdata.append(sw(i))
    
    plt.plot(indata)
    plt.plot(outdata)
    plt.savefig(img_filename)
    plt.cla()

i = 2

for filename in os.listdir('csv'):
    save(os.path.join('csv', filename), os.path.join('imgs', f'Figure_{i}.png'), i)
    i += 1