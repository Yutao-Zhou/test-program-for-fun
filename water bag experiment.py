import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tkinter import *
import random

master = Tk()
e = Entry(master)
e.pack()
e.focus_set()
height = 0
def callback():
    height = int(e.get())
    rou = 1 * 10 ** 3
    g = 9.8
    t = [*np.arange(0,1,0.01)]
    x = [*np.arange(0,1,0.01)]
    y = [*np.arange(0,1,0.01)]
    h = [*np.arange(0,0.5,0.01)]
    v = [*np.arange(0,0.5,0.01)]
    for i in range(len(v)):
        v[i] = ((2 * g * v[i]) ** 0.5)
    hindex = height - 1
    for i in range(len(x)):
        x[i] = v[hindex] * x[i]
    print(h[hindex])
    for i in range(len(y)):
        y[i] = -0.5 * 9.8 * (y[i] ** 2)
    def animate(i):
        graph.set_data(x[:i+1], y[:i+1])
        plt.title(f'Water flow trajectory at height of {height}cm',fontweight='bold',color=random_color(),fontsize=80)
        return graph
    def random_color():
        rgbl = [random.uniform(0, 1),random.uniform(0, 1),random.uniform(0, 1)]
        return tuple(rgbl)
    fig = plt.figure() 
    plt.xlim(0, 2)
    plt.ylim(-2, 0.1)
    graph, = plt.plot([], [], '2',ms = 40)
    ani = FuncAnimation(fig, animate, frames=100, interval=80)
    plt.xlabel('x distance (m)',fontweight='bold',fontsize=50)
    plt.ylabel('y distance (m)',fontweight='bold',fontsize=50)
    plt.legend(['Water flow trajectory'],fontsize=50)
    plt.grid()
    manager = plt.get_current_fig_manager()
    manager.full_screen_toggle()
    plt.show()
b = Button(master, text = "OK", width = 10, command = callback)
b.pack()
mainloop()