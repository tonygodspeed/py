#!/usr/bin/env python
#coding=utf8

from MR_BASE import *

reload(sys)
sys.setdefaultencoding("utf-8")

"""
class MR_RECOM_SHOW(mr_base):
	def __init__(self):
		mr_base.__init__(self, "", "ACT_RECOM_SHOW_MINI")

	def ProcessMapper(self,value):
		words = value.split("|")

		r = ["mac","ver","sp_trigger"]
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
			line = dict["mac"] + "\t" + dict["ver"] + "\t" + dict["sp_trigger"]
			#config.appendlist(line)
			print(self.act_type + "\t" + line+"\n")
		pass

	def InitReducer(self,value):
		print("========================"+value+"===================")
		print("MAC\tVER\tsp_trigger")
		print("s\ts\ti")

	def ProcessReducer(self,value):
		try:
			key, value = value.split('\t', 1)
			if len(value) > 0:
				print(value)
		except ValueError:
			return

mr_obj = MR_RECOM_SHOW()
"""


str_act = "ACT_RECOM_SHOW_MINI"
class MR_RECOM_SHOW(mr_base):
	def __init__(self):
		mt_type = [
			{'key': 'VER', 'type': 's', 'mt': r'.*VER:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'CHID', 'type': 's', 'mt': r'CHID:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'MAC', 'type': 's', 'mt': r'MAC:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'sp_trigger', 'type': 'i', 'mt': r'sp_trigger:' + common_def.MT_VALUE_VALID_POSTFIX},
			{'key': 'org', 'type': 'i', 'mt': common_def.MT_VALUE_BEFORE('U'), 'cb_kv': self.MapperKvCb},
		]
		mr_base.__init__(self, mt_type, str_act)

	def MapperKvCb(self, key, data):
		v = 0
		if (key == "org"):
			if len(data) > 0:
				try:
					# v = data[1:] #temp.split(":",1)
					res = re.findall(".*from:+(\d).*$", data, re.IGNORECASE)
					if res:
						v = res[0]
				except Exception, message:
					v = 0

		return v


mr_obj = MR_RECOM_SHOW()

if __name__ == '__main__':
	test_str = r'01:37| [INFO]: <SRC:KWSHELLEXT_1.0.6.9030_MUSIC8310BDS1|S:RECOM_TIPS|PROD:KWSHELLEXT|DISVER:1.0.6.9040|OS:6.1.7601.2_Service Pack 1|PLAT:WIN32|VER:1.0.2.0|GID:1182|CHID:MUSIC8310BDS1|PN:RecomTips.exe|MAC:00E04C49E526|UAC:1|ADMIN:1|ST:1467648092|CFGVER:5|ACT:ACT_RECOM_SHOW_MINI|sp_trigger:0||{}|U:>(114.103.122.85)TM:1467648096'
	mr_obj.LocalTest(test_str)
	pass