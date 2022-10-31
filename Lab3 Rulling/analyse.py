timport numpy as np
import matplotlib.pyplot as plt


def read_data(filename: str) -> tuple[np.ndarray]:
    with open(filename, "r") as f:
        pass
        # TODO Format data


def f(phi: float, phi_dot: float) -> float:
    pass


def plot_results(
    filename: str,
    x_values_list: list[np.ndarray],
    y_values_list: list[np.ndarray],
    xlabel: str,
    ylabel: str,
    labels: list[str],
) -> None:
    for x_values, y_values, label in zip(x_values_list, y_values_list, labels):
        plt.plot(x_values, y_values, label=label)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)

    plt.legend(fontsize=18)
    plt.grid()

    plt.savefig(filename, bbox_inches="tight")


def phi_d2(phi: float, phi_d1: float, w0: float, delta: float) -> float:
    pass


if __name__ == "__main__":
    pass
