#!/usr/bin/env python3
"""
A boilerplate script to be customized for data projects.

This script-level docstring will double as the description when the script is
called with the --help or -h option.
"""

# Standard Library imports
import argparse
# import collections
# import csv
# import itertools
import logging

# External library imports
# import pandas as pd
# import numpy as np

# Standard Library from-style imports go here
from pathlib import Path

# External library from-style imports go here
# from matplotlib import pyplot as plt

__version__ = '0.1'

log = logging.getLogger(__name__ if __name__ != '__main__ '
                        else Path(__file__).stem)


def manipulate_data(data):
    """This function is where the real work happens (or at least starts).

    Probably you should write some real documentation for it.

    Arguments:

    * data: the data to be manipulated

    """
    log.info("Doing some fun stuff here!")
    return data


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', nargs='?', default='-')
    parser.add_argument('-ei', '--infile_encoding', default='utf-8')
    parser.add_argument('-o', '--outfile', default='-')
    parser.add_argument('-eo', '--outfile_encoding', default='utf-8')

    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument('-v', '--verbose', action='store_const',
                           const=logging.DEBUG, default=logging.INFO)
    verbosity.add_argument('-q', '--quiet', dest='verbose',
                           action='store_const', const=logging.WARNING)

    parser.add_argument('--version', action='version',
                        version=f'%(prog)s v{__version__}')

    args = parser.parse_args()
    args.infile = argparse.FileType(encoding=args.infile_encoding)(args.infile)
    args.outfile = argparse.FileType(
        mode='w',
        encoding=args.outfile_encoding,
        # newline='', # for csvs
    )(args.outfile)
    return args


def read_instream(instream):
    """Convert raw input for to a manipulable format.

    Arguments:

    * instream: a file-like object

    Returns: probably a DataFrame

    """
    log.info('Reading Input')
    return instream.read()


def main():
    args = parse_args()
    logging.basicConfig(level=args.verbose)
    data = read_instream(args.infile)
    results = manipulate_data(data)
    print(results, file=args.outfile)


if __name__ == "__main__":
    main()
