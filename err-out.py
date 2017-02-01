#! /usr/bin/python
from __future__ import print_function
import sys
from time import sleep
from random import choice
from datetime import datetime


choices = (
    (sys.stderr, 'error   '),
    (sys.stdout, 'standard')
)

try:
    while True:
        sleep(1)
        out, status = choice(choices)
        print("This is {} message. Emitted at {}".format(status, datetime.now()), file=out)
except KeyboardInterrupt:
    sys.exit()
