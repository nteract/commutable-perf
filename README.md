# commutable-perf

Addressing performance of the commutable library (https://github.com/nteract/commutable/issues/51).

The loading of the notebooks right now has fairly absymal performance. This is an attempt to get notebook loading (and likely saving) down to reasonable numbers. One culprit is the amount of chained `.update` and other operations during multiline cleaning of the notebooks.
