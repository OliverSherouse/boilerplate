#!/usr/bin/env python
"""A boilerplate script to be customized for data projects.

This script-level docstring will double as the description when the script is
called with the --help or -h option.

"""

# Standard Library imports
import argparse
import logging

# External library imports
# import pandas as pd
# import numpy as np


# Standard Library from-style imports go here
from pathlib import Path

# External library from-style imports go here
# from matplotlib import pyplot as plt

# Ideally we all live in a unicode world, but if you have to use something
# else, you can set it here
ENCODE_IN = 'utf-8'
ENCODE_OUT = 'utf-8'

log = logging.getLogger(
    __name__ if __name__ != '__main__ ' else Path(__file__).stem
)


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
    inft = argparse.FileType(encoding=ENCODE_IN)
    outft = argparse.filetype('w', encoding=ENCODE_OUT)  # , newline='')

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', nargs='?', type=inft, default=inft('-'))
    parser.add_argument('-o', '--outfile', type=outft, default=outft('-'))
    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument('-v', '--verbose', action='store_const',
                           const=logging.DEBUG, default=logging.INFO)
    verbosity.add_argument('-q', '--quiet', dest='verbose',
                           action='store_const', const=logging.WARNING)
    return parser.parse_args()


def read_instream(instream):
    """Convert raw input for to a manipulatable format.

    Arguments:

    * instream: a file-like object

    Returns: probably a DataFrame

    """
    return instream.read()


def main():
    args = parse_args()
    logging.basicConfig(level=args.verbose)
    data = read_instream(args.infile)
    results = manipulate_data(data)
    print(results, file=args.outfile)


if __name__ == "__main__":
    main()
