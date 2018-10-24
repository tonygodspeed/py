#!/usr/bin/env python
#coding=utf8

from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")


str_act = "ACT_RECOMLOADER_CHECK_INST_GMUSIC"
class MR_1007_CHECK_INST_GMUSIC(mr_base):
	def __init__(self):
		mt_type = [
			{'key': 'VER', 'type': 's', 'mt': r'.*VER:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'CHID', 'type': 's', 'mt': r'CHID:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'MAC', 'type': 's', 'mt': r'MAC:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'ret', 'type': 'i', 'mt': r'ret:' + common_def.MT_VALUE_VALID_POSTFIX},
			{'key': 'nat', 'type': 'i', 'mt': r'nat:' + common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
		]
		mr_base.__init__(self, mt_type, str_act)

mr_obj = MR_1007_CHECK_INST_GMUSIC()

if __name__ == '__main__':
	test_str = r'<SRC:KWSHELLEXT_1.0.6.9051_MUSIC8400P2T1|S:1007|PROD:KWSHELLEXT|DISVER:1.0.6.9072|OS:10.0.14393.2_|PLAT:X64|VER:1.0.2.5|GID:2028|CHID:MUSIC8400P2T1|PN:rundll32.exe|MAC:BCAEC54AA5BA|UAC:1|ADMIN:0|ST:1477843205|CFGVER:12|ACT:ACT_RECOMLOADER_CHECK_INST_GMUSIC||ret:1|nat:-1|{}|U:>(118.251.23.126)TM:1477843198'

	mr_obj.LocalTest(test_str)
	pass
