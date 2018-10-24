#!/usr/bin/env python
#coding=utf8
from MR_BASE import *
reload(sys)
sys.setdefaultencoding("utf-8")

str_act = "COMMON_START_1013"
class MR_COMMON_START_1013(mr_base):
    def __init__(self):
        mt_type = [
                    {'key':'DISVER',   'type':'s', 'mt':r'.*DISVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'VER','type':'s', 'mt':r'VER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CHID','type':'s', 'mt':r'CHID:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'MAC','type':'s', 'mt':r'MAC:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'CFGVER','type':'s', 'mt':r'CFGVER:'+ common_def.MT_VALUE_INVALID_POSTFIX},
                    {'key':'cookie_exist','type':'i', 'mt':r'cookie_exist:'+ common_def.MT_VALUE_VALID_POSTFIX + common_def.MT_VALUE_END},
                  ]
        mr_base.__init__(self,mt_type,str_act)

mr_obj = MR_COMMON_START_1013()

if __name__ == '__main__':
    test_str = r'13:00| [INFO]: <SRC:KWSHELLEXT_1.0.6.9051_MUSIC8710BCS9|S:1013|PROD:KWSHELLEXT|DISVER:1.0.6.9077|OS:10.0.14393.2_|PLAT:X64|VER:1.0.0.1|GID:3791|CHID:MUSIC8710BCS9|PN:rundll32.exe|MAC:7845C403A55A|UAC:1|ADMIN:0|MVER:MUSIC_8.7.1.0_BCS10|MCID:28479825|ST:1487571051|CFGVER:17|ACT:COMMON_START_1013|cookie_exist:0|{}|U:>(111.207.202.5)TM:1487571182'
    mr_obj.LocalTest(test_str)
    pass
