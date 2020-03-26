import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
x, y = [], []
ln, = plt.plot([], [])


def compute(Bw, dB):
    snr = 10 ** (dB/10)
    return Bw * np.log2(1 + snr)


def update(Bw, frame):
    x.append(frame)  # dB
    y.append(compute(Bw, frame))  # Bps
    ln.set_data(x, y)
    ax.relim()
    ax.autoscale_view()
    return ln,


# Formula: C=Bw*log2(1+SNR)
# X axis -> dB (SNR)
# Y axis -> C (Channel Capacity)
Bw_ = 23.8 * (10**6)
dB_ = np.linspace(36, 100)
ani = FuncAnimation(fig,
                    lambda frame: update(Bw_, frame),
                    frames=dB_)
plt.xlabel('dB (SNR)')
plt.ylabel('C (Bps)')
plt.show()
