#!/usr/bin/env python

import sys
import time
import cPickle as pickle
import os
import hashlib
import datetime
import subprocess
import datetime
from crontab import CronTab
from scapy.all import *
from fsc import *
from capture import *
from hostComp import *
from rules import *
from logger import *
from multiprocessing import Process

print 'Welcome to HybrIDS'

tasks = raw_input('Start host and network components?\n')

if tasks == 'y' or 'yes':
   hidsProc = Process(target=hComp)
   nidsProc = Process(target=cap)
   hidsProc.start()
   nidsProc.start()
   hidsProc.join()
   nidsProc.join()
else:
   tasks = raw_input('Which individual component to start?')
   if tasks == 'host':
      hidsProc = Process(target=hComp)
      hidsProc.start()
      hidsProc.join()
   elif tasks == 'network':
      nidsProc = Process(target=cap)
      nidsProc.start()
      nidsProc.join()
   else:
      print 'Hybrids not started'
      print 'Exiting...'
      exit(-1)