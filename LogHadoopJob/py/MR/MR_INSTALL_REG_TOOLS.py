#!/usr/bin/env python
#coding=utf8

from MR_BASE import *

reload(sys)
sys.setdefaultencoding("utf-8")


class MR_INSTALL_REG_TOOLS(mr_base):
	def __init__(self):
		mr_base.__init__(self, "", "ACT_INSTALL_REG_TOOLS")

	def ProcessMapper(self,value):

		words = value.split("|")

		r = ["mac","ver","reg_ret","sub_ret","is_upgrade","srcid","reg_desc"]
		dict = {}
		for word in words:
			if word.find(":") == -1:
				continue

			k,v = word.split(":",1)

			for key in r:
				if re.match(key,k, re.IGNORECASE):#.find(key) != -1:
					if len(v) == 0:
						v = "0"
					dict[key] = v
					r.remove(key)
					break
			if len(r) == 0:
				break
		if len(r) == 0:
			line = dict["mac"] + "\t" + dict["ver"] + "\t" + dict["reg_ret"]+ "\t" + dict["sub_ret"]+ "\t" + dict["is_upgrade"]+ "\t" + dict["srcid"]+ "\t" + dict["reg_desc"]
			#config.appendlist(line)
			print(self.act_type + "\t" + line+"\n")
		pass

	def InitReducer(self,value):
		print("========================"+value+"===================")
		print("MAC\tVER\treg_ret\tsub_ret\tis_upgrade\tsrcid\treg_desc")
		print("s\ts\ti\ti\ti\ts\ts")

	def ProcessReducer(self,value):
		try:
			key, value = value.split('\t', 1)
			if len(value) > 0:
				print(value)
		except ValueError:
			return

mr_obj = MR_INSTALL_REG_TOOLS()