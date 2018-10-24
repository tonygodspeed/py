#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "COMMON_START_1010"
class MR_COMMON_START_1010(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'DISVER',   'type':'s', 'mt':r'.*DISVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER','type':'s', 'mt':r'VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CHID','type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MCID','type':'i', 'mt':r'MCID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CFGVER','type':'s', 'mt':r'CFGVER:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_COMMON_START_1010()

if __name__ == '__main__':
    test_str = r'00:02| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8500AN0|S:1010|PROD:KWSHELLEXT|DISVER:1.0.6.9072|OS:6.1.7601.2_Service Pack 1|PLAT:X64|VER:2.0.2.17|GID:2549|CHID:MUSIC8500AN0|PN:rundll32.exe|MAC:00E04C40F078|UAC:0|ADMIN:1|MVER:MUSIC_8.5.0.0_AN0|MCID:23380535|ST:1481558576|CFGVER:14|ACT:COMMON_START_1010||{}|U:>(116.1.46.3)TM:1481558403'
    mr_obj.LocalTest(test_str)
    pass
