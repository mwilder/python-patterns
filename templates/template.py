#!/usr/bin/env python

# Imports
import sys
import os
import logging
import module

# Script versions
__version__ = "0.0.0"
__prog__version__ = "{} {}".format(os.path.basename(__file__), __version__)

#----------------------------------------
# Main program
#----------------------------------------
if __name__ == "__main__":
    import argparse
    import textwrap

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent("""
            Template python scrip
            Extend as needed"""),
        epilog=textwrap.dedent("""
            More details..."""))
    parser.add_argument("-l", "--log", default='ERROR',
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                        help="logger level (default: %(default)s)")
    parser.add_argument("-v", "--verbosity", type=int, default=0,
                        help="Unused verbosity setting (default: %(default)i)")
    parser.add_argument("-V", "--version", action='version', version=__prog__version__)
    args = parser.parse_args()

    print "Version: ", __prog__version__
    
    # Set logging level
    logging.basicConfig(level=getattr(logging, args.log.upper()))
    logging.debug("Debug logging enabled")    
    logging.info("Info logging enabled")
    logging.warning("Warning logging enabled")
    logging.error("Error logging enabled")
    logging.critical("Critical error logging enabled")

    # Use template module
    t = module.TempClass()
