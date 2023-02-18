# Data Plotter

|           |                                                                                 |
| --------- | ------------------------------------------------------------------------------- |
| Name      | Data Plotter                                                                    |
| Version   | v1.0.0                                                                          |
| DockerHub | [weevenetwork/data-plotter](https://hub.docker.com/r/weevenetwork/data-plotter) |
| Authors   | Jakub Grzelak                                                                   |

- [Data Plotter](#data-plotter)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

This module collects some amount of data (Sample Size) and then plots them together. Later the module sends the graph as the PNG file to the next module.

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name                    | Environment Variables | type    | Description                                                                                                                  |
| ----------------------- | --------------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------- |
| X Axis Input Data Label | X_AXIS_DATA           | string  | Input data label that holds data points for x axis.                                                                          |
| Y Axis Input Data Label | Y_AXIS_DATA           | string  | Input data label that holds data points for y axis.                                                                          |
| Sample Size             | SAMPLE_SIZE           | integer | Number of data points to plot, i.e. if sample size is 10 then every 10 received data points the graph is plotted and output. |
| Graph X Axis Name       | X_AXIS_LABEL          | string  | Name of the graph x axis.                                                                                                    |
| Graph Y Axis Name       | Y_AXIS_LABEL          | string  | Name of the graph y axis.                                                                                                    |
| Graph Title             | GRAPH_TITLE           | string  | Title of the graph.                                                                                                          |
| Graph Color             | GRAPH_COLOR           | string  | Color of the graph (`red`, `blue`, `green`, `cyan`, `magenta`, `yellow`, `black`).                                           |
| Graph Linestyle         | GRAPH_LINESTYLE       | string  | Linestyle of the graph (`solid`, `dashed`, `dashdot`, `dotted`).                                                             |
| Graph Marker            | GRAPH_MARKER          | string  | Marker of the graph (`.`, `o`, `v`, `^`, `<`, `>`, `*`, `+`, `x`).                                                           |
| Grid Lines              | GRID_LINES            | string  | Configure the grid lines by selecting the axis to apply the changes on (`None`, `both`, `x`, `y`).                           |
| Output Label            | OUTPUT_LABEL          | string  | The output label at which graph file is dispatched.                                                                          |

### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output) |
| EGRESS_URLS           | string | HTTP ReST endpoints for the next module        |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

## Dependencies

```txt
bottle
requests
matplotlib
```

## Input

Input to this module is:

* JSON body single object, example:

```json
{
    "temperature": 12,
    "timestamp": "12:50"
}
```

* array of JSON body objects, example:

```json
[
    {
        "temperature": 12,
        "pressure": 14
    },
    {
        "temperature": 15,
        "pressure": 17
    }
]
```

## Output

Output of this module is a PNG file with the plotted graph sent to the next module.
