"""Code for MAT461: Hamiltonian Mechanics HW1"""

import matplotlib.pyplot as plt
import numpy as np


def y_vel(x, y):
    return 5 * x ** 4 - 24 * x ** 3 + 24 * x ** 2


def x_vel(x, y):
    return y


def phase_portrait(xlim, ylim, n_grid, t_step, tot_time):
    x = np.linspace(xlim[0], xlim[1], n_grid)
    y = np.linspace(ylim[0], ylim[1], n_grid)

    for x_init in x:
        for y_init in y:
            counter = 1
            x_coord = x_init
            y_coord = y_init
            x_lst = [x_coord]
            y_lst = [y_coord]
            for i in range(0, int(tot_time / t_step)):
                X_vel = x_vel(x_coord, y_coord) * t_step
                Y_vel = y_vel(x_coord, y_coord) * t_step
                x_coord += X_vel
                y_coord += Y_vel
                x_lst.append(x_coord)
                y_lst.append(y_coord)
            counter += 1
            plt.scatter(x_lst, y_lst, marker=',', s=1)
    plt.xlabel("Position (x)")
    plt.ylabel("Velocity (y)")
    plt.show()


if __name__ == '__main__':
    phase_portrait([-1.5, 3], [-5, 5], 20, 0.01, 0.4)
