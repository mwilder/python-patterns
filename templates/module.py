#!/usr/bin/env python

import sys
import os
import logging

# Script versions
__version__ = "0.0.0"
__prog__version__ = "{} {}".format(os.path.basename(__file__), __version__)

#----------------------------------------
# Template class
#----------------------------------------
class TempClass:
    """A template class"""

    def __init__(self):
        logging.info("Class created")

#----------------------------------------
# Main program
#----------------------------------------
if __name__ == "__main__":
    print "Version: ", __prog__version__
    print """\
    This is a template module.
    It should be imported into a script, not executed."""
