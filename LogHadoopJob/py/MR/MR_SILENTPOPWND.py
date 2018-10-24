#!/usr/bin/env python
#coding=utf8

from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "SILENTPOPWND"
class MR_SILENTPOPWND(mr_base):
	def __init__(self):
		mt_type = [
                    {'key':'SRC',   'type':'s', 'mt':r'^.*<SRC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'TYPE','type':'s', 'mt':r'TYPE:'+ common_def.MT_VALUE_VALID_POSTFIX},
                    {'key':'Ret','type':'s', 'mt':r'Ret:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'U','type':'i', 'mt': common_def.MT_VALUE_U + common_def.MT_VALUE_END},
                  ]
		mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_SILENTPOPWND()

if __name__ == '__main__':
	test_str = r'00:55| [INFO]: <SRC:MUSIC_8.4.0.0_P2T1|ACT:SILENTPOPWND|S:KwMusic|SHOW WINDOW|TYPE:MiniPopup|Ret:0|CHANNEL_NAME:kuwo_jm713|PROD:MUSIC|VER:8.4.0.0_P2T1|PLAT:WIN32|FROM:kuwo_jm713.exe|UI:|{kuwo_jm713.exe}|K:80503971|RESEND:0|U:74169613>(115.150.106.0)TM:1480608057'
	#test_str = r'00:31| [INFO]: <SRC:KWSHELLEXT_1.0.6.9030_MUSIC8310BDS1|S:RECOM_TIPS|PROD:KWSHELLEXT|DISVER:1.0.6.9040|OS:6.1.7600.2_|PLAT:WIN32|VER:1.0.2.0|GID:1203|CHID:MUSIC8310BDS1|PN:RecomTips.exe|MAC:F04DA26B8CEC|UAC:0|ADMIN:1|ST:1467236451|CFGVER:5|ACT:ACT_RECOM_QUIT|quit_err:16||{}|U:>(180.191.155.250)TM:1467648029'
	mr_obj.LocalTest(test_str)
	pass