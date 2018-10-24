#!/usr/bin/env python

from operator import itemgetter
import sys
import os
sys.path.append('/data/client/code/py/')
from dispatcher import Dispatcher
import common_def

def statistics(file):
	if common_def.IS_LINUX_FILE:
		fw = open('/tmp/result.txt','w')
		origin = sys.stdout
		sys.stdout = fw

	current_word = None
	current_count = 0
	key = None
	c_key = ""
	disp = Dispatcher()
	prefix_len = len(common_def.WORD_COUNT)
	for line in file:
		l = line.strip()
		npos = l.find(common_def.WORD_COUNT)
		if npos >= 0:
			key = l[npos + prefix_len:]
			if current_word == key:
				current_count +=1
			else:
				if current_word:
					print "%s\t%s" % (current_word, current_count)
				current_count = 1
				current_word = key
		else:
			spos = 0
			epos = l.find("\t",spos)
			if spos != -1 and epos != -1:
				kw = l[spos:epos]
				if kw != c_key:
					disp.ReducerInit(kw)
					c_key = kw
				disp.ReducerDispatch(kw,l)
			else:
				continue

	if key == current_word and key is not None:
		print "%s\t%s" % (current_word, current_count)

	if common_def.IS_LINUX_FILE:
		sys.stdout = origin
		fw.close()

if sys.platform != "win32":
	statistics(sys.stdin)
