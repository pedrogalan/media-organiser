#!/usr/bin/python

from sys import argv, exit
from Runner import Runner
import logging

logging.basicConfig(filename='/var/log/media-in-the-cloud.log', format='[%(asctime)s][%(levelname)s] %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

if len(argv) < 3 or len(argv) > 4:
    print "Usage: " + argv[0] + " source-path destination-path [max-files-to-rename]"
    exit(1)

Runner(argv).run()
