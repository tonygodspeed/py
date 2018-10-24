#!/usr/bin/env python
#coding=utf8

from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")


str_act = "NSIS_UNINST"
class MR_NSIS_UNINST(mr_base):
	def __init__(self):
		mt_type = [
			{'key': 'NONE', 'type': 's', 'mt': r'.*TYPE:UNSTEnd.*?'},
			{'key': 'CURDT', 'type': 'i', 'mt': r'CURDT:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'GnVer', 'type': 'i', 'mt': r'GnVer:' + common_def.MT_VALUE_VALID_POSTFIX},
			{'key': 'GnVInDT', 'type': 'i', 'mt': r'GnVInDT:' + common_def.MT_VALUE_INVALID_POSTFIX},
			{'key': 'MAC', 'type': 's', 'mt': r'MAC:([^>]*).*?' + common_def.MT_VALUE_END},
		]
		mr_base.__init__(self, mt_type, str_act)

mr_obj = MR_NSIS_UNINST()

if __name__ == '__main__':
	#test_str = r'2%09<SRC:MUSIC_8.5.0.0_BCS1|ACT:NSIS_UNINST|TYPE:UNSTEnd|CURDT:17010|INSTDT:|US:17010|UnstBegin:1|UnstEnd:1|UsrData:0|GnVer:1|GnVInDT:17010|TCount:110511890|{Au_.exe}|U:55523277|MAC:F8BC125A7FA6>'
	test_str = r'<SRC:MUSIC_8.4.1.0_BCS5|ACT:NSIS_UNINST|TYPE:UNSTEnd|CURDT:17040|INSTDT:17040|US:0|UnstBegin:1|UnstEnd:1|UsrData:1|GnVer:|GnVInDT:|TCount:6742191|{Au_.exe}|U:47221162|MAC:701A04B2B31A>'
	#'00:00| [INFO]: <SRC:|ACT:ACT_RECOM_START|init_err:0|S:KWPRMODULE|PROD:KWSHELLEXT|VER:1.0.0.7|PLAT:WIN32|FROM:|GID:|CIN:|MAC:00E0702B553D|X64:1|UAC:0|ADMIN:1|OS:6.1.7601|MN:rundll32.exe|INT:1970-01-01|{}|U:>(112.239.100.203)TM:1467734403'

	mr_obj.LocalTest(test_str)
	pass
