#!/usr/bin/env python
"""A boilerplate script to be customized for data projects.

This script-level docstring will double as the description when the script is
called with the --help or -h option.

"""

import argparse
import contextlib
import io
import logging
import sys

#
from pathlib import Path

#
ENCODE_IN = 'utf-8'
ENCODE_OUT = 'utf-8'

log = logging.getLogger(Path(__file__).stem)


def manipulate_data(data):
    """This function is where the real work happens (or at least starts).

    Probably you should write some real documentation for it.

    Arguments:

    * data_in: the data to be manipulated

    """
    log.info("Doing some fun stuff here!")
    return data


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-i', '--infile',
                        type=lambda x: open(x, encoding=ENCODE_IN),
                        default=io.TextIOWrapper(
                            sys.stdin.buffer, encoding=ENCODE_IN)
                        )
    parser.add_argument('-o', '--outfile',
                        type=lambda x: open(x, 'w', encoding=ENCODE_OUT),
                        default=io.TextIOWrapper(
                            sys.stdout.buffer, encoding=ENCODE_OUT)
                        )
    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument('-v', '--verbose', action='store_const',
                           const=logging.DEBUG, default=logging.INFO)
    verbosity.add_argument('-q', '--quiet', dest='verbose',
                           action='store_const', const=logging.WARNING)
    return parser.parse_args()


def read_infile(instream):
    """Convert raw input for to a manipulatable format.

    Arguments:

    *Instream: a file-like object

    """
    return infile.read()


def main():
    args = parse_args()
    logging.basicConfig(level=args.verbose)
    data = read_instream(args.infile)
    results = manipulate_data(data)
    args.outfile.write(results)

if __name__ == "__main__":
    main()
