#!/usr/bin/env python
#coding=utf8

from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

"""
str_act = "ACT_RECOM_QUIT"
class MR_RECOM_QUIT(mr_base):
	def __init__(self):
		mr_base.__init__(self, "", str_act)

	def ProcessMapper(self,value):

		words = value.split("|")

		r = ["mac","ver","quit_err"]
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
			line = dict["mac"] + "\t" + dict["ver"] + "\t" + dict["quit_err"]
			#config.appendlist(line)
			print(self.act_type + "\t" + line+"\n")
		pass

	def InitReducer(self,value):
		print("========================"+value+"===================")
		print("MAC\tVER\tquit_err")
		print("s\ts\ti")

	def ProcessReducer(self,value):
		try:
			key, value = value.split('\t', 1)
			if len(value) > 0:
				print(value)
		except ValueError:
			return

mr_obj = MR_RECOM_QUIT()
"""

str_act = "ACT_RECOM_QUIT"
class MR_RECOM_QUIT(mr_base):
	def __init__(self):
		mt_type = [
			{'key': 'VER', 'type': 's', 'mt': r'.*VER:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'CHID', 'type': 's', 'mt': r'CHID:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'MAC', 'type': 's', 'mt': r'MAC:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'quit_err', 'type': 'i', 'mt': r'quit_err:' + common_def.MT_VALUE_VALID_POSTFIX},
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


mr_obj = MR_RECOM_QUIT()

if __name__ == '__main__':
	test_str = r'00:31| [INFO]: <SRC:KWSHELLEXT_1.0.6.9030_MUSIC8310BDS1|S:RECOM_TIPS|PROD:KWSHELLEXT|DISVER:1.0.6.9040|OS:6.1.7600.2_|PLAT:WIN32|VER:1.0.2.0|GID:1203|CHID:MUSIC8310BDS1|PN:RecomTips.exe|MAC:F04DA26B8CEC|UAC:0|ADMIN:1|ST:1467236451|CFGVER:5|ACT:ACT_RECOM_QUIT|quit_err:16||{}|U:>(180.191.155.250)TM:1467648029'
	mr_obj.LocalTest(test_str)
	pass