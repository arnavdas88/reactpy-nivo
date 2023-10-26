# reactpy-nivo

A [Nivo Charts](https://nivo.rocks) component implemented in [ReactPy](https://github.com/reactive-python/reactpy)

## Installation

Installation through pip

```shell
$ pip3 install .
```

## Run Demo

All the demo code, exists in the `examples/` directory.

```shell 
$ cd examples/
```

### Bar Chart Demo
```shell
$ uvicorn sample_bar:app --reload
INFO:     Will watch for changes in these directories: ['.../reactpy-nivo/examples']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [17430] using WatchFiles
INFO:     Started server process [17480]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
![Bar Chart](https://raw.githubusercontent.com/arnavdas88/reactpy-nivo/nivo-component/docs/images/bar_chart.png)

### Line Chart Demo
```shell 
$ uvicorn sample_line:app --reload
INFO:     Will watch for changes in these directories: ['.../reactpy-nivo/examples']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [17430] using WatchFiles
INFO:     Started server process [17480]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
![Line Chart](https://raw.githubusercontent.com/arnavdas88/reactpy-nivo/nivo-component/docs/images/line_chart.png)