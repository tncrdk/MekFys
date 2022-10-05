import numpy as np
import matplotlib.pyplot as plt


def main():
    filepaths = [
            "Data\white_black_unelastic_Nrot.txt",
            "Data\green_red_diag.txt",
            "Data\green_red_frontal.txt",
            "Data\green_white_frontal.txt",
            "Data\white_red_diag.txt"
        ]
    masses = {
        "red": 31.910,
        "green": 32.19,
        "white": 80.82,
        "black-b": 31.008,
        "white-b": 82.97
    }
    for i in range(filepaths):
        times, pos_first, pos_second = load_data(i)

        vel_first = differentiate(pos_first, times)
        vel_second = differentiate(pos_second, times)
        plot_and_save(times, vel_first, "some")
        plot_and_save(times, vel_second, "eome")

        
def plot_and_save(x, y, filename):
    plt.plot(x, y)
    plt.savefig(filename)

def load_data(file_path: str):
    data = np.loadtxt(file_path, delimiter=",", skiprows=3)
    times = data[:, 0]
    pos_first = data[:, 1:3]
    pos_second = data[:, 3:-1]
    return times, pos_first, pos_second

def differentiate(values: list[float], times: list[float]):
    return np.diff(values, axis=0) / np.vstack(np.diff(times))

def momentum(mass, velocity):
    return mass * velocity

def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

main()