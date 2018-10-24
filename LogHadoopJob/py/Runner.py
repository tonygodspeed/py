#!/usr/bin/env python

import sys
import os
import re
import unittest

sys.path.append('/data/client/code/py/')
import mapper
import reducer
import time
import codecs
import shutil;

m_path = "F:\\1.txt"
r_path = "F:\\2.txt"
s_path = "F:\\4.txt"
res_path = "F:\\3.txt"

need_sort = True

class Test(unittest.TestCase):
	def testAMapper(self):
		fw = open(r_path,'w')
		origin = sys.stdout
		sys.stdout = fw

		#fh = open(m_path)
		fh = codecs.open(m_path)

		# time.sleep(100)

		mapper.statistics(fh)

		fh.close()
		sys.stdout = origin
		fw.close()
		pass

	def testBSort(self):
		if need_sort:
			fh = codecs.open(r_path)
			lt = []
			for l in fh:
				l = l.strip()
				lt.append(l + "\n")
			lt.sort()
			frh= open(s_path,'w')
			#for l in lt:
			frh.writelines(lt)
			#buf = "".join(lt)
			#fh.write(buf)
			fh.close()
			frh.close()
		else:
			if os.path.isfile(s_path):
				os.remove(s_path)
			shutil.copyfile(r_path,s_path);

	def testCReducer(self):
		fw = open(res_path,'w')
		origin = sys.stdout
		sys.stdout = fw
		#fh = open(s_path)
		fh = codecs.open(s_path)
		reducer.statistics(fh)
		fh.close()
		sys.stdout = origin
		fw.close()
		pass



if __name__ == '__main__':
	#unittest.TestLoader().loadTestsFromName("Test")

	import dispatcher;
	dispatcher.InitHandlers();
	unittest.main()

	#txt_mapper()