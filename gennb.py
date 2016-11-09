#!/usr/bin/env python
"""
usage: gennb.py [-h] [--lines LINES] [--cells CELLS] fname

positional arguments:
  fname

optional arguments:
  -h, --help     show this help message and exit
  --lines LINES
  --cells CELLS
"""

from nbformat import v4, write

def generate_notebook(fname, nlines=10, ncells=100):
    """Generate a notebook to test loading time

    fname: destination filename
    nlines: number of lines of input/output per cell
    ncells: number of cells
    """
    nb = v4.new_notebook()
    source = '\n'.join([
        'print(%i)' % i for i in range(nlines)
    ])
    output = v4.new_output('stream', text='\n'.join(map(str, range(nlines))))
    nb.cells = [
        v4.new_code_cell(source, outputs=[output])
        for i in range(ncells)
    ]
    with open(fname, 'w') as f:
        write(nb, f)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--lines', type=int, default=10)
    parser.add_argument('--cells', type=int, default=100)
    parser.add_argument('fname', type=str, default='bignb.ipynb')
    args = parser.parse_args()
    fname = args.fname
    if not fname.endswith('.ipynb'):
        fname += '.ipynb'
    generate_notebook(fname, args.lines, args.cells)
