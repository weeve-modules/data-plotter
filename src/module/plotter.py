import matplotlib.pyplot as plt
from .params import PARAMS


def plot_graph(x_axis, y_axis):
    # plotting the points
    plt.plot(
        x_axis,
        y_axis,
        color=PARAMS["GRAPH_COLOR"],
        linestyle=PARAMS["GRAPH_LINESTYLE"],
        marker=PARAMS["GRAPH_MARKER"],
    )
    plt.xlabel(PARAMS["X_AXIS_LABEL"])
    plt.ylabel(PARAMS["Y_AXIS_LABEL"])
    plt.title(PARAMS["GRAPH_TITLE"])

    if not PARAMS["GRID_LINES"] == "None":
        plt.grid(axis=PARAMS["GRID_LINES"])

    # save plot to this location
    plt.savefig("assets/chart.png")
