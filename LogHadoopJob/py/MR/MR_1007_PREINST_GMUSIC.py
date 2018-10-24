#!/usr/bin/env python
#coding=utf8

from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")


str_act = "ACT_RECOMLOADER_PREINST_GMUSIC"
class MR_1007_PREINST_GMUSIC(mr_base):
	def __init__(self):
		mt_type = [
			{'key': 'VER', 'type': 's', 'mt': r'.*VER:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'CHID', 'type': 's', 'mt': r'CHID:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'MAC', 'type': 's', 'mt': r'MAC:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'ret', 'type': 'i', 'mt': r'ret:' + common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
		]
		mr_base.__init__(self, mt_type, str_act)

mr_obj = MR_1007_PREINST_GMUSIC()

if __name__ == '__main__':
	test_str = r'<SRC:KWSHELLEXT_1.0.6.9030_MUSIC8310PT|S:1007|PROD:KWSHELLEXT|DISVER:1.0.6.9051|OS:10.0.10586.2_|PLAT:X64|VER:1.0.1.3|GID:1269|CHID:MUSIC8310PT|PN:rundll32.exe|MAC:382C4A1BE52F|UAC:1|ADMIN:0|ST:1472400045|CFGVER:8|ACT:ACT_RECOMLOADER_PREINST_GMUSIC|ret:1|{}|U:>(58.59.216.208)TM:1472400046'

	mr_obj.LocalTest(test_str)
	pass
