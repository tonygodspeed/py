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
class MR_RECOM_SHOW(mr_base_ex):
	def __init__(self):
		mr_base_ex.__init__(self,str_act)
		self.res_type = ["s","s","s","s","i","i","i","i","i","i","i","i"];
		self.res_name = ["VER","CHID","MAC","MCID","sp_trigger","is_sign","show_sign_in","from","green_shot","is_green","is_auto"];

	'''
		mt_type = [
			{'key': 'VER', 'type': 's', 'mt': r'.*VER:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'CHID', 'type': 's', 'mt': r'CHID:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'MAC', 'type': 's', 'mt': r'MAC:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'sp_trigger', 'type': 'i', 'mt': r'sp_trigger:' + common_def.MT_VALUE_VALID_POSTFIX},
			{'key': 'org', 'type': 's', 'mt': common_def.MT_VALUE_BEFORE('U'), 'cb_kv': self.MapperKvCb},
		]
		mr_base.__init__(self, mt_type, str_act)

	def MapperKvCb(self, key, data):
		v = 0
		if (key == "org"):
			if len(data) > 0:
				try:
					# v = data[1:] #temp.split(":",1)
					res = re.findall("(from:.*)\|{}.*$", data, re.IGNORECASE)
					if res:
						v = res[0]
				except Exception, message:
					v = 0

		return v
	'''

mr_obj = MR_RECOM_SHOW()

if __name__ == '__main__':
	#test_str = r'01:37| [INFO]: <SRC:KWSHELLEXT_1.0.6.9030_MUSIC8310BDS1|S:RECOM_TIPS|PROD:KWSHELLEXT|DISVER:1.0.6.9040|OS:6.1.7601.2_Service Pack 1|PLAT:WIN32|VER:1.0.2.0|GID:1182|CHID:MUSIC8310BDS1|PN:RecomTips.exe|MAC:00E04C49E526|UAC:1|ADMIN:1|ST:1467648092|CFGVER:5|ACT:ACT_RECOM_SHOW_MINI|sp_trigger:0||{}|U:>(114.103.122.85)TM:1467648096'
	#test_str = r'02:39| [INFO]: <SRC:KWSHELLEXT_1.0.6.9012_MUSIC8120AN0|S:RECOM_TIPS|PROD:KWSHELLEXT|DISVER:1.0.6.9061|OS:5.1.2600.2_Service Pack 3|PLAT:WIN32|VER:1.0.2.5|GID:622|CHID:MUSIC8120AN0|PN:RecomTips.exe|MAC:002682B3E8AC|UAC:0|ADMIN:1|ST:1472400148|CFGVER:9|ACT:ACT_RECOM_SHOW_MINI|sp_trigger:0|from:1|green_shot:0|is_green:0|{}|U:>(125.124.106.121)TM:1472400157'
	test_str = r'00:00| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8200P2T1|S:RECOM_TIPS|PROD:KWSHELLEXT|DISVER:1.0.6.9072|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.2.10|GID:2724|CHID:MUSIC8200P2T1|PN:RecomTips.exe|MAC:74D435F3944A|UAC:0|ADMIN:1|ST:1478534132|CFGVER:12|ACT:ACT_RECOM_SHOW_MINI|sp_trigger:0|is_sign:0|from:3|green_shot:0|is_green:0|{}|U:>(59.63.248.97)TM:1478534391'
	#test_str = r'05:32| [INFO]: <SRC:|S:RECOM_TIPS|PROD:KWSHELLEXT|DISVER:|OS:6.2.9200.2_|PLAT:X64|VER:1.0.2.20|GID:|CHID:|PN:RecomTips.exe|MAC:7845C403A55A|UAC:0|ADMIN:0|MVER:MUSIC_8.5.2.0|MCID:28479825|ST:1481774611|CFGVER:0|ACT:ACT_RECOM_SHOW_MINI|sp_trigger:0|is_sign:1|show_sign_in:1|from:-1|green_shot:0|is_green:0|{}|U:>(111.207.202.8)TM:1481601933'
	mr_obj.LocalTest(test_str)
	pass