#!/usr/bin/env python
#coding=utf8

from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

class MR_DISP_START(mr_base):
	def __init__(self):
		mr_base.__init__(self,"","ACT_DISP_START")

	def ProcessMapper(self,value):

		words = value.split("|")

		r = ["mac","ver","chid"]
		dict = {}
		for word in words:
			if word.find(":") == -1:
				continue

			k,v = word.split(":",1)
			if len(v) > 0:
				for key in r:
					if re.match(key,k, re.IGNORECASE):#.find(key) != -1:
						dict[key] = v
						r.remove(key)
						break
			if len(r) == 0:
				break
		if len(r) == 0:
			line = dict["mac"] + "\t" + dict["ver"] + "\t" + dict["chid"]
			#config.appendlist(line)
			print(self.act_type + "\t" + line+"\n")
		else:
			print (self.act_type + "\t" + "error:" + value +"\n")
		pass

	def InitReducer(self,value):
		print("========================"+value+"===================")
		print("MAC\tVER\tchid")
		print("s\ts\ts")

	def ProcessReducer(self,value):
		try:
			key, value = value.split('\t', 1)
			if len(value) > 0:
				print(value)
		except ValueError:
			return

mr_obj = MR_DISP_START()