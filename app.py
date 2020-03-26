import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x, y = [], []
ln, = plt.plot([], [], 'ro')


def compute(Bw, dB):
    return Bw * np.log2(1 + np.power(10, dB/10))


def update(Bw, dB):
    x.append(dB)
    y.append(compute(Bw, dB))
    ln.set_data(x, y)
    ax.relim()
    ax.autoscale_view()
    return ln,


Bw_ = 5
dB_ = np.arange(0, 250)
ani = FuncAnimation(fig,
                    lambda frame: update(Bw_, frame),
                    frames=dB_)
plt.title('Bandwith = 1Bps')
plt.xlabel('dB (SNR)')
plt.ylabel('C (Bps)')
plt.show()
