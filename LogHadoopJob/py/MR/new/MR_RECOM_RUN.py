#!/usr/bin/env python
# coding=utf8
from MR_BASE import *

reload(sys)
sys.setdefaultencoding("utf-8")

"""
class MR_RECOM_RUN(mr_base):
	def __init__(self):
		mr_base.__init__(self, "", "ACT_RECOM_EXC_KUWO")

	def ProcessMapper(self,value):

		words = value.split("|")

		r = ["mac","ver","lst_err"]
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
			line = dict["mac"] + "\t" + dict["ver"] + "\t" + dict["lst_err"]
			#config.appendlist(line)
			print(self.act_type + "\t" + line+"\n")
		pass

	def InitReducer(self,value):
		print("========================"+value+"===================")
		print("MAC\tVER\tlst_err")
		print("s\ts\ti")

	def ProcessReducer(self,value):
		try:
			key, value = value.split('\t', 1)
			if len(value) > 0:
				print(value)
		except ValueError:
			return

mr_obj = MR_RECOM_RUN()
"""

str_act = "ACT_RECOM_EXC_KUWO"
class MR_RECOM_RUN(mr_base):
	def __init__(self):
		mt_type = [
			{'key': 'VER', 'type': 's', 'mt': r'.*VER:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'CHID', 'type': 's', 'mt': r'CHID:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'MAC', 'type': 's', 'mt': r'MAC:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'lst_err', 'type': 'i', 'mt': r'lst_err:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'org', 'type': 'i', 'mt': common_def.MT_VALUE_BETWEEN('path_exist', 'U'), 'cb_kv': self.MapperKvCb},
		]
		mr_base.__init__(self, mt_type, str_act)

	def MapperKvCb(self, key, data):
		v = 0
		if (key == "org"):
			if len(data) > 0:
				try:
					# v = data[1:] #temp.split(":",1)
					res = re.findall(".*\|from:+(\d).*$", data, re.IGNORECASE)
					if res:
						v = res[0]
				except Exception, message:
					v = 0

		return v


mr_obj = MR_RECOM_RUN()

if __name__ == '__main__':
	test_str = r'00:22| [INFO]: <SRC:KWSHELLEXT_1.0.6.9030_MUSIC8300PQ|S:1005|PROD:KWSHELLEXT|DISVER:1.0.6.9030|OS:10.0.10586.2_|PLAT:X64|VER:1.0.1.2|GID:1118|CHID:MUSIC8300PQ|PN:rundll32.exe|MAC:000000000000|UAC:1|ADMIN:0|ST:1467647942|ACT:ACT_RECOM_EXC_KUWO|lst_err:0|path_exist:0|:1|{}|U:>(123.186.80.132)TM:1467648021'
	mr_obj.LocalTest(test_str)
	pass
