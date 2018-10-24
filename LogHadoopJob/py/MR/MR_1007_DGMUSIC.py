#!/usr/bin/env python
#coding=utf8

from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")


str_act = "ACT_RECOM_DGMUSIC"
class MR_1007_DGMUSIC(mr_base):
	def __init__(self):
		mt_type = [
			{'key': 'VER', 'type': 's', 'mt': r'.*VER:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'CHID', 'type': 's', 'mt': r'CHID:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'MAC', 'type': 's', 'mt': r'MAC:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'ret', 'type': 'i', 'mt': r'ret:' + common_def.MT_VALUE_VALID_POSTFIX},
			{'key': 'subret', 'type': 'i', 'mt': r'subret:' + common_def.MT_VALUE_VALID_POSTFIX},
			{'key': 'downused', 'type': 'i', 'mt': r'downused:' + common_def.MT_VALUE_VALID_POSTFIX},
			{'key': 'unzipused', 'type': 's', 'mt': r'unzipused:' + common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
		]
		mr_base.__init__(self, mt_type, str_act)

mr_obj = MR_1007_DGMUSIC()

if __name__ == '__main__':
	test_str = r'<SRC:KWSHELLEXT_1.0.6.9030_MUSIC8310PT|S:1007|PROD:KWSHELLEXT|DISVER:1.0.6.9051|OS:10.0.10586.2_|PLAT:X64|VER:1.0.1.3|GID:1269|CHID:MUSIC8310PT|PN:rundll32.exe|MAC:382C4A1BE52F|UAC:1|ADMIN:0|ST:1472400045|CFGVER:8|ACT:ACT_RECOM_DGMUSIC|ret:1|subret:-1|downused:0|unzipused:0|{}|U:>(58.59.216.208)TM:1472400046'
	#test_str = r'00:00| [INFO]: <SRC:KWSHELLEXT_1.0.6.9030_funmusic|S:1005|PROD:KWSHELLEXT|DISVER:1.0.6.9030|OS:6.1.7601.2_Service Pack 1|PLAT:WIN32|VER:1.0.1.3|GID:1339|CHID:funmusic|PN:rundll32.exe|MAC:24FD52817184|UAC:0|ADMIN:1|ST:1467648278|ACT:ACT_RECOM_START|init_err:2|{}|U:>(183.93.232.254)TM:1467648001'
	#'00:00| [INFO]: <SRC:|ACT:ACT_RECOM_START|init_err:0|S:KWPRMODULE|PROD:KWSHELLEXT|VER:1.0.0.7|PLAT:WIN32|FROM:|GID:|CIN:|MAC:00E0702B553D|X64:1|UAC:0|ADMIN:1|OS:6.1.7601|MN:rundll32.exe|INT:1970-01-01|{}|U:>(112.239.100.203)TM:1467734403'

	mr_obj.LocalTest(test_str)
	pass
