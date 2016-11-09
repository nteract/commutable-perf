# commutable-perf

This project addresses performance enhancements for the commutable library (https://github.com/nteract/commutable/issues/51).

## Motivation

The loading of the notebooks right now is optimized for accuracy. The next
goal is to improve performance from the current baseline. This project provides
a focused attempt to get notebook loading (and likely saving) down to
reasonable numbers for frequent users.

## Optimization targets for performance

### Multiline cleaning of notebooks

One culprit contributing to slow performance is the number of chained
`.update` and other operations during multiline cleaning of the notebooks.

### Additional areas
