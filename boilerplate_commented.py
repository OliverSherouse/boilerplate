#!/usr/bin/env python
"""A boilerplate script to be customized for data projects.

This script-level docstring will double as the description when the script is
called with the --help or -h option.

"""

# Standard Library imports go here
import argparse
import contextlib
import io
import logging
import sys

# External library imports go here
#
# Standard Library from-style imports go here
from pathlib import Path

# External library from-style imports go here
#
# Ideally we all live in a unicode world, but if you have to use something
# else, you can set it here
ENCODE_IN = 'utf-8'
ENCODE_OUT = 'utf-8'

# Set up a global logger. Logging is a decent exception to the no-globals rule.
# We want to use the logger because it sends to standard error, and we might
# need to use the standard output for, well, output. We'll set the name of the
# logger to the name of the file (sans extension).
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
    # If user doesn't specify an input file, read from standard input. Since
    # encodings are the worst thing, we're explicitly expecting std
    parser.add_argument('-i', '--infile',
                        type=lambda x: open(x, encoding=ENCODE_IN),
                        default=io.TextIOWrapper(
                            sys.stdin.buffer, encoding=ENCODE_IN)
                        )
    # Same thing goes with the output file.
    parser.add_argument('-o', '--outfile',
                        type=lambda x: open(x, 'w', encoding=ENCODE_OUT),
                        default=io.TextIOWrapper(
                            sys.stdout.buffer, encoding=ENCODE_OUT)
                        )
    # Set the verbosity level for the logger. The `-v` option will set it to
    # the debug level, while the `-q` will set it to the warning level.
    # Otherwise use the info level.
    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument('-v', '--verbose', action='store_const',
                           const=logging.DEBUG, default=logging.INFO)
    verbosity.add_argument('-q', '--quiet', dest='verbose',
                           action='store_const', const=logging.WARNING)
    return parser.parse_args()


def read_instream(instream):
    """Convert raw input for to a manipulatable format.

    Arguments:

    *Instream: a file-like object

    """
    # If you need to read a csv, create a DataFrame, or whatever it might be,
    # do it here.
    return instream.read()


def main():
    args = parse_args()
    logging.basicConfig(level=args.verbose)
    data = read_instream(args.infile)
    results = manipulate_data(data)
    args.outfile.write(results)

if __name__ == "__main__":
    main()
