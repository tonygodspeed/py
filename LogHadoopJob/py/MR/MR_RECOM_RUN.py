#!/usr/bin/env python
# coding=utf8
from MR_BASE import *

reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_RECOM_EXC_KUWO"
class MR_RECOM_RUN(mr_base_ex):
	def __init__(self):
		mr_base_ex.__init__(self,str_act)
		self.res_type = ["s","s","s","i","i","i","i","i","i","i","i"];
		self.res_name = ["VER","CHID","MAC","lst_err","setup_kw","sign_in","show_sign_in","from","green_shot","is_green","is_auto"];

mr_obj = MR_RECOM_RUN()

if __name__ == '__main__':
	#test_str = r'46:11| [INFO]: <SRC:KWSHELLEXT_1.0.6.9012_MUSIC8120AN0|S:RECOM_TIPS|PROD:KWSHELLEXT|DISVER:1.0.6.9061|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:1.0.2.5|GID:521|CHID:MUSIC8120AN0|PN:RecomTips.exe|MAC:C03FD50B8C9E|UAC:0|ADMIN:1|ST:1472420835|CFGVER:9|ACT:ACT_RECOM_EXC_KUWO|lst_err:0|path_exist:1|setup_kw:0|from:1|green_shot:0|is_green:0|{}|U:>(123.186.18.160)TM:1472420771'
	#test_str = r'00:22| [INFO]: <SRC:KWSHELLEXT_1.0.6.9030_MUSIC8300PQ|S:1005|PROD:KWSHELLEXT|DISVER:1.0.6.9030|OS:10.0.10586.2_|PLAT:X64|VER:1.0.1.2|GID:1118|CHID:MUSIC8300PQ|PN:rundll32.exe|MAC:000000000000|UAC:1|ADMIN:0|ST:1467647942|ACT:ACT_RECOM_EXC_KUWO|lst_err:0|path_exist:0|from:1|{}|U:>(123.186.80.132)TM:1467648021'
	test_str = r'00:31| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8111AN0|S:RECOM_TIPS|PROD:KWSHELLEXT|DISVER:1.0.6.9072|OS:5.1.2600.2_Service Pack 3|PLAT:WIN32|VER:1.0.2.10|GID:2468|CHID:MUSIC8111AN0|PN:RecomTips.exe|MAC:94DE8080A99F|UAC:0|ADMIN:1|ST:1478534423|CFGVER:12|ACT:ACT_RECOM_EXC_KUWO|lst_err:0|path_exist:1|setup_kw:0|sign_in:0|from:3|green_shot:0|is_green:0|{}|U:>(111.63.0.118)TM:1478534422'
	#test_str = r'38:53| [INFO]: <SRC:|S:RECOM_TIPS|PROD:KWSHELLEXT|DISVER:|OS:5.1.2600.2_Service Pack 3|PLAT:WIN32|VER:1.0.2.20|GID:|CHID:|PN:RecomTips.exe|MAC:000C29F3DFE6|UAC:0|ADMIN:1|MVER:MUSIC_8.5.0.0_BCS54|MCID:14012116|ST:1481611106|CFGVER:0|ACT:ACT_RECOM_EXC_KUWO|lst_err:0|path_exist:1|setup_kw:0|sign_in:1|show_sign_in:1|from:1|green_shot:0|is_green:0|{}|U:>(111.207.202.8)TM:1481611134'
	mr_obj.LocalTest(test_str)
	pass
