#!/usr/bin/env python
#coding=utf8

from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "ACT_CL_START"
class MR_COMMON_START_1003(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'DISVER',   'type':'s', 'mt':r'.*DISVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER','type':'s', 'mt':r'VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'org','type':'i', 'mt':r'from:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_COMMON_START_1003()

if __name__ == '__main__':
    test_str = r'00:00| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8700PQ|S:1003|PROD:KWSHELLEXT|DISVER:1.0.6.9076|OS:10.0.10586.2_|PLAT:X64|VER:1.0.1.8|GID:3868|CHID:MUSIC8700PQ|PN:rundll32.exe|MAC:00E04C004C69|UAC:1|ADMIN:0|ST:1488816008|CFGVER:19|ACT:ACT_CL_START|from:1|{}|U:>(183.228.118.104)TM:1488816002'
    mr_obj.LocalTest(test_str)
    pass
