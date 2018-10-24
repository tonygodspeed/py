#!/usr/bin/env python

import sys
import os
import re
sys.path.append('/data/client/code/py/')
from dispatcher import Dispatcher
import common_def

def statistics(file):
	if common_def.IS_LINUX_FILE:
		fw = open('/tmp/ls.txt','w')
		origin = sys.stdout
		sys.stdout = fw

	disp = Dispatcher()
	for line in file:
		l = line.strip()

		act = ""
		res = re.findall("(ACT:|SUBKEY:)([^\|]*)\|",l,re.IGNORECASE)
		for k,v in res:
			if k == "ACT:":
				act = v + act
			else:
				act += "_" + v
		disp.MapperDispatch(act,l)

	if common_def.IS_LINUX_FILE:
		sys.stdout = origin
		fw.close()

if sys.platform != "win32":
	statistics(sys.stdin)