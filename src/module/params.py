from os import getenv

PARAMS = {
    "X_AXIS_DATA": getenv("X_AXIS_DATA", "temperature"),
    "Y_AXIS_DATA": getenv("Y_AXIS_DATA", "timestamp"),
    "SAMPLE_SIZE": int(getenv("SAMPLE_SIZE", 100)),
    "X_AXIS_LABEL": getenv("X_AXIS_LABEL", "Sensor Data"),
    "Y_AXIS_LABEL": getenv("Y_AXIS_LABEL", "Timestamp"),
    "GRAPH_TITLE": getenv("GRAPH_TITLE", "Sensor Data Graph"),
    "GRAPH_COLOR": getenv("GRAPH_COLOR", "red"),
    "GRAPH_LINESTYLE": getenv("GRAPH_LINESTYLE", "dashed"),
    "GRAPH_MARKER": getenv("GRAPH_MARKER", "o"),
    "GRID_LINES": getenv("GRID_LINES", "both"),
    "OUTPUT_LABEL": getenv("OUTPUT_LABEL", "chart-file"),
}
