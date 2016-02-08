#!/usr/bin/python

import sys, os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path = os.path.join(BASE_DIR, sys.path)
from django.core.servers.fastcgi import runfastcgi


basepath = 'nuclearpowerplantconference.com/kunden/homepages/13/d609847479/htdocs'

sys.path.insert(0, basepath + '/.local/lib')
sys.path.insert(0, basepath + '/www/DISS')

os.environ['DJANGO_SETTINGS_MODULE'] = 'DISS.settings'

runfastcgi(method='threaded', daemonize='false')