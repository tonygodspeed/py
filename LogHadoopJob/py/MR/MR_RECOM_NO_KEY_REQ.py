#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_RECOM_NO_KEY_REQ"
class MR_RECOM_NO_KEY_REQ(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'VER',   'type':'s', 'mt':r'.*VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'org','type':'i', 'mt':r'from:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_RECOM_NO_KEY_REQ()

if __name__ == '__main__':
    test_str = r'<SRC:KWSHELLEXT_1.0.6.9030_MUSIC8310W4|S:RECOM_TIPS|PROD:KWSHELLEXT|DISVER:1.0.6.9040|OS:6.1.7600.2_|PLAT:X64|VER:1.0.2.0|GID:544|CHID:MUSIC8310W4|PN:RecomTips.exe|MAC:000C2956AC54|UAC:1|ADMIN:1|ST:1467258150|CFGVER:2|ACT:ACT_RECOM_NO_KEY_REQ||from:1|{}|U:>(111.207.202.5)TM:1467258118'
    mr_obj.LocalTest(test_str)
    pass
