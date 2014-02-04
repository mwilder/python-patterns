#!/usr/bin/env python

import sys
import os
import logging
import numpy as np
import matplotlib.pyplot as plt

# Script versions
__version__ = "0.1.0"
__prog__version__ = "{} {}".format(os.path.basename(__file__), __version__)

#----------------------------------------
# Plot classes
#----------------------------------------

# Simple line plot
class PlotLine:
    """A simple line plot"""

    def __init__(self):
        logging.debug("Class created")

    def drawData(self, y):
        x = np.linspace(1, len(y), len(y))
        plt.plot(y)

    def show(self):
        plt.show()

# Time slot graph
class TimeSlot:
    """A time slot graph, using broken horizontal bars."""

    def __init__(self):
        logging.debug("TimeSlot class created")
        self.title = "TimeSlot"
        self.slots = []

    def addSlot(self, data):
        self.slots.append(data)

    def draw(self):
        y_pos = 0
        y_ticks = []
        y_labels = []
        for s in self.slots:
            logging.debug("{}, ({}, {}), facecolors={}".format(s[0], s[1], s[2], s[3]))
            plt.broken_barh(s[1], (y_pos, s[2]-1), facecolors=s[3])
            y_ticks.append(y_pos + s[2] / 2)
            y_labels.append(s[0])
            y_pos = y_pos + s[2]
        plt.ylim(0, y_pos)
        plt.yticks(y_ticks, y_labels)
        plt.title(self.title)

    def show(self):
        self.draw()
        plt.show()

#----------------------------------------
# Main program
#----------------------------------------
if __name__ == "__main__":
    import argparse
    import textwrap

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent("""
            Example graphs using matplotlib.
            
            Select plot type with '-p' switch."""),
        epilog=textwrap.dedent("""
            Version %s""" % (__version__)))
    # Positional arguments
    parser.add_argument("plot", type=int, nargs='+',
                        help="Select plot example")
    # Optional arguments
    parser.add_argument("-l", "--log", default='ERROR',
                        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                        help="logger level (default: %(default)s)")
    parser.add_argument("-s", "--subplot", type=int, default=0,
                        help="Select sub-plot example (default: %(default)i)")
    parser.add_argument("-V", "--version", action='version', version=__prog__version__)
    args = parser.parse_args()

    # ----------------------------------
    # Set logging level
    logging.basicConfig(level=getattr(logging, args.log.upper()))
    logging.debug("Debug logging enabled")    
    logging.info("Info logging enabled")

    # ----------------------------------
    # Example plots
    fig = plt.figure()
    fig_rows = len(args.plot)
    graph = 1
    for pt in args.plot:
        plt.subplot(fig_rows, 1, graph)
        graph+=1
        if (pt == 1):
            p = PlotLine()
            p.drawData([1, 1.5, 1.2, 1.5])
            p.drawData([2, 2.1, 2.2, 2.3, 2.4])
        elif (pt == 2):
            p = TimeSlot()
            p.title = "My time slot"
            p.addSlot(["Slot0", [(0,100)], 20, 'blue'])
            p.addSlot(["Slot1", [(10,60), (60,30)], 10, ('green', 'yellow')])
            p.addSlot(["Slot2", [(5,65)], 20, 'red'])
            p.draw()
        else:
            print "Unknown plot type: {}".format(p)

    plt.show()
