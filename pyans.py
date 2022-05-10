#!/usr/bin/env python3
#
# // PyANS² a simple ANSI scroller
# Basic ANSI/ASCII scroller for python3
# -: @sairukau :-
#
# ISSUES:
#  Colours aren't quite right
#  Doesn't support all ansi correctly
#
# CHANGELOG:
#  v01: initial version, rewrite of pyANS

import sys, argparse
from pya_config import Config
from pya_logger import Logger
from pya_library import Library
from pya_term import Terminal

logger = Logger('MAIN')

def main(args=None):

    config = Config()
    library = Library()
    term = Terminal()
    config.read()

    if args.update_cache:
        library.cache_build()
        exit()
    else:
        library.cache_read()

    while True:
        ans_view = library.select()
        ans_data = library.load(ans_view)
        term.display(ans_data)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='pyANS.nfo')
    parser.add_argument('--update-cache', const=True, nargs='?')

    if sys.version_info<(3,0,0):
        sys.stderr.write('Python 3 is required')
        exit(1)

    main(parser.parse_args())