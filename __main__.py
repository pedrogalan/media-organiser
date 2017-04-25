#!/usr/bin/python

from sys import argv, exit
from Runner import Runner

if len(argv) < 3 or len(argv) > 4:
    print "Usage: " + argv[0] + " source-path destination-path [max-files-to-rename]"
    exit(1)

Runner(argv).run()
