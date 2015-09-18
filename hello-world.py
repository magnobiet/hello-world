#!/usr/bin/python

"""
"
" Execution:    python hello-world.py
"
"""

import sys

if len(sys.argv) > 1:
    print 'Hello World ' + str(sys.argv[1]) + '!'
else:
    print 'Hello World!'
