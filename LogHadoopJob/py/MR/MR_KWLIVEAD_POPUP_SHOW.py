#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_KWLIVEAD_POPUP_SHOW"
class MR_KWLIVEAD_POPUP_SHOW(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'SRC',   'type':'s', 'mt':r'^.*<SRC:KWSHELLEXT_[\.0-9]*_' + common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER',   'type':'s', 'mt':r'.*VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_KWLIVEAD_POPUP_SHOW()

if __name__ == '__main__':
    test_str = r'00:04| [INFO]: <SRC:KWSHELLEXT_1.0.6.9072_MUSIC8500W4|S:1010|PROD:KWSHELLEXT|DISVER:1.0.6.9072|OS:10.0.14393.2_|PLAT:X64|VER:2.0.2.17|GID:2810|CHID:MUSIC8500W4|PN:rundll32.exe|MAC:902B3468269C|UAC:1|ADMIN:0|MVER:MUSIC_8.5.0.0_W4|MCID:20137889|ST:1481371732|CFGVER:14|ACT:ACT_KWLIVEAD_POPUP_SHOW||{}|U:>(222.244.99.151)TM:1481385606'
    mr_obj.LocalTest(test_str)
    pass
