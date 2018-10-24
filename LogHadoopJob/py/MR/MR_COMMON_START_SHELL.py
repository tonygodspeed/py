#!/usr/bin/env python
#coding=utf8

from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

class MR_COMMON_START_SHELL(mr_base):
	def __init__(self):
		mr_base.__init__(self,"","COMMON_START_SHELL")

	def ProcessMapper(self,value):

		words = value.split("|")

		r = ["mac","ver","s", "DISVER", "CHID"]
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
#[4176] (26402124)#Kw#[KwStatTask.cpp:202](10544)- *INFO* url = 2%09<SRC:KWSHELLEXT_1.0.6.9051_MUSIC8720BCS14|S:SHELLEXT|PROD:KWSHELLEXT|DISVER:1.0.6.9051|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.6.9051|GID:4439|CHID:MUSIC8720BCS14|PN:explorer.exe|MAC:D8CB8A68A2AC|UAC:1|ADMIN:1|ST:1495445369|CFGVER:0|ACT:COMMON_START_SHELL||{}|U:>

		if len(r) == 0:
			line = dict["mac"] + "\t" + dict["ver"] + "\t" + dict["s"] + "\t" + dict["DISVER"] + "\t" + dict["CHID"]
			#config.appendlist(line)
			print(self.act_type + "\t" + line+"\n")
		pass

	def InitReducer(self,value):
		print("========================"+value+"===================")
		print("MAC\tVER\ts\tDISVER\tCHID")
		print("s\ts\ts\ts\ts")

	def ProcessReducer(self,value):
		try:
			key, value = value.split('\t', 1)
			if len(value) > 0:
				print(value)
		except ValueError:
			return

mr_obj = MR_COMMON_START_SHELL()