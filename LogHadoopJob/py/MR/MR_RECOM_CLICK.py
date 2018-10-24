#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_RECOM_CLICK"
class MR_RECOM_CLICK(mr_base_ex):
	def __init__(self):
		mr_base_ex.__init__(self,str_act)
		self.res_type = ["s","s","s","s","i","i","i","i","i"];
		self.res_name = ["VER","CHID","MAC","MCID","click_type","from","green_shot","is_green","is_auto"];

mr_obj = MR_RECOM_CLICK()

if __name__ == '__main__':
    test_str = r'00:00| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8520P2T1|S:RECOM_TIPS|PROD:KWSHELLEXT|DISVER:1.0.6.9072|OS:5.1.2600.2_Service Pack 3|PLAT:WIN32|VER:1.0.2.21|GID:3495|CHID:MUSIC8520P2T1|PN:RecomTips.exe|MAC:14CF92EB74D7|UAC:0|ADMIN:1|MVER:MUSIC_8.5.2.0_P2T1|MCID:22893472|ST:1462117590|CFGVER:16|ACT:ACT_RECOM_CLICK|click_type:4|from:3|green_shot:0|is_green:0|{}|U:>(123.97.183.153)TM:1484582405'
    mr_obj.LocalTest(test_str)
    pass
