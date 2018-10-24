#!/usr/bin/env python
#coding=utf8

from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_RECOM_QUIT"
class MR_RECOM_QUIT(mr_base_ex):
	def __init__(self):
		mr_base_ex.__init__(self,str_act)
		self.res_type = ["s","s","s","i","i","i","i","i"];
		self.res_name = ["VER","CHID","MAC","quit_err","from","green_shot","is_green","is_auto"];

mr_obj = MR_RECOM_QUIT()

if __name__ == '__main__':
	test_str = r'01:22| [INFO]: <SRC:KWSHELLEXT_1.0.6.9012_MUSIC8120AN0|S:RECOM_TIPS|PROD:KWSHELLEXT|DISVER:1.0.6.9061|OS:6.1.7601.2_Service Pack 1|PLAT:WIN32|VER:1.0.2.5|GID:690|CHID:MUSIC8120AN0|PN:RecomTips.exe|MAC:E8113286A172|UAC:0|ADMIN:1|ST:1472399895|CFGVER:9|ACT:ACT_RECOM_QUIT|quit_err:3|from:1|green_shot:0|is_green:0|{}|U:>(223.147.67.55)TM:1472400079'
	#test_str = r'00:31| [INFO]: <SRC:KWSHELLEXT_1.0.6.9030_MUSIC8310BDS1|S:RECOM_TIPS|PROD:KWSHELLEXT|DISVER:1.0.6.9040|OS:6.1.7600.2_|PLAT:WIN32|VER:1.0.2.0|GID:1203|CHID:MUSIC8310BDS1|PN:RecomTips.exe|MAC:F04DA26B8CEC|UAC:0|ADMIN:1|ST:1467236451|CFGVER:5|ACT:ACT_RECOM_QUIT|quit_err:16||{}|U:>(180.191.155.250)TM:1467648029'
	mr_obj.LocalTest(test_str)
	pass