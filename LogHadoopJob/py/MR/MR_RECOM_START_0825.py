#!/usr/bin/env python
#coding=utf8

from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

"""
class MR_RECOM_START(mr_base):
	def __init__(self):
		mr_base.__init__(self, "", "ACT_RECOM_START")

	def ProcessMapper(self,value):

		words = value.split("|")

		r = ["mac","ver","init_err"]
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
			line = dict["mac"] + "\t" + dict["ver"] + "\t" + dict["init_err"]
			#config.appendlist(line)
			print(self.act_type + "\t" + line+"\n")
		pass

	def InitReducer(self,value):
		print("========================"+value+"===================")
		print("MAC\tVER\tinit_err")
		print("s\ts\ti")

	def ProcessReducer(self,value):
		try:
			key, value = value.split('\t', 1)
			if len(value) > 0:
				print(value)
		except ValueError:
			return

mr_obj = MR_RECOM_START()
"""


str_act = "ACT_RECOM_START"
class MR_RECOM_START(mr_base):
	def __init__(self):
		mt_type = [
			{'key': 'VER', 'type': 's', 'mt': r'.*VER:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'CHID', 'type': 's', 'mt': r'CHID:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'MAC', 'type': 's', 'mt': r'MAC:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'init_err', 'type': 'i', 'mt': r'init_err:' + common_def.MT_VALUE_VALID_POSTFIX},
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


mr_obj = MR_RECOM_START()

if __name__ == '__main__':
	test_str = r'00:00| [INFO]: <SRC:KWSHELLEXT_1.0.6.9030_funmusic|S:1005|PROD:KWSHELLEXT|DISVER:1.0.6.9030|OS:6.1.7601.2_Service Pack 1|PLAT:WIN32|VER:1.0.1.3|GID:1339|CHID:funmusic|PN:rundll32.exe|MAC:24FD52817184|UAC:0|ADMIN:1|ST:1467648278|ACT:ACT_RECOM_START|init_err:2|from:1|{}|U:>(183.93.232.254)TM:1467648001'
	mr_obj.LocalTest(test_str)
	pass
