import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    filepaths = [
        "Data\white_black_unelastic_Nrot.txt",
        "Data\green_red_diag.txt",
        "Data\green_red_frontal.txt",
        "Data\green_white_frontal.txt",
        "Data\white_red_diag.txt",
    ]
    masses = {
        "red": 31.910,
        "green": 32.19,
        "white": 80.82,
        "black-b": 31.008,
        "white-b": 82.97,
    }
    for index, i in enumerate(filepaths):
        times, pos_first, pos_second = load_data(i)

        vel_first = differentiate(pos_first, times)
        vel_second = differentiate(pos_second, times)
        plot_and_save(times, vel_first, f"graphs/{index}rome")
        # plot_and_save(times, vel_second, "eome")


def plot_and_save(x, y, filename) -> None:
    plt.plot(x, y)
    plt.savefig(filename)
    plt.clf()


def load_data(file_path: str) -> tuple[list[float]]:
    data = np.loadtxt(file_path, delimiter=",", skiprows=3)
    times = data[:, 0]
    pos_first = data[:, 1:3]
    pos_second = data[:, 3:-1]
    return times, pos_first, pos_second


def differentiate(values: list[list[float]], times: list[float]) -> list[list[float]]:
    # return np.diff(values, axis=0) / np.vstack(np.diff(times))
    return np.gradient(values, times, axis=0)


def momentum(mass: float, velocity: list[float]) -> list[float]:
    return mass * velocity


def kinetic_energy(mass: float, velocity: list[float]) -> list[float]:
    return 0.5 * mass * np.sum(velocity**2, axis=1)


main()
