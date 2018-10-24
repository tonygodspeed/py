#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_KWLIVEAD_POPUP"
class MR_KWLIVEAD_POPUP(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'SRC',   'type':'s', 'mt':r'^.*<SRC:KWSHELLEXT_[\.0-9]*_' + common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER',   'type':'s', 'mt':r'.*VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
					{'key':'MAC',	'type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
					{'key':'ret',	'type':'i', 'mt':r'ret:'+ common_def.MT_VALUE_INVALID_POSTFIX},
					{'key':'wnd_create',	'type':'i', 'mt':r'create:'+ common_def.MT_VALUE_INVALID_POSTFIX},
					{'key':'wnd_show',	'type':'i', 'mt':r'show:'+ common_def.MT_VALUE_INVALID_POSTFIX},
					{'key':'wnd_destroy',	'type':'i', 'mt':r'destroy:'+ common_def.MT_VALUE_INVALID_POSTFIX},
					{'key':'wnd_dret',	'type':'i', 'mt':r'dret:'+ common_def.MT_VALUE_INVALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_KWLIVEAD_POPUP()

if __name__ == '__main__':
    test_str = r'00:23| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8500AN0|S:1010|PROD:KWSHELLEXT|DISVER:1.0.6.9072|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:2.0.2.17|GID:2629|CHID:MUSIC8500AN0|PN:rundll32.exe|MAC:B8975A20D44E|UAC:0|ADMIN:1|MVER:MUSIC_8.5.0.0_AN0|MCID:14832382|ST:1481552305|CFGVER:14|ACT:ACT_KWLIVEAD_POPUP|ret:7|create:1|show:1|destroy:1|dret:2|{}|U:>(119.141.24.79)TM:1481558424'
    mr_obj.LocalTest(test_str)
    pass
