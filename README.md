# commutable-perf

This project addresses performance enhancements for the
[**commutable** library](https://github.com/nteract/commutable).

## Motivation

The loading of the notebooks right now is optimized for accuracy. The next
goal is to improve performance from the current baseline. This project provides
a focused attempt to get notebook loading (and likely saving) down to
reasonable numbers for frequent users. Additional information is available in
this issue: https://github.com/nteract/commutable/issues/51.

## Optimization targets for performance

### Multiline cleaning of notebooks

One culprit contributing to slow performance is the number of chained
`.update` and other operations during multiline cleaning of the notebooks.

## Notebook generation tool

`gennb.py` generates a notebook for performance measurement of notebook
loading. The following is the usage of `gennb.py`:

```
usage: gennb.py [-h] [--lines LINES] [--cells CELLS] fname

positional arguments:
  fname            output filename for notebook

optional arguments:
  -h, --help       show this help message and exit
  --lines LINES    number of lines of input/output per cell
  --cells CELLS    number of cells
```
