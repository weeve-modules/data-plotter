"""
This file implements module's main logic.
Data processing should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
from .params import PARAMS
from .plotter import plot_graph
from api.send_data import send_data

log = getLogger("module")

x_axis = []
y_axis = []


def record_data(data):
    global x_axis, y_axis

    # append data to x and y axis
    x_axis.append(data[PARAMS["X_AXIS_DATA"]])
    y_axis.append(data[PARAMS["Y_AXIS_DATA"]])

    if len(x_axis) == PARAMS["SAMPLE_SIZE"]:
        # plot graph
        plot_graph(x_axis, y_axis)

        # reset records
        x_axis = []
        y_axis = []

        # send graph
        send_error = send_data()
        if send_error:
            log.error(send_error)
        else:
            log.debug("Graph sent.")


def module_main(received_data: any) -> [any, str]:
    """
    Process received data by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        any: Processed data that are ready to be sent to the next module or None if error occurs.
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Processing ...")

    try:
        if type(received_data) == list:
            for data in received_data:
                record_data(data)

        else:
            record_data(received_data)

        return received_data, None

    except Exception as e:
        return None, f"Exception in the module business logic: {e}"
